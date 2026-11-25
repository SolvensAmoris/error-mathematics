# MIOD-001 — Measurement uncertainty by channel

**Status:** methodological working note; DRAFT / NOT PREREGISTERED  
**Scope:** uncertainty estimation for each directly recorded measurement channel.  
**Parent protocol:** `EXPERIMENTS/MIOD-001-WATER/protocol.md` v0.1. This note does not modify that protocol.

## 1. Purpose

Estimate and report the uncertainty associated with each channel without inventing sensor specifications or treating uncertainty as a known measurement error. No numerical budget can be completed until the apparatus, sensors, calibration records, acquisition settings, and measurement procedures are identified.

Type A and Type B describe methods of evaluating uncertainty components. They are not synonyms for random and systematic effects, and should not be called “Type A errors” or “Type B errors.”

## 2. Define the measurement result first

For each channel, specify:

- measurand and operational definition;
- unit, sensor make/model/serial number, location and orientation;
- acquisition range, resolution, sampling rate, bandwidth/response time and exposure settings where applicable;
- calibration status, correction applied, certificate and validity;
- whether the reported result is an individual reading, a mean over a stated interval, a fitted parameter, or another derived quantity.

Do not combine readings that refer to different measurands or materially different conditions.

## 3. Type A evaluation: observed repeatability

Under a defined stable condition, collect repeated observations using a documented procedure. For (n) independent observations (x_i), calculate the sample standard deviation (s).

- For the dispersion of an individual reading, report (s) as the observed repeatability component.
- For the uncertainty of the arithmetic mean, use (u_A=s/\sqrt{n}), only when the observations are reasonably independent and represent the same measurement condition.
- For time-series samples, do not assume adjacent samples are independent. Inspect drift and autocorrelation; estimate effective information or use a time-series/blocked-trial method appropriate to the acquisition design. Increasing the sample count does not automatically reduce uncertainty by (1/\sqrt n).
- Separate within-run signal variation from between-run repeatability. They answer different questions.

Record (n), sampling interval, run count, stabilization period, mean, (s), and the method used to handle dependence or drift.

## 4. Type B evaluation: instrument and method information

Build a component budget from available evidence, such as calibration certificates, manufacturer specifications, reference standards, resolution, and documented environmental limits. Convert each contribution to a standard uncertainty using the distribution and coverage information actually supplied.

Examples:

- **Digital resolution:** if the display increment is (r), and rounding error is reasonably modeled as uniform over ([-r/2,r/2]), then (u_{res}=r/\sqrt{12}). State the uniform-quantization assumption.
- **Bounded specification:** if a source gives only a limit (pm a), do not automatically assume a uniform distribution. If equal probability within the limits is justified and no better information exists, (u=a/\sqrt{3}). If the source instead gives an expanded uncertainty, confidence interval, standard deviation, or coverage factor, interpret it accordingly; do not apply the rectangular conversion blindly.
- **Calibration:** use the certificate's stated uncertainty, coverage factor, traceability information and any required correction. Do not count the same calibration contribution again under a manufacturer specification.

Consider relevant channel-specific effects: sensor drift, linearity, hysteresis, repeatability, temperature sensitivity, positioning, timing/base-clock uncertainty, bandwidth, response time, camera exposure, pixel calibration, segmentation, and environmental influences. Include only effects relevant to the measurand and method.

## 5. Combine contributions

Express all components as standard uncertainties in the measurand's units, or propagate them through an explicit measurement model. For independent components:

`u_c = sqrt(u_1^2 + u_2^2 + ... + u_m^2)`

If components are correlated, include covariance terms using the law of propagation of uncertainty; do not use root-sum-of-squares as if they were independent. Apply significant known corrections before reporting the result, and include uncertainty associated with those corrections.

For a derived quantity (y=f(x_1,...,x_m)), document the function and sensitivity coefficients. Use a suitable propagation method; the first-order covariance formula is appropriate only when its approximation is adequate.

## 6. Reporting

For every channel and every reported measurand, retain:

- estimate and unit;
- whether it is an individual reading, run-level statistic, or mean;
- each uncertainty component, source, evaluation method (Type A/Type B), distribution assumption and conversion;
- covariance/dependence treatment;
- combined standard uncertainty (u_c);
- expanded uncertainty (U=k u_c), only if reported, with (k), degrees of freedom/method and coverage statement justified;
- calibration correction, date, certificate, instrument identifiers and raw-data reference.

Do not label (x\pm u_c) a 95% confidence interval by default. A combined standard uncertainty is not automatically a 95% interval; coverage depends on the distribution, degrees of freedom and method used.

Keep raw readings unrounded. Round only for presentation, consistently with the reported uncertainty.

## 7. MIOD-001 decision gate

No channel receives a numerical uncertainty value in this note until its sensor and acquisition configuration are identified. If calibration or specification information is unavailable, mark that component **UNKNOWN / NOT QUANTIFIED** rather than assigning a convenient number.

Before using a channel to claim a structural or relational change, establish that the observed difference is distinguishable from baseline variability and the channel's measurement uncertainty under the same analysis procedure. This alone does not establish reorganization or causality.

If the apparatus cannot resolve the proposed difference with adequate precision, report that MIOD-001 cannot currently test that distinction. Do not reinterpret an unresolved measurement as evidence of absence.

## 8. References

- NIST Technical Note 1297, §2, classification of uncertainty components: https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-2-classification-components-uncertainty
- NIST TN 1297, §3, Type A evaluation: https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-3-type-evaluation-standard-uncertainty
- NIST TN 1297, §4, Type B evaluation: https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-4-type-b-evaluation-standard-uncertainty
- NIST TN 1297, §5, combined standard uncertainty: https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-5-combined-standard-uncertainty
- NIST TN 1297, Appendix A, propagation and covariance: https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-law-propagation-uncertainty
