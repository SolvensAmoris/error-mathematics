# DB-003 — Palindromic Segment Symmetry

**Status:** EXPLORATORY; one stronger conjecture refuted; one orbit consequence proved.  
**Research question:** What additional structure does a palindromic sequence contribute to the modular-segment theorem?

## 1. Scope and definitions

Fix \(n\geq1\) and a palindromic integer sequence

\[
a_k=a_{n+1-k}\qquad(1\leq k\leq n).
\]

Represent a nonempty consecutive segment by indices \((i,j)\), where \(0\leq i<j\leq n\), corresponding to terms \(a_{i+1},\ldots,a_j\). Its sum is

\[
D_{ij}=\sum_{k=i+1}^{j}a_k.
\]

Define reflection

\[
\rho(i,j)=(n-j,n-i).
\]

## 2. Reflection lemma

For every valid interval, \(\rho(i,j)\) is valid and \(\rho^2(i,j)=(i,j)\).

The reflected interval contains terms \(a_{n-j+1},\ldots,a_{n-i}\). Since the sequence is palindromic, termwise reflection gives

\[
D_{n-j,n-i}=D_{ij}.
\]

Therefore reflection preserves segment sums and, in particular, preserves the property \(n\mid D_{ij}\).

## 3. Fixed intervals

A segment is fixed by reflection exactly when

\[
(i,j)=(n-j,n-i),
\]

equivalently,

\[
i+j=n.
\]

These are precisely the intervals symmetric about the center of the sequence.

The involution partitions the set of intervals whose sums are divisible by \(n\) into:
- singleton orbits, which are centered intervals;
- two-element orbits, consisting of two distinct reflected intervals with equal sums.

This is an orbit decomposition. It does not by itself guarantee that a fixed interval exists.

## 4. A tempting stronger conjecture, refuted

**Conjecture C1:** Every palindromic sequence of length \(n\) contains a centered nonempty segment whose sum is divisible by \(n\).

Counterexample: take \(n=3\) and sequence \((1,2,1)\). The centered intervals are:
- the middle singleton, with sum \(2\);
- the full sequence, with sum \(4\).

Neither sum is divisible by \(3\). Thus C1 is false.

The general modular-segment theorem still holds: the two off-center segments \((1,2)\) and \((2,3)\) both have sum \(3\), and reflection exchanges them.

## 5. Corollary from DB-002

By DB-002, at least one interval has sum divisible by \(n\). In a palindromic sequence, its reflected interval also has sum divisible by \(n\).

Consequently:

- either at least one centered divisible interval exists;
- or there are at least two distinct divisible intervals, exchanged by reflection.

More precisely, if \(Q\) is the set of nonempty intervals whose sums are divisible by \(n\), then

\[
|Q|\equiv |\operatorname{Fix}(\rho|_Q)|\pmod2.
\]

This follows because every non-fixed orbit has exactly two elements.

This is a valid structural consequence, but it is derived from DB-002 plus the reflection lemma. It is not an independent proof of DB-002 and is not currently claimed as a new theorem.

## 6. Audit and status

- Index reflection is well-defined: VERIFIED.
- Reflection is an involution: VERIFIED.
- Palindromicity makes reflected interval sums equal: VERIFIED.
- A centered divisible interval always exists: REFUTED by \((1,2,1)\) modulo 3.
- At least one divisible interval exists: inherited from DB-002.
- If no centered divisible interval exists, at least two distinct reflected solutions exist: VERIFIED.
- Independent replacement for finite counting: NOT ESTABLISHED.

## 7. Next research questions

1. Can the orbit structure yield useful lower bounds on the number of divisible intervals under additional, explicit conditions?
2. Which restrictions on a palindrome force a centered divisible interval?
3. Can a condition weaker than full palindromicity preserve enough interval-sum symmetry for a useful result?
4. Can any such result be proved without merely importing DB-002's existence theorem?
5. Are the resulting statements already known? A literature review is required before any novelty claim.

## 8. Methodological classification

**Result:** a valid orbit consequence and a counterexample to C1.  
**Novel theorem claimed:** No.  
**Independent existence mechanism:** No.  
**Research status:** exploratory; continue only with precise conjectures and counterexample searches.
