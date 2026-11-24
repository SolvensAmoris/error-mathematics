# DB-002 — Modular Segment Bridge

**Status:** RECONSTRUCTION; main proof verified. Alternative-mechanism search open.  
**Target:** In every sequence of \(n\geq1\) integers, some nonempty consecutive segment has sum divisible by \(n\).

## 1. Exact statement

For every integer \(n\geq1\) and every sequence \(a_1,\ldots,a_n\in\mathbb Z\), there exist indices \(1\leq r\leq s\leq n\) such that

\[
n\mid\sum_{k=r}^{s}a_k.
\]

The sequence has exactly \(n\) terms in this formulation. A sequence with more than \(n\) terms also satisfies the conclusion by applying the theorem to any chosen block of its first \(n\) terms. The statement is not true for arbitrary shorter sequences.

## 2. Trunks and connectors

### P1 — Finite counting / pigeonhole principle

If more objects are assigned to fewer categories, at least two objects occupy the same category.

### P2 — Congruence and divisibility

For integers \(x,y,n\), with \(n\geq1\),

\[
x\equiv y\pmod n\quad\Longleftrightarrow\quad n\mid(x-y).
\]

### P3 — Prefix-sum difference identity

Define

\[
S_0=0,\qquad S_j=\sum_{k=1}^{j}a_k.
\]

For \(0\leq i<j\leq n\),

\[
S_j-S_i=\sum_{k=i+1}^{j}a_k.
\]

This is a connector between the accumulated representation and the original sequence. It is an identity, not an existence principle.

## 3. Assembly A: split cases

Consider \(S_1,\ldots,S_n\) modulo \(n\).

- If some \(S_j\equiv0\pmod n\), the prefix \(a_1,\ldots,a_j\) is a required segment.
- Otherwise all \(n\) residues lie among the \(n-1\) nonzero residue classes. By P1, two coincide: \(S_i\equiv S_j\pmod n\) for some \(1\leq i<j\leq n\).
- By P2 and P3, \(n\mid S_j-S_i=\sum_{k=i+1}^{j}a_k\). Since \(i<j\), this segment is nonempty.

## 4. Assembly B: include the initial sum

Consider \(S_0,S_1,\ldots,S_n\). There are \(n+1\) values and only \(n\) residue classes modulo \(n\). Therefore two have the same residue, so there are \(0\leq i<j\leq n\) with \(S_i\equiv S_j\pmod n\). P2 and P3 give the required nonempty segment.

Assembly B is more compact. It does not eliminate the pigeonhole principle; it packages the zero-residue and repeated-nonzero-residue cases into one count.

## 5. Dependency clarification

P2 and P3 play distinct roles but are not wholly unrelated in their mathematical foundations. Congruence is defined through divisibility of a difference, while P3 identifies that difference with a consecutive segment sum. Keep the roles distinct without claiming absolute logical independence.

## 6. Substitution audit

A proposed replacement for P1 must identify exactly what guarantees indices \(i<j\) with equal residues, under the applicable hypotheses.

Audit questions:

1. What does the candidate assert, and under which assumptions?
2. Does it guarantee a repeated residue among the relevant prefix sums?
3. Does the guarantee hold for every \(n\) and every integer sequence in scope?
4. Does it use finite counting directly or under another name?
5. If not, what independent structural property supplies the guarantee?
6. Does the resulting congruence still yield a nonempty segment through P2 and P3?

Classification:
- INVALID: does not guarantee the required pair or violates its hypotheses.
- REFORMULATION: same counting guarantee in different language.
- ALTERNATIVE ORGANIZATION: different proof layout, same underlying guarantee.
- GENUINE MECHANISM CANDIDATE: a separately proved property guarantees the pair without relying on the same finite-counting argument. This label is provisional until audited.

## 7. Candidate mechanisms examined

### Group language: \(\mathbb Z/n\mathbb Z\)

Prefix sums can be viewed as elements of the finite additive group \(\mathbb Z/n\mathbb Z\). If two prefix sums coincide, their difference is the identity element. However, guaranteeing a repeated element among \(n+1\) prefix sums in a group of order \(n\) is still the finite-counting argument. This is a useful algebraic organization, not an independent replacement.

### Difference cocycle

For \(D_{ij}=S_j-S_i\), where \(i<j<k\),

\[
D_{ij}+D_{jk}=D_{ik}.
\]

The identity is valid over the integers and after reduction modulo any positive modulus. It organizes and propagates relations but does not, by itself, force any \(D_{ij}\equiv0\pmod n\).

A weighted identity also considered was

\[
\sum_{0\leq i<j\leq n}D_{ij}
=\sum_{k=1}^{n}k(n+1-k)a_k.
\]

This identity is valid, but a sum of terms being divisible by \(n\) does not imply that one of its terms is divisible by \(n\).

### Reflection of intervals

For interval coordinates \(0\leq i<j\leq n\), define

\[
\rho(i,j)=(n-j,n-i).
\]

This is well-defined and satisfies \(\rho^2(i,j)=(i,j)\). It reflects the interval of terms \(a_{i+1},\ldots,a_j\) to \(a_{n-j+1},\ldots,a_{n-i}\). For arbitrary sequences, their sums need not agree. If the sequence is palindromic, the reflected intervals do have equal sums.

The involution alone does not guarantee a fixed interval or a zero residue.

### Induction on the modulus

The direct theorem for modulus \(m\) does not automatically imply the case \(m+1\), because the modulus changes. A proposed stronger induction statement must contain genuinely additional information and a valid transition; it cannot simply restate the target as its induction hypothesis.

## 8. Current result

**Main theorem:** proved by Assemblies A and B.  
**Alternative to finite counting:** not found.  
**Useful methodological result:** changing the representation can simplify an argument without changing its underlying existence mechanism.  
**Novel theorem claimed:** No.  
**Novel proof claimed:** No.

## 9. Open question

Can a separately established algebraic or structural property force two prefix sums to coincide modulo \(n\) for every length-\(n\) integer sequence, without depending on the same finite-counting argument? Any candidate must be proved and audited for hidden counting.
