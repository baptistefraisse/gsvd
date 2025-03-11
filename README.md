# **GSVD: Generalized Singular Value Decomposition**  

## **Description**  
This repository provides an implementation of the **Generalized Singular Value Decomposition (GSVD)**, a matrix factorization technique that extends the **Singular Value Decomposition (SVD)** to two matrices.  

Given two matrices $A \in \mathbb{R}^{m \times n}$ and $B \in \mathbb{R}^{p \times n}$, the GSVD decomposes them as:  

$$
A = U_1 S_1 X^{-1}, \quad B = U_2 S_2 X^{-1}
$$

where:  
- $U_1 \in \mathbb{R}^{m \times m}$ and $U_2 \in \mathbb{R}^{p \times p}$ are **unitary** matrices,  
- $S_1$ and $S_2$ are **diagonal** matrices containing the generalized singular values,  
- $X \in \mathbb{R}^{n \times n}$ is **non-singular**.  

The generalized singular values are defined as:  

$$
\gamma_i = \frac{\sigma_i(A)}{\sigma_i(B)}
$$

where $\sigma_i(A)$ and $\sigma_i(B)$ are the singular values of $A$ and $B$, respectively.  

---

## **Installation**  
Simply clone the repository:  
```bash
git clone git@github.com:baptistefraisse/gsvd.git
cd gsvd