#!/usr/bin/env python3
"""MIOD-001 synthetic indicator evaluation. Synthetic data only, not water physics."""
import argparse,csv,json,math,platform
from pathlib import Path
import numpy as np
VERSION="0.1.0"; KEYS=("pearson","dcor"); TOL=1e-10

def pearson(x,y):
 x=np.asarray(x,float).ravel(); y=np.asarray(y,float).ravel()
 if x.size!=y.size or x.size<2: raise ValueError("equal-length vectors of size >=2 required")
 sx,sy=np.std(x),np.std(y)
 if sx==0 or sy==0: raise ValueError("Pearson undefined for constant input")
 return float(np.mean((x-x.mean())*(y-y.mean()))/(sx*sy))

def dcor(x,y):
 x=np.asarray(x,float).ravel(); y=np.asarray(y,float).ravel()
 if x.size!=y.size or x.size<2 or not np.isfinite(x).all() or not np.isfinite(y).all(): raise ValueError("finite equal-length vectors of size >=2 required")
 a=np.abs(x[:,None]-x[None,:]); b=np.abs(y[:,None]-y[None,:])
 a-=a.mean(0,keepdims=True); a-=a.mean(1,keepdims=True); a+=a.mean()
 b-=b.mean(0,keepdims=True); b-=b.mean(1,keepdims=True); b+=b.mean()
 v=float(np.mean(a*b)); den=math.sqrt(float(np.mean(a*a))*float(np.mean(b*b)))
 if den<=0: raise ValueError("dCor undefined for constant input")
 return float(math.sqrt(max(0.,v)/den))

def measure(x,y): return {"pearson":pearson(x,y),"dcor":dcor(x,y)}
def draw(rng,n,kind,noise=.35):
 x=rng.uniform(-1,1,n); e=rng.normal(0,noise,n)
 if kind=="linear": y=x+e
 elif kind=="quadratic": y=x**2+e
 elif kind=="quartic": y=x**4+e
 elif kind=="independent": y=rng.normal(0,1,n)
 else: raise ValueError(kind)
 return x,y
def delta(a,b): return {k:abs(b[k]-a[k]) for k in KEYS}

def calibrate(n,reps,seed,case):
 rng=np.random.default_rng(seed)
 mechanisms={"C4":["linear"],"C5":["linear"],"C6":["quadratic","quartic"],"C3":["linear"]}.get(case,["linear"])
 vals={k:[] for k in KEYS}
 for i in range(reps):
  m=mechanisms[i%len(mechanisms)]
  x,y=draw(rng,n,m); u,v=draw(rng,n,m); d=delta(measure(x,y),measure(u,v))
  for k in KEYS: vals[k].append(d[k])
 return {k:float(np.quantile(v,.95,method="higher")) for k,v in vals.items()}

