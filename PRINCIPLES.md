# Research Principles and Method

## P1. Discrepancy before dismissal
Do not discard a discrepancy before recording it and investigating plausible sources. This does not mean treating every anomaly as meaningful.

## P2. Explicit comparison
Every error measure must specify the compared quantities, reference or expectation, coordinate system and units, time window and sampling method, uncertainty and calibration, and rules for missing or excluded observations.

## P3. Separate error, failure, and uncertainty
- Error: difference relative to a defined reference or comparison.
- Failure: violation of a defined requirement or loss of a specified capability or relation.
- Uncertainty: characterized limitation in knowledge of a measurement or result.

A failure can occur without measurement error. A measurement can have uncertainty without system failure.

## P4. Invariance must name its transformation class
State what changes, what is held fixed, what property or relation should remain, and the tolerance or uncertainty.

## P5. Observer and instrument accountability
Record instrument identity, configuration, calibration, placement, sampling, processing, and observer-dependent choices. Estimate measurement-induced perturbation where relevant.

## P6. Symmetric testing
Define in advance what supports, limits, or contradicts a hypothesis. Report results that do not support it.

## P7. Replication and robustness
Distinguish repeatability under the same setup from reproducibility under changed operators, instruments, locations, or implementations.

## P8. No forced cross-domain equivalence
Cross-domain comparison requires an explicit mapping between operationally defined variables and transformations. Similar language or visual appearance is insufficient.

## P9. Preserve the record
Retain raw data, metadata, code, protocol versions, exclusions, failed runs, and reasons for revisions. Never silently overwrite an earlier hypothesis or result.

## P10. Separate exploration from confirmation
Exploratory analysis may generate hypotheses. Confirmatory analysis tests hypotheses using criteria fixed before examining the relevant outcomes.

## P11. Verifiable structures, not monoliths
Complex arguments should be decomposable into identifiable units with explicit claims, evidence or derivations, dependencies, and verification states. Their architecture must expose consistency checks, corroboration, unresolved gaps, and the consequences of removing a unit. Dependency relations must not conceal circular justification. See [Da Vinci Bridge Principle](DAVINCI_BRIDGE_PRINCIPLE.md). This is a methodological design principle, not a claim that every argument has already been shown to admit an optimal decomposition.
