# MIOD-001 — Annex: Comparative Methodological Criterion from the Sparse Reward Subsystem

**Type:** criterio metodológico comparativo
**Status:** HYPOTHESIS / PENDING
**Date:** 2026-11-25 (America/Tijuana)
**Parent protocol:** `EXPERIMENTS/MIOD-001-WATER/protocol.md` v0.1 — protocol unchanged by this annex.
**Parent protocol SHA (file):** `fd5b203545a87af4f546cd946951df2a5ccfd3ba`
**Parent HEAD at annex creation:** `4f69be0b484cc99d313557c251683b0a5f48f624`
**Recorded by:** Luis Burciaga, via Zorra

## External reference (only)

Xu, Guowei; Yuksekgonul, Mert; Zou, James. *Sparse Reward Subsystem in Large Language Models*. arXiv:2602.00986. v1 submitted 1 Feb 2026; v3 revised 4 Nov 2026; NeurIPS 2026.
https://arxiv.org/abs/2602.00986
Code: https://github.com/zou-group/reward_subsystem

This annex cites the paper as an experimental strategy. It does not import its results as MIOD evidence.

## Rule

```
STATISTICAL_SELECTION ≠ FUNCTIONAL_SELECTION
```

Do not confuse statistical selection with functional selection.

## What the paper does (external evidence only)

1. **Probe:** identifies predictive dimensions in hidden states.
2. **Pruning:** identifies a compact subset — less than 1% of neurons suffice to preserve value prediction (AUC).
3. **Ablation:** tests functional dependence — zeroing the top 1% of value neurons in a single layer drops MATH500 accuracy far more than zeroing 1% at random.
4. **Error signal:** dopamine neurons encode step-level TD / reward-prediction error, allowing study of posterior changes.

What the paper does **not** demonstrate: that an LLM is conscious of its errors. The authors state the value/dopamine terms are analogies in computational role — residual-stream coordinates selected through supervised probing — not biologically characterized cell types, and that intervention experiments are preliminary, with confounds (e.g. probe stability, large activation magnitudes) remaining.

## Comparative hypothesis (MIOD-001)

This is a comparative hypothesis, **not** a MIOD result. No physical data have been collected or analyzed under protocol v0.1 at the date of this annex.

Investigate whether MIOD-001 and the paper describe two aspects of a more general phenomenon: selection of information and functional transformation produced by error. Do not assert that MIOD and the paper say the same thing.

Three levels to keep distinct in MIOD-001:

- **Available information:** present / decodable in the system.
- **Selected information:** retained under a defined selection criterion.
- **Behaviour-modifying information:** a change that alters subsequent organization or behaviour of the system.

## Two independent questions

**Q1 — Selection:** What component is necessary to produce or maintain the reorganization?

**Q2 — Discrepancy:** Does the difference between the expected state and the observed state predict a posterior transformation?

## Additional question (MIOD-specific)

**Q3 — Fate of a modification:** What determines whether a modification of the system is conserved, discarded, or incorporated into a new organization?

Q3 is not answered by the paper. It requires longitudinal follow-up: observation after perturbation removal, recovery period, and repeat trials (protocol §4, §5, §7), distinguishing discard, conservation, and incorporation as separate outcomes.

## Controls required before claiming necessity

Before a suppression result can be read as necessity, all of the following are required:

1. **Equivalent random ablation/suppression:** a suppression of the same magnitude, applied to randomly chosen components, does not produce the same loss.
2. **Non-predictive component control:** suppressing a component that is not predictive / not selected does not produce the same loss.
3. **Reversibility:** the effect reverses (or is shown not to reverse, with that outcome recorded) when the suppression is removed, where reversibility is applicable to the intervention used.
4. **Baseline functions intact:** functions basal to the system are checked and remain intact under the intervention.

## Explicit warning

> La pérdida de una función tras una supresión no demuestra necesidad específica si la intervención también deteriora las funciones basales del sistema.

Loss after suppression is not, by itself, evidence of specific necessity.

## Separation of evidence

- Evidence from Xu et al. is external evidence about LLMs.
- Evidence from MIOD-001 is experimental evidence about water under controlled vibration.
- Do not mix the two. No claim in this annex counts as MIOD experimental evidence.
- Do not adapt the experiment to the result expected to be found.

## Order of work

1. Close the operational definitions of MIOD-001 first (protocol §3 variables, §5 observables, §7 analysis plan, including primary outcome, exclusion criteria, and acceptance / limitation / rejection criteria).
2. Then execute experiments.
3. Record this annex's hypothesis as HYPOTHESIS / PENDING until tested under those closed definitions.
