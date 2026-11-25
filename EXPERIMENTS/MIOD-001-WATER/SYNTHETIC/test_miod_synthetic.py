import unittest
import numpy as np
from miod_synthetic import pearson,dcor,evaluate

class IndicatorTests(unittest.TestCase):
 def test_pearson_perfect_correlations(self):
  x=np.array([-2.,-1.,0.,1.,2.]); self.assertAlmostEqual(pearson(x,x),1.,places=12); self.assertAlmostEqual(pearson(x,-x),-1.,places=12)
 def test_pearson_positive_affine_invariance(self):
  x=np.array([-2.,-1.,0.,1.,2.]); y=np.array([1.,0.,2.,3.,4.]); self.assertAlmostEqual(pearson(x,y),pearson(7+3*x,-4+2*y),places=12)
 def test_dcor_range_and_dependence(self):
  rng=np.random.default_rng(7); x=rng.uniform(-1,1,250); dep=x**2+rng.normal(0,.05,250); ind=rng.normal(0,1,250)
  self.assertGreaterEqual(dcor(x,dep),0.); self.assertLessEqual(dcor(x,dep),1.); self.assertGreater(dcor(x,dep),dcor(x,ind))
 def test_dcor_affine_invariance(self):
  rng=np.random.default_rng(8); x=rng.normal(size=100); y=x**2+rng.normal(0,.2,100)
  self.assertAlmostEqual(dcor(x,y),dcor(10+3*x,-2+2*y),places=10)
 def test_c6_even_generators_have_small_pearson(self):
  rng=np.random.default_rng(9); x=rng.uniform(-1,1,100000); e=rng.normal(0,.05,x.size)
  self.assertLess(abs(pearson(x,x**2+e)),.02); self.assertLess(abs(pearson(x,x**4+e)),.02)
 def test_constant_pearson_rejected(self):
  with self.assertRaises(ValueError): pearson(np.ones(5),np.arange(5.))
 def test_pipeline_reproducible(self):
  a=evaluate(n=40,reps=3,cal_reps=20,seed=123); b=evaluate(n=40,reps=3,cal_reps=20,seed=123)
  self.assertEqual(a["thresholds"],b["thresholds"]); self.assertEqual(a["results"],b["results"])
if __name__=="__main__": unittest.main()
