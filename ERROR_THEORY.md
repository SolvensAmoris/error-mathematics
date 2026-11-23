# Toward a Theory of Error

**Status:** conceptual framework; formal theory not yet established.

## 1. Why make error central?
Many workflows optimize performance by minimizing deviations from a target. This project asks what structure can be learned by examining deviations themselves.

The project does not assume that every error is informative, that error is always intrinsic to a system, or that conventional error analysis is inadequate. It seeks a broader framework in which the origin, relations, persistence, and transformations of discrepancies are primary research objects.

## 2. Working definition
An error is a difference between two explicitly specified objects of comparison, under a stated measurement and interpretation procedure.

A general placeholder is:

E := Compare(X, Y | C, M)

X and Y are compared quantities or states; C represents comparison conditions; M represents measurement and interpretation. The comparison need not be subtraction. It may be numerical, temporal, structural, relational, or categorical.

## 3. Candidate error classes
1. Reference discrepancy: observation versus a declared reference.
2. Predictive discrepancy: prediction versus subsequent observation.
3. Inter-observer discrepancy: differences between observers or observation systems.
4. Instrumental discrepancy: differences attributable to calibration, resolution, drift, or procedure.
5. Model discrepancy: systematic structure not represented by a model.
6. Relational discrepancy: change or incompatibility in relations among components.
7. Temporal discrepancy: differences in timing, order, persistence, or transition.
8. Scale discrepancy: changes in a proposed relation when the level of description changes.

These classes may overlap. Classification must be supported by evidence.

## 4. Error is not automatically information
A discrepancy becomes informative only when analysis shows reproducible or otherwise defensible structure relevant to a question. Candidate tests include dependence on controlled conditions, persistence across trials, predictive value on independent data, sensitivity to observer or instrument changes, and robustness against plausible confounders and alternative models.

## 5. Formalization agenda
Develop a typed representation of comparison objects; an explicit comparison operator; provenance for reference, observer, instrument, and processing; a decomposition where identifiable; measures for persistence and structure; and criteria for distinguishing informative discrepancy from noise and artifact.

## 6. Open questions
- Can error be defined without a reference, or does every error require explicit comparison?
- Which discrepancies are properties of a system, and which are properties of a relation between system and observer?
- Can two domains share an error transformation while having different physical observables?
- What information is required to distinguish error, failure, uncertainty, and novelty?
