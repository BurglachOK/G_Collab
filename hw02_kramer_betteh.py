# Напиши функцію для вирішення системи методом Крамера
import numpy as np

A = np.array(
    [[-1, 1, 2],
     [0, -1, -3],
     [4, -3, 2]]
    )
B = np.array(
   [[1, -4, 7]]
)


def solve_cramer(a, b, verbose=False):
    if a.shape[0] != a.shape[1] or a.shape[0] != b.shape[1]:
        return 'Invalid input dimensions'

    deltaall = np.linalg.det(a)
    if verbose:
        print(f'\ndeterminant delta\n')
        print(deltaall)

    results = np.array([])

    for n in range(a.shape[0]):
        delta_n = np.array(a, copy=True)
        delta_n[:, n] = b[0]
        det_n = np.linalg.det(delta_n)
        if verbose:
            print(f'\nDeterminant delta_{n}\n')
            print(det_n)

        results = np.append(results, det_n/deltaall)

    return results

    # deltax = np.array(a, copy=True)
    # deltax[:, 0] = b[0]
    # deltax = np.linalg.det(deltax)
    # if verbose:
    #     print(f'\ndeterminant delta x\n')
    #     print(deltax)
    #
    # deltay = np.array(a, copy=True)
    # deltay[:, 1] = b[0]
    # deltay = np.linalg.det(deltay)
    # if verbose:
    #     print(f'\ndeterminant delta y\n')
    #     print(deltay)
    #
    # deltaz = np.array(a, copy=True)
    # deltaz[:, 2] = b[0]
    # deltaz = np.linalg.det(deltaz)
    # if verbose:
    #     print(f'\ndeterminant delta z\n')
    #     print(deltaz)
    #
    # x = deltax / deltaall
    # y = deltay / deltaall
    # z = deltaz / deltaall
    # return np.array([x, y, z])


print(f"Вектор рішення: \r\n {solve_cramer(A, B, verbose=True)}")