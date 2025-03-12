# **GSVD: Generalized Singular Value Decomposition**  

## **Description**  
This repository provides an implementation of the **Generalized Singular Value Decomposition (GSVD)**, a matrix factorization technique that extends the **Singular Value Decomposition (SVD)** to two matrices [1-3]. GSVD has many applications in physics and engineering, as it compares the spectra of two matrices in a common space [4].  

Given two matrices $A \in \mathbb{R}^{m \times n}$ and $B \in \mathbb{R}^{p \times n}$, the GSVD decomposes them as:  

$$
A = U_1 S_1 X^{T}, \quad B = U_2 S_2 X^{T}
$$

where:  
- $U_1 \in \mathbb{R}^{m \times m}$ and $U_2 \in \mathbb{R}^{p \times p}$ are **unitary** matrices,  
- $S_1$ and $S_2$ are **diagonal** matrices containing the generalized singular values,  
- $X \in \mathbb{R}^{n \times n}$ is **non-singular**.  

The generalized singular values (GSVs) are defined as:  

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
```
---

## **How to do a GSVD?**  
The gsvd function takes two matrices as inputs and returns a dictionary with the following keys : "U1", "U2", "S1", "S2", "X" and "gamma". 
Please read the example for more details.

---

## **References**  

[1] C. F. Van Loan, SIAM J. Numer. Anal. 13, 76 (1976)

[2] C. C. Paige et al., SIAM J. Numer. Anal. 18, 398 (1981)

[3] S. Friedland, SIAM J. Matrix Anal. Appl. 27, 434 (2005)

[4] K. A. Aiello et al., APL Bioeng. 2, 031909 (2018).