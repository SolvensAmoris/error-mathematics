# Da Vinci Bridge: Mathematical Trunk Assembly

**Status:** Research method, version 0.1.  
**Scope:** Construction and audit of mathematical arguments from independently established results.

## 1. Core idea

A *trunk* is a mathematical result that already has standing on its own: a theorem, lemma, identity, principle, or property with a valid proof and explicit conditions. It is not an unfinished task, software module, or dependency placeholder.

The research question is whether several independently justified trunks, assembled in a particular arrangement, yield a conclusion that none of the trunks yields alone.

The potential discovery may lie in the selection, compatibility, transformation, or arrangement of established results. It must not be confused with proving the trunks themselves.

## 2. Formal shape

A first schematic form is:

\[
(P_1\land P_2\land\cdots\land P_r)\land C
\;\Longrightarrow\; H,
\]

where:

- each \(P_i\) is an independently established mathematical result;
- each \(P_i\) carries its own domain, hypotheses, definitions, and proof;
- \(C\) contains the compatibility conditions and construction rules needed for the assembly;
- \(H\) is the target conclusion.

This notation is only a schema. A real proof must state all quantifiers, domains, hypotheses, and inference steps.

## 3. Independence and non-circularity

A trunk is independent of the target \(H\) when its justification does not assume \(H\), use an equivalent reformulation of \(H\) as an unproved premise, or rely on a result whose proof already depends on \(H\).

Independence does not mean that trunks have no mathematical relationships to one another. It means their validity is established without borrowing the target conclusion.

A trunk may be a known theorem with substantial prerequisites. Its prerequisites must be exposed sufficiently to establish that it is applicable in the target setting.

## 4. Compatibility audit

For every trunk, record:

1. exact statement;
2. domain and quantified objects;
3. hypotheses and boundary conditions;
4. proof or authoritative proof reference;
5. definitions and notation;
6. transformations required to apply it;
7. limitations and known counterexamples;
8. whether it depends on the target or on another selected trunk.

Before assembly, verify that the output of one result satisfies the input conditions of the next. Similar notation is not sufficient evidence of compatibility.

## 5. Assembly versus trunks

Keep separate:

- **Trunk:** an independently justified result.
- **Construction:** an object or representation introduced for the target proof.
- **Connector:** a valid identity or inference that transfers information between representations.
- **Compatibility condition:** a requirement that makes a trunk applicable.
- **Assembly:** the ordered use of trunks, constructions, and connectors.
- **Target:** the conclusion derived by the complete argument.

A construction may be the decisive creative step. It should not be mislabeled as an already established trunk unless it has an independent statement and proof.

## 6. Removal and substitution tests

For each trunk \(P_i\):

- remove it and identify the exact inference that becomes unavailable;
- check whether another selected trunk makes it redundant;
- search for a replacement result with independently justified content;
- determine whether the replacement changes the mathematical mechanism or merely renames/rephrases it.

A removal test is diagnostic, not a proof of minimality. A trunk is logically necessary only relative to the chosen proof architecture and available alternatives.

## 7. Classification of outcomes

- **RECONSTRUCTION:** known target and known proof reorganized into explicit trunks.
- **NEW_ASSEMBLY:** known trunks are connected through a demonstrably distinct arrangement or representation.
- **NEW_DERIVATION:** a valid derivation is obtained that is not merely a transcription of the selected reference proof; novelty still requires literature review.
- **NEW_RESULT_CANDIDATE:** the target conclusion itself appears not to be established in the relevant literature; this label requires independent verification and expert review.
- **FAILED_ASSEMBLY:** a compatibility condition, inference, or required guarantee fails.
- **INCONCLUSIVE:** available evidence does not settle the classification.

Do not infer mathematical novelty from an unfamiliar arrangement. Literature review and expert scrutiny are separate obligations.

## 8. Required record

Each Da Vinci Bridge case should include:

- target statement and scope;
- trunk register with proofs and sources;
- constructions and connectors;
- complete assembled derivation;
- compatibility and circularity audit;
- removal and substitution tests;
- counterexamples and failed attempts;
- classification and unresolved questions.

## 9. Guiding statement

A trunk is not a task pending. It is a result that already stands on its own. The research lies in discovering whether independently established results can be assembled, under valid compatibility conditions, into a conclusion that none supplies alone.

**The bridge is the assembly, not the inventory.**
