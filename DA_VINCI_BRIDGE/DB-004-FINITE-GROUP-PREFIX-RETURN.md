# DB-004 — Finite-Group Prefix Return

**Status:** RECONSTRUCTION / STRUCTURAL GENERALIZATION; proof verified.  
**Research question:** Does the modular consecutive-segment theorem depend essentially on integer arithmetic, or does it arise from a more general finite-group structure?

## 1. Target theorem

Let \(G\) be a finite group with identity element \(e\) and order \(|G|=m\geq1\). For every ordered sequence

\[
g_1,g_2,\ldots,g_m\in G,
\]

there exist indices \(0\leq i<j\leq m\) such that

\[
g_{i+1}g_{i+2}\cdots g_j=e.
\]

The order of the factors is the order in the original sequence. No commutativity assumption is made.

Equivalently: every sequence of \(m\) elements of a group of order \(m\) contains a nonempty consecutive block whose ordered product is the identity.

## 2. Trunk register

### P1 — Finite counting

A list of \(m+1\) elements drawn from a set of size \(m\) contains a repeated element.

This is the finite pigeonhole principle.

### P2 — Group inverse and cancellation

For every \(x\in G\), there exists \(x^{-1}\in G\) with

\[
x^{-1}x=e.
\]

In particular, left multiplication by \(x^{-1}\) cancels a common left factor. This holds in every group, including non-abelian groups.

### C1 — Ordered prefix-product decomposition

Define

\[
P_0=e,\qquad P_k=g_1g_2\cdots g_k\quad(1\leq k\leq m).
\]

Associativity gives, for \(0\leq i<j\leq m\),

\[
P_j=P_i(g_{i+1}g_{i+2}\cdots g_j).
\]

This is an identity connecting prefix products to a consecutive block. It does not itself guarantee that a suitable pair of prefixes exists.

## 3. Assembly

There are \(m+1\) prefix products

\[
P_0,P_1,\ldots,P_m
\]

and only \(m\) elements in \(G\). By P1, there exist \(0\leq i<j\leq m\) such that

\[
P_i=P_j.
\]

By C1,

\[
P_i=P_i(g_{i+1}\cdots g_j).
\]

Left-multiply both sides by \(P_i^{-1}\), using P2:

\[
e=g_{i+1}g_{i+2}\cdots g_j.
\]

Since \(i<j\), the block is nonempty. This proves the theorem.

The proof uses associativity and inverses, but never commutes or reorders factors. It is therefore valid for non-abelian groups.

## 4. Relation to DB-002

Take the additive cyclic group

\[
G=\mathbb Z/n\mathbb Z,
\]

whose identity is \(0\), and let \(g_k\) be the residue class of \(a_k\). Group multiplication is then written as addition. The prefix products become prefix sums, and the identity block becomes

\[
a_{i+1}+\cdots+a_j\equiv0\pmod n.
\]

Thus DB-002 is the cyclic-group instance of DB-004. DB-004 extends the same prefix-return mechanism to arbitrary finite groups, including non-abelian ones.

This is a genuine increase in mathematical scope, but not a new theorem claim: the finite-group result and its prefix-product proof are already present in the literature cited below.

## 5. Why non-commutativity is not an obstacle

The key equation is

\[
P_j=P_iB,
\qquad B=g_{i+1}\cdots g_j.
\]

From \(P_i=P_j\), we obtain \(P_i=P_iB\). Multiplication on the left by \(P_i^{-1}\) gives \(e=B\).

No step changes the order of the factors in \(B\). Commutativity is unnecessary.

## 6. Boundary test: remove inverses

The group hypothesis cannot simply be weakened to an arbitrary finite monoid.

Let

\[
M=\{e,z\}
\]

with identity \(e\) and absorbing element \(z\), so

\[
ez=ze=z,\qquad z^2=z.
\]

This is a monoid of size two, but \(z\) has no inverse. Consider the length-two sequence \((z,z)\). Its nonempty consecutive block products are

\[
z,\quad z,\quad z^2=z.
\]

None equals \(e\). Therefore the theorem fails for finite monoids in general.

The prefix products are \(P_0=e,P_1=z,P_2=z\). The repeated prefix products do not yield an identity block because the cancellation step is unavailable. This isolates the role of the group-inverse trunk.

## 7. Sharpness of the length bound

The bound \(m\) cannot be lowered uniformly for all groups of order \(m\).

In the cyclic group \(C_m\), choose a generator \(g\) and take the sequence of \(m-1\) copies

\[
(g,g,\ldots,g).
\]

Every nonempty consecutive block of length \(r\), with \(1\leq r\leq m-1\), has product \(g^r\neq e\). Hence \(m-1\) terms do not suffice in general, while the theorem proves that \(m\) terms do.

For \(m=1\), the statement is immediate because the unique group element is the identity.

## 8. Removal and substitution audit

- **Remove P1:** no repeated prefix product is guaranteed by the recorded argument.
- **Remove P2:** a repeated prefix product need not yield an identity block in a structure without inverses; the two-element monoid above is a counterexample.
- **Remove C1:** there is no explicit bridge from equality of prefixes to the product of the intervening block.
- **Replace the group by a finite monoid:** invalid in general, as shown by \((z,z)\).

These are local audits of this proof architecture, not claims of absolute logical independence among all group axioms.

## 9. Literature and novelty audit

A direct antecedent appears in Section 2, “Subsequence products representing the identity in a group,” of:

W. R. Alford, Andrew Granville, and Carl Pomerance, *There are infinitely many Carmichael numbers*, available at:

https://dms.umontreal.ca/~andrew/PDF/carmichael.pdf

That section states the finite-group result for a group of order \(m\) and gives the prefix-product collision argument. Its displayed proof obtains a consecutive block, even though it uses the broader word “subsequence.”

Accordingly:

- **Known result:** YES.
- **Proof mechanism:** prefix products + finite counting + group cancellation.
- **Non-abelian scope:** YES; the argument does not use commutativity.
- **Independent replacement for counting:** NO.
- **New theorem claimed:** NO.
- **Classification:** STRUCTURAL GENERALIZATION / RECONSTRUCTION.

The useful methodological outcome is the separation of two forces: finite counting creates a repeated state; group inverses convert that repetition into an identity block. The monoid counterexample shows that the second force is substantive, not decorative.

## 10. Next questions

1. For a finite monoid, which additional cancellation or regularity assumptions are sufficient to recover a prefix-return theorem?
2. Can the group-inverse requirement be weakened to a condition on the particular prefix products generated by the sequence?
3. For groups of order \(m\), can stronger conclusions be obtained when the sequence has more than \(m\) terms, such as multiple disjoint identity blocks or constraints on their lengths?
4. Which of these questions are already settled in semigroup theory or zero-sum theory?

Any continuation must distinguish consecutive blocks from arbitrary subsequences and preserve factor order in the non-abelian setting.
