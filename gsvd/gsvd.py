""" Generalized Singular Value Decomposition """

# Librairies

import scipy.special
import numpy as np
import sys

# Function


def gsvd(a, b):
    """
    Generalized Singular Value Decomposition:
    A = U1*S1*X
    B = U2*S2*X
    with U1 and U2 unitaries

    """

    # Error messages

    if (
        (np.shape(a)[0] < 2)
        or (np.shape(a)[1] < 2)
        or (np.shape(b)[0] < 2)
        or (np.shape(b)[0] < 2)
    ):
        raise ValueError("Error: A and B must size > 1")

    if (np.shape(a)[0] < np.shape(a)[1]) or (np.shape(b)[0] < np.shape(b)[1]):
        raise ValueError("Error: A and B must have full column rank (m>n)")

    if np.shape(a)[1] != np.shape(b)[1]:
        raise ValueError("Error: A and B must have matching column ranks")

    # Decomposition steps

    q, r = np.linalg.qr(np.block([[a], [b]]))

    try:
        u_1, s_1, vq_1 = np.linalg.svd(q[: np.shape(a)[0]])
    except:
        raise ValueError("Error: A and B similarly singular")

    vq_1 = np.transpose(vq_1)
    s_1 = np.diag(s_1)
    s_2 = np.zeros((np.shape(a)[1], np.shape(a)[1]))

    for k in range(np.shape(a)[1]):

        if 1 - s_1[k, k] * s_1[k, k] > 0:
            s_2[k, k] = np.sqrt(1 - s_1[k, k] * s_1[k, k])

    try:
        u_2 = np.matmul(q[np.shape(a)[0] :], np.matmul(vq_1, scipy.linalg.inv(s_2)))
    except:
        raise ValueError("Error: A and B similarly singular")

    h = np.diag(
        np.diag(
            np.matmul(
                np.matmul(np.transpose(vq_1), r),
                np.transpose(np.matmul(np.transpose(vq_1), r)),
            )
        )
    )

    s_1 = np.matmul(s_1, scipy.linalg.fractional_matrix_power(h, 0.5))
    s_2 = np.matmul(s_2, scipy.linalg.fractional_matrix_power(h, 0.5))
    x = np.transpose(
        np.matmul(
            scipy.linalg.fractional_matrix_power(h, -0.5),
            np.matmul(np.transpose(vq_1), r),
        )
    )

    # Completion with zeros if necessary (size-matching)

    if u_1.shape[1] != s_1.shape[0]:

        if u_1.shape[1] > s_1.shape[0]:
            s_1 = np.pad(
                s_1,
                ((0, u_1.shape[1] - s_1.shape[0]), (0, 0)),
                mode="constant",
                constant_values=0,
            )
        else:
            u_1 = np.pad(
                u_1,
                ((0, 0), (0, s_1.shape[0] - u_1.shape[1])),
                mode="constant",
                constant_values=0,
            )

    if u_2.shape[1] != s_2.shape[0]:

        if u_2.shape[1] > s_2.shape[0]:
            s_2 = np.pad(
                s_2,
                ((0, u_2.shape[1] - s_2.shape[0]), (0, 0)),
                mode="constant",
                constant_values=0,
            )
        else:
            u_2 = np.pad(
                u_2,
                ((0, 0), (0, s_2.shape[0] - u_2.shape[1])),
                mode="constant",
                constant_values=0,
            )

    # GSVs

    gamma = []

    for k in range(np.shape(a)[1]):

        if s_2[k, k] == 0.0:
            gamma.append(0.0)
        else:
            gamma.append(s_1[k, k] / s_2[k, k])

    return {"U1": u_1, "U2": u_2, "S1": s_1, "S2": s_2, "X": x, "gamma": gamma}
