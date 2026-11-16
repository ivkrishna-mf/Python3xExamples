"""@ operator — Python 3.5+ (PEP 465). Pure-Python Matrix class, NumPy optional."""
MIN_VERSION = (3, 5)


class Matrix:
    def __init__(self, rows):
        self.rows = [list(r) for r in rows]

    def __matmul__(self, other):
        if isinstance(other, Vector):
            return Vector(sum(a * b for a, b in zip(row, other.v)) for row in self.rows)
        cols = list(zip(*other.rows))
        return Matrix([[sum(a * b for a, b in zip(r, c)) for c in cols] for r in self.rows])

    def __imatmul__(self, other):
        self.rows = (self @ other).rows
        return self

    def __eq__(self, other):
        return self.rows == other.rows

    def __repr__(self):
        return f"Matrix({self.rows})"

    @staticmethod
    def identity(n):
        return Matrix([[int(i == j) for j in range(n)] for i in range(n)])


class Vector:
    def __init__(self, v):
        self.v = list(v)

    def __matmul__(self, other):          # dot product
        return sum(a * b for a, b in zip(self.v, other.v))

    def __rmatmul__(self, other):         # list @ Vector
        return Vector(other) @ self

    def __repr__(self):
        return f"Vector({self.v})"


A = Matrix([[1, 2], [3, 4]])
B = Matrix([[5, 6], [7, 8]])


def example_01_matrix_product():
    print(A @ B)


def example_02_identity_is_neutral():
    print(A @ Matrix.identity(2) == A)


def example_03_matrix_vector():
    print(A @ Vector([1, 1]))


def example_04_dot_product():
    print(Vector([1, 2, 3]) @ Vector([4, 5, 6]))


def example_05_rmatmul():
    print([1, 0, 0] @ Vector([9, 8, 7]))


def example_06_in_place_matmul():
    M = Matrix([[1, 2], [3, 4]])
    M @= Matrix.identity(2)
    print(M)


def example_07_not_commutative():
    print(A @ B == B @ A)


def example_08_rotation_composition():
    import math
    def rot(deg):
        r = math.radians(deg)
        return Matrix([[round(math.cos(r), 6), round(-math.sin(r), 6)],
                       [round(math.sin(r), 6), round(math.cos(r), 6)]])
    print((rot(45) @ rot(45)).rows, "≈ rot(90)")


def example_09_operator_module():
    import operator
    print(operator.matmul(A, B))


def example_10_numpy_if_available():
    try:
        import numpy as np
        X = np.array([[1, 2], [3, 4]])
        print(X @ X, X * X, sep="\n")      # @ = matrix, * = element-wise
    except ImportError:
        print("NumPy not installed – with NumPy, X @ W is the standard matrix product")


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
