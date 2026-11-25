# Changelog

## 2026-11-25 — MIOD-001 synthetic indicator pilot
- Added `EXPERIMENTS/MIOD-001-WATER/SYNTHETIC/` with a reproducible NumPy implementation of Pearson correlation and biased sample distance correlation, synthetic generators C0-C6, same-DGP null calibration, held-out evaluation, confusion metrics, and unit tests.
- Corrected C6 to compare two distinct even nonlinear mechanisms, X² and X⁴, whose population Pearson correlations with symmetric X are zero; dCor is evaluated rather than assumed to distinguish them.
- Calibrated thresholds from independent same-generating-process sample pairs and reserved separate seed streams for evaluation.
- Completed pilot: n=250, 200 calibration and 200 evaluation replicates per condition, seed 20261125; 7 unit tests passed. Cnull FPR=4%; C6 detection: Pearson 4%, dCor 31%.
- Recorded pilot metrics and interpretation limits in SYNTHETIC/pilot_summary.json. The larger n=500/1,000-replicate run exceeded the available execution window and was not included.
- Synthetic indicator evaluation only. No validation of water physics; MIOD-001 physical protocol v0.1 remains unchanged.

## 2026-11-25 — MIOD-001 measurement uncertainty
- Added `EXPERIMENTS/MIOD-001-WATER/MEASUREMENT_UNCERTAINTY.md`, a draft method note for evaluating and reporting uncertainty by directly measured channel.
- Distinguished Type A and Type B evaluation methods; clarified individual-reading dispersion versus uncertainty of a mean.
- Added cautions for autocorrelation in time-series data, conditional resolution/specification models, calibration contributions, covariance, and uncertainty propagation.
- Left all numerical uncertainty budgets pending identification of the apparatus, sensors, acquisition settings, and calibration evidence.
- Marked the note DRAFT / NOT PREREGISTERED. The MIOD-001 v0.1 parent protocol remains unchanged.

## 2026-11-23 — Da Vinci Bridge research track
- Added DB-004, the finite-group prefix-return theorem: a sequence of |G| elements in a finite group G contains a nonempty consecutive block whose ordered product is the identity.
- Verified the argument for non-abelian groups; the proof uses prefix products, finite counting, associativity, and inverses, but not commutativity.
- Connected DB-004 to DB-002 by identifying the cyclic group Z/nZ as the additive special case.
- Added a finite-monoid counterexample showing that prefix-product repetition alone is insufficient without inverses.
- Recorded sharpness of the uniform length bound using a generator repeated m-1 times in C_m.
- Located a direct published antecedent in Alford, Granville, and Pomerance, Section 2; classified DB-004 as structural generalization/reconstruction, not a new theorem.
- No independent replacement for finite counting and no mathematical novelty are claimed.

## 2026-11-23 — Da Vinci Bridge research track (initial pilots)
- Added the mathematical trunk-assembly method and corrected the Da Vinci Bridge principle to reflect the intended research concept: independently proven results assembled under explicit compatibility conditions.
- Recorded DB-001, a structured reconstruction of Euclid's proof of infinitely many primes, including trunk roles and removal audit. No novelty is claimed.
- Recorded DB-002, the modular consecutive-segment theorem, both prefix-sum proof variants, and audits of counting, group language, difference cocycles, induction, reflection, and substitution candidates.
- Opened DB-003 on palindromic segment symmetry. Proved the interval-reflection lemma and orbit consequence; refuted the conjecture that a centered divisible segment must always exist using the counterexample (1,2,1) modulo 3.
- Distinguished established results, constructions, connectors, derived consequences, counterexamples, and open research questions.
- No new theorem or independent replacement for finite counting is claimed.

## 2026-11-23 — Initial foundation
- Established the repository as a research program centered on error, invariance, failure, observation, and relational transformation.
- Added foundational statement and research principles.
- Added provisional error, invariance, and relational-transformation notes.
- Registered three proposed hypotheses: structured error, cross-system relational invariance, and observer dependence.
- Added the MIOD-001 water-vibration protocol design draft.
- Explicitly marked mathematical structures and hypotheses as provisional; no confirmatory evidence is claimed.