def evaluate(n=250,reps=200,cal_reps=200,seed=20261125):
 if n<20 or reps<1 or cal_reps<20: raise ValueError("n>=20, reps>=1, calibration reps>=20 required")
 kids=np.random.SeedSequence(seed).spawn(10)
 cs=[int(s.generate_state(1)[0]) for s in kids[:4]]
 es=[int(s.generate_state(1)[0]) for s in kids[4:]]
 th={c:calibrate(n,cal_reps,cs[i],c) for i,c in enumerate(("C3","C4","C5","C6"))}
 rows=[]
 rng=np.random.default_rng(es[0])
 for i in range(reps):
  x,y=draw(rng,n,"linear"); ref=measure(x,y)
  for case,u,v in (("C0_replica",x.copy(),y.copy()),("C1_shift",x+10,y+20),("C2_positive_scale",3*x,2*y)):
   d=delta(ref,measure(u,v)); rows.append({"case":case,"replicate":i,"truth_change":False,**{f"delta_{k}":d[k] for k in KEYS},**{f"threshold_{k}":None for k in KEYS},**{f"detected_{k}":d[k]>TOL for k in KEYS}})
 rng=np.random.default_rng(es[1])
 for i in range(reps):
  x,y=draw(rng,n,"linear"); u,v=draw(rng,n,"linear"); d=delta(measure(x,y),measure(u,v))
  rows.append({"case":"Cnull_independent_same_DGP","replicate":i,"truth_change":False,**{f"delta_{k}":d[k] for k in KEYS},**{f"threshold_{k}":th["C3"][k] for k in KEYS},**{f"detected_{k}":d[k]>th["C3"][k] for k in KEYS}})
 rng=np.random.default_rng(es[2])
 for level in (.05,.10,.25,.50):
  for i in range(reps):
   x,y=draw(rng,n,"linear"); ref=measure(x,y); u=x+rng.normal(0,level,n); v=y+rng.normal(0,level,n); d=delta(ref,measure(u,v))
   rows.append({"case":f"C3_noise_{level:.2f}","replicate":i,"truth_change":None,**{f"delta_{k}":d[k] for k in KEYS},**{f"threshold_{k}":th["C3"][k] for k in KEYS},**{f"detected_{k}":d[k]>th["C3"][k] for k in KEYS}})
 for case,ma,mb,sseed,ck in (("C4_linear_to_quadratic","linear","quadratic",es[3],"C4"),("C5_dependence_to_independence","linear","independent",es[4],"C5"),("C6_quadratic_to_quartic","quadratic","quartic",es[5],"C6")):
  rng=np.random.default_rng(sseed)
  for i in range(reps):
   x,y=draw(rng,n,ma); u,v=draw(rng,n,mb); d=delta(measure(x,y),measure(u,v))
   rows.append({"case":case,"replicate":i,"truth_change":True,**{f"delta_{k}":d[k] for k in KEYS},**{f"threshold_{k}":th[ck][k] for k in KEYS},**{f"detected_{k}":d[k]>th[ck][k] for k in KEYS}})
 results={}
 for case in sorted({r["case"] for r in rows}):
  g=[r for r in rows if r["case"]==case]; truth=g[0]["truth_change"]; item={"n":len(g)}
  for k in KEYS:
   vals=[r[f"delta_{k}"] for r in g]; det=[bool(r[f"detected_{k}"]) for r in g]
   tp=sum(det) if truth is True else (None if truth is None else 0); fn=len(g)-tp if truth is True else (None if truth is None else 0)
   fp=sum(det) if truth is False else (None if truth is None else 0); tn=len(g)-fp if truth is False else (None if truth is None else 0)
   item[k]={"delta_median":float(np.median(vals)),"delta_p05":float(np.quantile(vals,.05)),"delta_p95":float(np.quantile(vals,.95)),"detections":int(sum(det)),"detection_rate":float(np.mean(det)),"threshold":g[0].get(f"threshold_{k}"),"truth_change":truth,"TP":tp,"FN":fn,"FP":fp,"TN":tn,"FPR":fp/(fp+tn) if fp is not None and fp+tn else None,"FNR":fn/(fn+tp) if fn is not None and fn+tp else None,"FDR":fp/(fp+tp) if fp is not None and fp+tp else None}
  results[case]=item
 labeled=[r for r in rows if r["case"] in {"Cnull_independent_same_DGP","C4_linear_to_quadratic","C5_dependence_to_independence","C6_quadratic_to_quartic"}]
 globalm={}
 for k in KEYS:
  tp=sum(r["truth_change"] is True and r[f"detected_{k}"] for r in labeled); fn=sum(r["truth_change"] is True and not r[f"detected_{k}"] for r in labeled)
  fp=sum(r["truth_change"] is False and r[f"detected_{k}"] for r in labeled); tn=sum(r["truth_change"] is False and not r[f"detected_{k}"] for r in labeled)
  globalm[k]={"TP":tp,"FN":fn,"FP":fp,"TN":tn,"FPR":fp/(fp+tn),"FNR":fn/(fn+tp),"FDR":fp/(fp+tp),"warning":"FDR depends on synthetic prevalence, not a field estimate."}
 return {"status":"SYNTHETIC_INDICATOR_EVALUATION_ONLY","program_version":VERSION,"parameters":{"n":n,"evaluation_replicates":reps,"calibration_replicates":cal_reps,"seed":seed,"calibration_seed_streams":cs,"evaluation_seed_streams":es,"tolerance_exact_controls":TOL,"calibration_quantile":.95},"environment":{"python":platform.python_version(),"numpy":np.__version__},"thresholds":th,"results":results,"global_confusion_metrics":globalm,"interpretation":["Pearson detects linear association only.","Biased sample dCor detects broad dependence, not dependency identity.","C6 tests whether scalar dCor changes between two even nonlinear mechanisms.","Exact transformation and independent-resampling controls answer different questions.","No result is evidence of physical water reorganization."],"rows":rows}

def write_outputs(result,outdir):
 outdir=Path(outdir); outdir.mkdir(parents=True,exist_ok=True); payload=dict(result); rows=payload.pop("rows")
 (outdir/"summary.json").write_text(json.dumps(payload,indent=2),encoding="utf-8")
 with (outdir/"replicate_results.csv").open("w",newline="",encoding="utf-8") as f:
  fields=sorted({k for r in rows for k in r}); w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
def main():
 p=argparse.ArgumentParser(description=__doc__); p.add_argument("--n",type=int,default=250); p.add_argument("--replicates",type=int,default=200); p.add_argument("--calibration-replicates",type=int,default=200); p.add_argument("--seed",type=int,default=20261125); p.add_argument("--outdir",type=Path,default=Path("results")); a=p.parse_args()
 result=evaluate(a.n,a.replicates,a.calibration_replicates,a.seed); write_outputs(result,a.outdir); print(json.dumps({k:v for k,v in result.items() if k!="rows"},indent=2))
if __name__=="__main__": main()
