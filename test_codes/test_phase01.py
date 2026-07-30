# class Vector:
#     def __init__(self, components):
#         self.components = list(components)
#         self.dim = len(self.components)

#     def __add__(self, other):
#         return Vector([a + b for a, b in zip(self.components, other.components)])

#     def __sub__(self, other):
#         return Vector([a - b for a, b in zip(self.components, other.components)])

#     def dot(self, other):
#         return sum(a * b for a, b in zip(self.components, other.components))

#     def magnitude(self):
#         return sum(x**2 for x in self.components) ** 0.5

#     def normalize(self):
#         mag = self.magnitude()
#         return Vector([x / mag for x in self.components])

#     def cosine_similarity(self, other):
#         return self.dot(other) / (self.magnitude() * other.magnitude())

#     def __repr__(self):
#         return f"Vector({self.components})"


# a = Vector([1, 2, 3])
# b = Vector([4, 5, 6])

# print(f"a + b = {a + b}")
# print(f"a · b = {a.dot(b)}")
# print(f"|a| = {a.magnitude():.4f}")
# print(f"cosine similarity = {a.cosine_similarity(b):.4f}")


# class Matrix:
#     def __init__(self, rows):
#         self.rows = [list(row) for row in rows]
#         self.shape = (len(self.rows), len(self.rows[0]))

#     def __matmul__(self, other):
#         if isinstance(other, Vector):
#             return Vector([
#                 sum(self.rows[i][j] * other.components[j] for j in range(self.shape[1]))
#                 for i in range(self.shape[0])
#             ])
#         rows = []
#         for i in range(self.shape[0]):
#             row = []
#             for j in range(other.shape[1]):
#                 row.append(sum(
#                     self.rows[i][k] * other.rows[k][j]
#                     for k in range(self.shape[1])
#                 ))
#             rows.append(row)
#         return Matrix(rows)

#     def transpose(self):
#         return Matrix([
#             [self.rows[j][i] for j in range(self.shape[0])]
#             for i in range(self.shape[1])
#         ])

#     def __repr__(self):
#         return f"Matrix({self.rows})"


# rotation_90 = Matrix([[0, -1], [1, 0]])
# point = Vector([3, 1])

# rotated = rotation_90 @ point
# print(f"Original: {point}")
# print(f"Rotated 90°: {rotated}")


# def is_linearly_independent(vectors):
#     n = len(vectors)
#     dim = len(vectors[0].components)
#     mat = Matrix([v.components[:] for v in vectors])
#     rows = [row[:] for row in mat.rows]
#     rank = 0
#     for col in range(dim):
#         pivot = None
#         for row in range(rank, len(rows)):
#             if abs(rows[row][col]) > 1e-10:
#                 pivot = row
#                 break
#         if pivot is None:
#             continue
#         rows[rank], rows[pivot] = rows[pivot], rows[rank]
#         scale = rows[rank][col]
#         rows[rank] = [x / scale for x in rows[rank]]
#         for row in range(len(rows)):
#             if row != rank and abs(rows[row][col]) > 1e-10:
#                 factor = rows[row][col]
#                 rows[row] = [rows[row][j] - factor * rows[rank][j] for j in range(dim)]
#         rank += 1
#     return rank == n


# def project(a, b):
#     scalar = a.dot(b) / b.dot(b)
#     return Vector([scalar * x for x in b.components])


# def gram_schmidt(vectors):
#     orthonormal = []
#     for v in vectors:
#         w = v
#         for u in orthonormal:
#             proj = project(w, u)
#             w = w - proj
#         if w.magnitude() < 1e-10:
#             continue
#         orthonormal.append(w.normalize())
#     return orthonormal


# v1 = Vector([1, 0, 0])
# v2 = Vector([1, 1, 0])
# v3 = Vector([1, 1, 1])
# basis = gram_schmidt([v1, v2, v3])
# for i, u in enumerate(basis):
#     print(f"u{i+1} = {u}")
#     print(f"  |u{i+1}| = {u.magnitude():.6f}")

# print(f"u1 · u2 = {basis[0].dot(basis[1]):.6f}")
# print(f"u1 · u3 = {basis[0].dot(basis[2]):.6f}")
# print(f"u2 · u3 = {basis[1].dot(basis[2]):.6f}")



# import numpy as np

# a = np.array([1, 2, 3], dtype=float)
# b = np.array([4, 5, 6], dtype=float)

# print(f"a + b = {a + b}")
# print(f"a · b = {np.dot(a, b)}")
# print(f"|a| = {np.linalg.norm(a):.4f}")
# print(f"cosine = {np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)):.4f}")

# W = np.random.randn(2, 3) * 0.1
# x = np.array([1.0, 0.5, -0.3])
# print(f"Wx = {W @ x}")


# import numpy as np

# A = np.array([[1, 2], [2, 4]])
# print(f"Rank: {np.linalg.matrix_rank(A)}")

# a = np.array([3, 4])
# b = np.array([1, 0])
# proj = (np.dot(a, b) / np.dot(b, b)) * b
# print(f"Projection of {a} onto {b}: {proj}")

# Q, R = np.linalg.qr(np.random.randn(3, 3))
# print(f"Q is orthogonal: {np.allclose(Q @ Q.T, np.eye(3))}")
# print(f"R is upper triangular: {np.allclose(R, np.triu(R))}")


# import torch

# x = torch.randn(3, requires_grad=True)
# y = torch.tensor([1.0, 0.0, 0.0])

# similarity = torch.dot(x, y)
# similarity.backward()

# print(f"x = {x.data}")
# print(f"y = {y.data}")
# print(f"dot product = {similarity.item():.4f}")
# print(f"d(dot)/dx = {x.grad}")


# import random
# import math

# # Create 5 random word-like vectors
# words = ["cat", "dog", "car", "apple", "music"]

# vectors = {}

# for word in words:
#     vectors[word] = [random.uniform(-1, 1) for _ in range(50)]


# def dot(a, b):
#     return sum(x * y for x, y in zip(a, b))


# def norm(v):
#     return math.sqrt(sum(x * x for x in v))


# def cosine_similarity(a, b):
#     return dot(a, b) / (norm(a) * norm(b))


# best_pair = None
# best_score = -1

# for i in range(len(words)):
#     for j in range(i + 1, len(words)):
#         w1 = words[i]
#         w2 = words[j]

#         score = cosine_similarity(vectors[w1], vectors[w2])

#         print(f"{w1:>6} vs {w2:<6} -> {score:.4f}")

#         if score > best_score:
#             best_score = score
#             best_pair = (w1, w2)

# print("\nMost similar pair:")
# print(best_pair, "score =", round(best_score, 4))



# import numpy as np

# words = ["cat", "dog", "car", "apple", "music"]

# vectors = {
#     word: np.random.randn(50)
#     for word in words
# }

# best_pair = None
# best_score = -1

# for i in range(len(words)):
#     for j in range(i + 1, len(words)):
#         w1, w2 = words[i], words[j]

#         a = vectors[w1]
#         b = vectors[w2]

#         score = np.dot(a, b) / (
#             np.linalg.norm(a) * np.linalg.norm(b)
#         )

#         print(f"{w1} vs {w2} -> {score:.4f}")

#         if score > best_score:
#             best_score = score
#             best_pair = (w1, w2)

# print("\nMost similar:", best_pair)
# print("Score:", best_score)


# class Vector:
#     def __init__(self, data):
#         self.data = list(data)
#         self.size = len(self.data)

#     def __repr__(self):
#         return f"Vector({self.data})"

#     def __add__(self, other):
#         return Vector([a + b for a, b in zip(self.data, other.data)])

#     def __sub__(self, other):
#         return Vector([a - b for a, b in zip(self.data, other.data)])

#     def __mul__(self, scalar):
#         return Vector([x * scalar for x in self.data])

#     def dot(self, other):
#         return sum(a * b for a, b in zip(self.data, other.data))

#     def magnitude(self):
#         return sum(x ** 2 for x in self.data) ** 0.5
    
# class Matrix:
#     def __init__(self, data):
#         self.data = [list(row) for row in data]
#         self.rows = len(self.data)
#         self.cols = len(self.data[0])
#         self.shape = (self.rows, self.cols)

#     def __repr__(self):
#         rows_str = "\n  ".join(str(row) for row in self.data)
#         return f"Matrix({self.shape}):\n  {rows_str}"

#     def __add__(self, other):
#         return Matrix([
#             [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
#             for i in range(self.rows)
#         ])

#     def __sub__(self, other):
#         return Matrix([
#             [self.data[i][j] - other.data[i][j] for j in range(self.cols)]
#             for i in range(self.rows)
#         ])

#     def scalar_multiply(self, scalar):
#         return Matrix([
#             [self.data[i][j] * scalar for j in range(self.cols)]
#             for i in range(self.rows)
#         ])

#     def element_wise_multiply(self, other):
#         return Matrix([
#             [self.data[i][j] * other.data[i][j] for j in range(self.cols)]
#             for i in range(self.rows)
#         ])

#     def matmul(self, other):
#         return Matrix([
#             [
#                 sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
#                 for j in range(other.cols)
#             ]
#             for i in range(self.rows)
#         ])

#     def transpose(self):
#         return Matrix([
#             [self.data[j][i] for j in range(self.rows)]
#             for i in range(self.cols)
#         ])

#     def determinant(self):
#         if self.shape == (1, 1):
#             return self.data[0][0]
#         if self.shape == (2, 2):
#             return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
#         det = 0
#         for j in range(self.cols):
#             minor = Matrix([
#                 [self.data[i][k] for k in range(self.cols) if k != j]
#                 for i in range(1, self.rows)
#             ])
#             det += ((-1) ** j) * self.data[0][j] * minor.determinant()
#         return det

#     def inverse_2x2(self):
#         det = self.determinant()
#         if det == 0:
#             raise ValueError("Matrix is singular, no inverse exists")
#         return Matrix([
#             [self.data[1][1] / det, -self.data[0][1] / det],
#             [-self.data[1][0] / det, self.data[0][0] / det]
#         ])

#     @staticmethod
#     def identity(n):
#         return Matrix([
#             [1 if i == j else 0 for j in range(n)]
#             for i in range(n)
#         ])
    
# A = Matrix([[1, 2], [3, 4]])
# B = Matrix([[5, 6], [7, 8]])

# print("A + B =", (A + B).data)
# print("A @ B =", A.matmul(B).data)
# print("A^T =", A.transpose().data)
# print("det(A) =", A.determinant())
# print("A^-1 =", A.inverse_2x2().data)

# I = Matrix.identity(2)
# print("A @ A^-1 =", A.matmul(A.inverse_2x2()).data)



# import random

# inputs = Matrix([[0.5], [0.8], [0.2]])
# weights = Matrix([
#     [random.uniform(-1, 1) for _ in range(3)]
#     for _ in range(2)
# ])
# bias = Matrix([[0.1], [0.1]])

# def relu_matrix(m):
#     return Matrix([[max(0, val) for val in row] for row in m.data])

# pre_activation = weights.matmul(inputs) + bias
# output = relu_matrix(pre_activation)

# print(f"Input shape: {inputs.shape}")
# print(f"Weight shape: {weights.shape}")
# print(f"Output shape: {output.shape}")
# print(f"Output: {output.data}")



# import numpy as np

# A = np.array([[1, 2], [3, 4]])
# B = np.array([[5, 6], [7, 8]])

# print("A + B =\n", A + B)
# print("A * B (element-wise) =\n", A * B)
# print("A @ B (matrix multiply) =\n", A @ B)
# print("A^T =\n", A.T)
# print("det(A) =", np.linalg.det(A))
# print("A^-1 =\n", np.linalg.inv(A))
# print("I =\n", np.eye(2))

# inputs = np.random.randn(3, 1)
# weights = np.random.randn(2, 3)
# bias = np.array([[0.1], [0.1]])
# output = np.maximum(0, weights @ inputs + bias)

# print(f"\nNeural network layer: {weights.shape} @ {inputs.shape} = {output.shape}")
# print(f"Output:\n{output}")




import math

# def rotation_2d(theta):
#     c, s = math.cos(theta), math.sin(theta)
#     return [[c, -s], [s, c]]

# def scaling_2d(sx, sy):
#     return [[sx, 0], [0, sy]]

# def shearing_2d(kx, ky):
#     return [[1, kx], [ky, 1]]

# def reflection_x():
#     return [[1, 0], [0, -1]]

# def reflection_y():
#     return [[-1, 0], [0, 1]]

# def mat_vec_mul(matrix, vector):
#     return [
#         sum(matrix[i][j] * vector[j] for j in range(len(vector)))
#         for i in range(len(matrix))
#     ]

# def mat_mul(a, b):
#     rows_a, cols_b = len(a), len(b[0])
#     cols_a = len(a[0])
#     return [
#         [sum(a[i][k] * b[k][j] for k in range(cols_a)) for j in range(cols_b)]
#         for i in range(rows_a)
#     ]

# point = [1.0, 0.0]
# angle = math.pi / 4

# rotated = mat_vec_mul(rotation_2d(angle), point)
# print(f"Rotate (1,0) by 45 deg: ({rotated[0]:.4f}, {rotated[1]:.4f})")

# scaled = mat_vec_mul(scaling_2d(2, 3), [1.0, 1.0])
# print(f"Scale (1,1) by (2,3): ({scaled[0]:.1f}, {scaled[1]:.1f})")

# sheared = mat_vec_mul(shearing_2d(1, 0), [1.0, 1.0])
# print(f"Shear (1,1) kx=1: ({sheared[0]:.1f}, {sheared[1]:.1f})")

# reflected = mat_vec_mul(reflection_y(), [2.0, 1.0])
# print(f"Reflect (2,1) across y: ({reflected[0]:.1f}, {reflected[1]:.1f})")


# R = rotation_2d(math.pi / 2)
# S = scaling_2d(2, 0.5)

# rotate_then_scale = mat_mul(S, R)
# scale_then_rotate = mat_mul(R, S)

# point = [1.0, 0.0]
# result1 = mat_vec_mul(rotate_then_scale, point)
# result2 = mat_vec_mul(scale_then_rotate, point)

# print(f"Rotate 90 then scale: ({result1[0]:.2f}, {result1[1]:.2f})")
# print(f"Scale then rotate 90: ({result2[0]:.2f}, {result2[1]:.2f})")
# print(f"Same? {result1 == result2}")


# def eigenvalues_2x2(matrix):
#     a, b = matrix[0]
#     c, d = matrix[1]
#     trace = a + d
#     det = a * d - b * c
#     discriminant = trace ** 2 - 4 * det
#     if discriminant < 0:
#         real = trace / 2
#         imag = (-discriminant) ** 0.5 / 2
#         return (complex(real, imag), complex(real, -imag))
#     sqrt_disc = discriminant ** 0.5
#     return ((trace + sqrt_disc) / 2, (trace - sqrt_disc) / 2)

# def eigenvector_2x2(matrix, eigenvalue):
#     a, b = matrix[0]
#     c, d = matrix[1]
#     if abs(b) > 1e-10:
#         v = [b, eigenvalue - a]
#     elif abs(c) > 1e-10:
#         v = [eigenvalue - d, c]
#     else:
#         if abs(a - eigenvalue) < 1e-10:
#             v = [1, 0]
#         else:
#             v = [0, 1]
#     mag = (v[0] ** 2 + v[1] ** 2) ** 0.5
#     return [v[0] / mag, v[1] / mag]

# A = [[2, 1], [1, 2]]
# vals = eigenvalues_2x2(A)
# print(f"Matrix: {A}")
# print(f"Eigenvalues: {vals[0]:.4f}, {vals[1]:.4f}")

# for val in vals:
#     vec = eigenvector_2x2(A, val)
#     result = mat_vec_mul(A, vec)
#     scaled = [val * vec[0], val * vec[1]]
#     print(f"  lambda={val:.1f}, v={[round(x,4) for x in vec]}")
#     print(f"    A@v = {[round(x,4) for x in result]}")
#     print(f"    l*v = {[round(x,4) for x in scaled]}")



# def det_2x2(matrix):
#     return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

# print(f"det(rotation 45) = {det_2x2(rotation_2d(math.pi/4)):.4f}")
# print(f"det(scale 2,3)   = {det_2x2(scaling_2d(2, 3)):.1f}")
# print(f"det(shear kx=1)  = {det_2x2(shearing_2d(1, 0)):.1f}")
# print(f"det(reflect y)   = {det_2x2(reflection_y()):.1f}")

# singular = [[1, 2], [2, 4]]
# print(f"det(singular)     = {det_2x2(singular):.1f}")
# print("Singular: columns are proportional, space collapses to a line.")


# import numpy as np

# theta = np.pi / 4
# R = np.array([[np.cos(theta), -np.sin(theta)],
#               [np.sin(theta),  np.cos(theta)]])

# point = np.array([1.0, 0.0])
# print(f"Rotate (1,0) by 45 deg: {R @ point}")

# S = np.diag([2.0, 3.0])
# composed = S @ R
# print(f"Scale(2,3) after Rotate(45): {composed @ point}")

# A = np.array([[2, 1], [1, 2]], dtype=float)
# eigenvalues, eigenvectors = np.linalg.eig(A)
# print(f"\nEigenvalues: {eigenvalues}")
# print(f"Eigenvectors (columns):\n{eigenvectors}")

# for i in range(len(eigenvalues)):
#     v = eigenvectors[:, i]
#     lam = eigenvalues[i]
#     print(f"  A @ v{i} = {A @ v}, lambda * v{i} = {lam * v}")

# print(f"\ndet(R) = {np.linalg.det(R):.4f}")
# print(f"det(S) = {np.linalg.det(S):.1f}")

# B = np.array([[3, 1], [0, 2]], dtype=float)
# vals, vecs = np.linalg.eig(B)
# D = np.diag(vals)
# V = vecs
# reconstructed = V @ D @ np.linalg.inv(V)
# print(f"\nEigendecomposition A = V @ D @ V^-1:")
# print(f"Original:\n{B}")
# print(f"Reconstructed:\n{reconstructed}")

# def rotation_3d_z(theta):
#     c, s = np.cos(theta), np.sin(theta)
#     return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])

# def rotation_3d_x(theta):
#     c, s = np.cos(theta), np.sin(theta)
#     return np.array([[1, 0, 0], [0, c, -s], [0, s, c]])

# point_3d = np.array([1.0, 0.0, 0.0])
# rotated_z = rotation_3d_z(np.pi / 2) @ point_3d
# rotated_x = rotation_3d_x(np.pi / 2) @ point_3d

# print(f"\n3D point: {point_3d}")
# print(f"Rotate 90 around z: {np.round(rotated_z, 4)}")
# print(f"Rotate 90 around x: {np.round(rotated_x, 4)}")




# import numpy as np

# # Unit square corners
# square = np.array([
#     [0, 1, 1, 0],
#     [0, 0, 1, 1]
# ])

# print("Original square:")
# print(square)

# # ---------------------------------------------------
# # 1. Rotation
# # ---------------------------------------------------

# theta = np.pi / 4  # 45 degrees

# R = np.array([
#     [np.cos(theta), -np.sin(theta)],
#     [np.sin(theta),  np.cos(theta)]
# ])

# rotated = R @ square

# print("\nRotated square:")
# print(rotated)

# # ---------------------------------------------------
# # 2. Scaling
# # ---------------------------------------------------

# S = np.array([
#     [2, 0],
#     [0, 0.5]
# ])

# scaled = S @ square

# print("\nScaled square:")
# print(scaled)

# # ---------------------------------------------------
# # 3. Shearing
# # ---------------------------------------------------

# H = np.array([
#     [1, 1],
#     [0, 1]
# ])

# sheared = H @ square

# print("\nSheared square:")
# print(sheared)

# # ---------------------------------------------------
# # Verify rotation preserves distances
# # ---------------------------------------------------

# def dist(a, b):
#     return np.linalg.norm(a - b)

# original_d = dist(square[:, 0], square[:, 1])
# rotated_d = dist(rotated[:, 0], rotated[:, 1])

# print("\nDistance check:")
# print("Original edge length:", original_d)
# print("Rotated edge length :", rotated_d)
# print("Preserved?", np.allclose(original_d, rotated_d))



# import math

# A = [[4, 2],
#      [1, 3]]

# # coefficients of λ² - 7λ + 10
# a = 1
# b = -7
# c = 10

# # quadratic formula
# disc = b*b - 4*a*c

# lambda1 = (-b + math.sqrt(disc)) / (2*a)
# lambda2 = (-b - math.sqrt(disc)) / (2*a)

# print("Eigenvalues:")
# print(lambda1)
# print(lambda2)


# import numpy as np

# A = np.array([[4, 2],
#               [1, 3]])

# values, vectors = np.linalg.eig(A)

# print("Eigenvalues:")
# print(values)

# print("\nEigenvectors:")
# print(vectors)


# import numpy as np
# import math

# # ----------------------------
# # 1. Create 8 circle points
# # ----------------------------

# angles = np.linspace(0, 2*np.pi, 8, endpoint=False)

# points = np.array([
#     [math.cos(a), math.sin(a)]
#     for a in angles
# ])

# print("Original points:\n")
# for p in points:
#     print(np.round(p, 4))


# # ----------------------------
# # 2. Rotation matrix (30 deg)
# # ----------------------------

# theta = math.radians(30)

# R = np.array([
#     [math.cos(theta), -math.sin(theta)],
#     [math.sin(theta),  math.cos(theta)]
# ])

# # ----------------------------
# # 3. Scaling matrix
# # ----------------------------

# S = np.array([
#     [1.5, 0],
#     [0, 0.8]
# ])

# # ----------------------------
# # 4. Shear matrix
# # ----------------------------

# kx = 0.3

# H = np.array([
#     [1, kx],
#     [0, 1]
# ])

# # ----------------------------
# # 5. Compose transformations
# # ----------------------------

# T = H @ S @ R

# print("\nComposed matrix T:\n")
# print(np.round(T, 4))


# # ----------------------------
# # 6. Apply transformation
# # ----------------------------

# transformed = np.array([
#     T @ p for p in points
# ])

# print("\nTransformed points:\n")
# for p in transformed:
#     print(np.round(p, 4))


# # ----------------------------
# # 7. Determinants
# # ----------------------------

# det_R = np.linalg.det(R)
# det_S = np.linalg.det(S)
# det_H = np.linalg.det(H)

# det_product = det_R * det_S * det_H
# det_T = np.linalg.det(T)

# print("\nDeterminants:")
# print(f"det(R) = {det_R:.4f}")
# print(f"det(S) = {det_S:.4f}")
# print(f"det(H) = {det_H:.4f}")

# print("\nProduct of determinants:")
# print(f"det(R)*det(S)*det(H) = {det_product:.4f}")

# print("\nDeterminant of composed matrix:")
# print(f"det(T) = {det_T:.4f}")



# def numerical_derivative(f, x, h=1e-7):
#     return (f(x + h) - f(x - h)) / (2 * h)

# def f(x):
#     return x ** 2

# for x in [-2, -1, 0, 1, 2]:
#     numerical = numerical_derivative(f, x)
#     analytical = 2 * x
#     print(f"x={x:2d}  f'(x) numerical={numerical:.6f}  analytical={analytical:.1f}")


# def numerical_gradient(f, point, h=1e-7):
#     gradient = []
#     for i in range(len(point)):
#         point_plus = list(point)
#         point_minus = list(point)
#         point_plus[i] += h
#         point_minus[i] -= h
#         partial = (f(point_plus) - f(point_minus)) / (2 * h)
#         gradient.append(partial)
#     return gradient

# def f_multi(point):
#     x, y = point
#     return x**2 + 3*x*y + y**2

# grad = numerical_gradient(f_multi, [1.0, 2.0])
# print(f"Numerical gradient at (1,2): {[f'{g:.4f}' for g in grad]}")
# print(f"Analytical gradient at (1,2): [2*1+3*2, 3*1+2*2] = [{2*1+3*2}, {3*1+2*2}]")


# x = 5.0
# lr = 0.1
# for step in range(20):
#     grad = 2 * x
#     x = x - lr * grad
#     print(f"step {step:2d}  x={x:8.4f}  f(x)={x**2:10.6f}")


# def f_2d(point):
#     x, y = point
#     return x**2 + y**2

# point = [4.0, 3.0]
# lr = 0.1
# for step in range(30):
#     grad = numerical_gradient(f_2d, point)
#     point = [p - lr * g for p, g in zip(point, grad)]
#     loss = f_2d(point)
#     if step % 5 == 0 or step == 29:
#         print(f"step {step:2d}  point=({point[0]:7.4f}, {point[1]:7.4f})  f={loss:.6f}")


# import math

# test_functions = [
#     ("x^2",      lambda x: x**2,          lambda x: 2*x),
#     ("x^3",      lambda x: x**3,          lambda x: 3*x**2),
#     ("sin(x)",   lambda x: math.sin(x),   lambda x: math.cos(x)),
#     ("e^x",      lambda x: math.exp(x),   lambda x: math.exp(x)),
#     ("1/x",      lambda x: 1/x,           lambda x: -1/x**2),
# ]

# x = 2.0
# print(f"{'Function':<12} {'Numerical':>12} {'Analytical':>12} {'Error':>12}")
# print("-" * 50)
# for name, f, df in test_functions:
#     num = numerical_derivative(f, x)
#     ana = df(x)
#     err = abs(num - ana)
#     print(f"{name:<12} {num:12.6f} {ana:12.6f} {err:12.2e}")

    
# def hessian_2d(f, x, y, h=1e-5):
#     fxx = (f(x + h, y) - 2 * f(x, y) + f(x - h, y)) / (h ** 2)
#     fyy = (f(x, y + h) - 2 * f(x, y) + f(x, y - h)) / (h ** 2)
#     fxy = (f(x + h, y + h) - f(x + h, y - h) - f(x - h, y + h) + f(x - h, y - h)) / (4 * h ** 2)
#     return [[fxx, fxy], [fxy, fyy]]

# def saddle(x, y):
#     return x ** 2 - y ** 2

# def bowl(x, y):
#     return x ** 2 + y ** 2

# H_saddle = hessian_2d(saddle, 0.0, 0.0)
# H_bowl = hessian_2d(bowl, 0.0, 0.0)
# print(f"Saddle Hessian: {H_saddle}")  # [[2, 0], [0, -2]] -- mixed signs
# print(f"Bowl Hessian:   {H_bowl}")    # [[2, 0], [0, 2]]  -- both positive


# import math

# def taylor_approx(f, f_prime, f_double_prime, x0, h, order=2):
#     result = f(x0)
#     if order >= 1:
#         result += f_prime(x0) * h
#     if order >= 2:
#         result += 0.5 * f_double_prime(x0) * h ** 2
#     return result

# x0 = 0.0
# for h in [0.1, 0.5, 1.0, 2.0]:
#     true_val = math.sin(h)
#     t1 = taylor_approx(math.sin, math.cos, lambda x: -math.sin(x), x0, h, order=1)
#     t2 = taylor_approx(math.sin, math.cos, lambda x: -math.sin(x), x0, h, order=2)
#     print(f"h={h:.1f}  sin(h)={true_val:.4f}  order1={t1:.4f}  order2={t2:.4f}")

# import random

# random.seed(42)

# w = random.gauss(0, 1)
# b = random.gauss(0, 1)
# lr = 0.01

# xs = [1.0, 2.0, 3.0, 4.0, 5.0]
# ys = [3.0, 5.0, 7.0, 9.0, 11.0]

# for epoch in range(200):
#     total_loss = 0
#     dw = 0
#     db = 0
#     for x, y in zip(xs, ys):
#         pred = w * x + b
#         error = pred - y
#         total_loss += error ** 2
#         dw += 2 * error * x
#         db += 2 * error
#     dw /= len(xs)
#     db /= len(xs)
#     total_loss /= len(xs)
#     w -= lr * dw
#     b -= lr * db
#     if epoch % 40 == 0 or epoch == 199:
#         print(f"epoch {epoch:3d}  w={w:.4f}  b={b:.4f}  loss={total_loss:.6f}")

# print(f"\nLearned: y = {w:.2f}x + {b:.2f}")
# print(f"Actual:  y = 2x + 1")


# import numpy as np

# x = np.array([1, 2, 3, 4, 5], dtype=float)
# y = np.array([3, 5, 7, 9, 11], dtype=float)

# w, b = np.random.randn(), np.random.randn()
# lr = 0.01

# for epoch in range(200):
#     pred = w * x + b
#     error = pred - y
#     loss = np.mean(error ** 2)
#     dw = np.mean(2 * error * x)
#     db = np.mean(2 * error)
#     w -= lr * dw
#     b -= lr * db

# print(f"Learned: y = {w:.2f}x + {b:.2f}")



# def numerical_derivative(f, x, h=1e-5):
#     return (f(x + h) - f(x - h)) / (2 * h)


# def numerical_second_derivative(f, x, h=1e-5):
#     return (
#         numerical_derivative(f, x + h, h)
#         - numerical_derivative(f, x - h, h)
#     ) / (2 * h)


# # Test function
# def f(x):
#     return x ** 3


# x = 2

# second_deriv = numerical_second_derivative(f, x)

# print("Approx second derivative:", second_deriv)
# print("Expected:", 12)



# def f(x, y):
#     return (x - 3)**2 + (y + 1)**2


# def grad_x(x):
#     return 2 * (x - 3)


# def grad_y(y):
#     return 2 * (y + 1)


# # Start point
# x = 0.0
# y = 0.0

# lr = 0.1

# for step in range(50):

#     dx = grad_x(x)
#     dy = grad_y(y)

#     x = x - lr * dx
#     y = y - lr * dy

#     loss = f(x, y)

#     print(
#         f"step {step:2d} | "
#         f"x={x:.4f}  y={y:.4f}  loss={loss:.6f}"
#     )

# print("\nFinal point:")
# print(f"x = {x:.4f}, y = {y:.4f}")


# def f(x):
#     return x**4 - 3*x**2


# def grad(x):
#     return 4*x**3 - 6*x


# # -----------------------------
# # Standard Gradient Descent
# # -----------------------------

# x = 2.0
# lr = 0.01

# print("STANDARD GRADIENT DESCENT\n")

# for step in range(50):

#     g = grad(x)

#     x = x - lr * g

#     print(
#         f"step {step:2d} | "
#         f"x={x:.6f} | "
#         f"f(x)={f(x):.6f}"
#     )


# # -----------------------------
# # Momentum Gradient Descent
# # -----------------------------

# x = 2.0
# v = 0.0

# lr = 0.01
# beta = 0.9

# print("\nMOMENTUM GRADIENT DESCENT\n")

# for step in range(50):

#     g = grad(x)

#     v = beta * v - lr * g

#     x = x + v

#     print(
#         f"step {step:2d} | "
#         f"x={x:.6f} | "
#         f"v={v:.6f} | "
#         f"f(x)={f(x):.6f}"
#     )


# import random
# import matplotlib.pyplot as plt

# def sample_exponential(lam, n=1):
#     """
#     Generate samples from an Exponential(lambda) distribution
#     using inverse transform sampling.
#     """
#     if lam <= 0:
#         raise ValueError("lambda must be positive")

#     samples = []
#     for _ in range(n):
#         u = random.random()

#         # Avoid log(0)
#         while u == 0:
#             u = random.random()

#         x = -math.log(u) / lam
#         samples.append(x)

#     return samples

# print("\n--- Exponential Distribution (Inverse Transform Sampling) ---")

# lam = 2.0
# samples = sample_exponential(lam, 10000)

# sample_mean = sum(samples) / len(samples)

# print(f"Lambda = {lam}")
# print(f"Expected mean = {1/lam:.4f}")
# print(f"Sample mean   = {sample_mean:.4f}")

# fig, ax = plt.subplots(figsize=(8,5))

# lam = 2.0
# samples = sample_exponential(lam, 10000)

# # Histogram
# ax.hist(
#     samples,
#     bins=50,
#     density=True,
#     alpha=0.6,
#     label="Sampled Histogram"
# )

# # True PDF
# xs = [i * 0.01 for i in range(800)]
# ys = [lam * math.exp(-lam * x) for x in xs]

# ax.plot(xs, ys, linewidth=2, label="True PDF")

# ax.set_title("Exponential Distribution via Inverse Transform Sampling")
# ax.set_xlabel("x")
# ax.set_ylabel("Density")
# ax.legend()

# plt.tight_layout()
# plt.savefig("exponential_inverse_sampling.png", dpi=150)
# plt.close()

# print("Saved: exponential_inverse_sampling.png")

# import numpy as np

# # Loaded die A
# pA = np.array([0.05, 0.10, 0.15, 0.20, 0.20, 0.30])

# # Loaded die B
# pB = np.array([0.30, 0.25, 0.20, 0.10, 0.10, 0.05])

# # Joint distribution
# joint = np.outer(pA, pB)

# print("Joint Distribution:")
# print(joint)

# # Marginals
# marginal_A = joint.sum(axis=1)
# marginal_B = joint.sum(axis=0)

# print("\nMarginal Distribution of A:")
# print(marginal_A)

# print("\nMarginal Distribution of B:")
# print(marginal_B)

# # Independence test
# print("\nIndependent?")
# print(np.allclose(joint, np.outer(marginal_A, marginal_B)))

# import numpy as np
# from scipy.special import softmax

# logits = np.array([2.0, 0.5, -1.0, 3.0, 0.1])

# probs = softmax(logits)

# loss = -np.log(probs[3])

# print("Softmax probabilities:")
# print(probs)

# print("Cross-Entropy Loss:", loss)

# import torch
# import torch.nn as nn

# # Batch size = 1
# logits = torch.tensor([[2.0, 0.5, -1.0, 3.0, 0.1]])
# target = torch.tensor([3])

# criterion = nn.CrossEntropyLoss()

# loss = criterion(logits, target)

# print(loss.item())


# import math

# def sequence_probability(sequence, log_probs):
#     """
#     Returns:
#         - most likely sequence
#         - total log probability
#         - equivalent raw probability
#     """
#     if len(sequence) != len(log_probs):
#         raise ValueError("Sequence and log_probs must have the same length.")

#     total_log_prob = sum(log_probs)
#     raw_prob = math.exp(total_log_prob)

#     return sequence, total_log_prob, raw_prob


# # ----------------------------------------------------
# # Test with a sentence of 50 words
# # Each word has probability 0.01
# # ----------------------------------------------------

# sentence = [f"word{i+1}" for i in range(50)]

# # log(p) for each word
# log_probs = [math.log(0.01)] * 50

# sequence, total_log_prob, raw_prob = sequence_probability(sentence, log_probs)

# print("Most likely sequence:")
# print(" ".join(sequence))

# print("\nTotal log probability:")
# print(total_log_prob)

# print("\nEquivalent raw probability:")
# print(raw_prob)

# # Verify against direct multiplication
# direct_prob = 0.01 ** 50

# print("\nDirect multiplication:")
# print(direct_prob)

# print("\nMatch:",
#       math.isclose(raw_prob, direct_prob, rel_tol=1e-12))


import numpy as np
import matplotlib.pyplot as plt

##############################################################
# Rosenbrock Function
##############################################################

def rosenbrock(x):
    return (1 - x[0])**2 + 100 * (x[1] - x[0]**2)**2


def rosenbrock_grad(x):
    dx = -2 * (1 - x[0]) - 400 * x[0] * (x[1] - x[0]**2)
    dy = 200 * (x[1] - x[0]**2)
    return np.array([dx, dy])


##############################################################
# Saddle Function
##############################################################

def saddle(x):
    return x[0]**2 - x[1]**2


def saddle_grad(x):
    return np.array([2 * x[0], -2 * x[1]])


##############################################################
# Gradient Descent
##############################################################

class GradientDescent:

    def __init__(self, lr=0.001, decay=False):
        self.lr0 = lr
        self.decay = decay

    def optimize(self, grad_fn, loss_fn, x0, steps):

        x = x0.copy()

        history = []
        losses = []

        for step in range(steps):

            lr = self.lr0

            if self.decay:
                lr = self.lr0 * (0.999 ** step)

            grad = grad_fn(x)

            x = x - lr * grad

            history.append(x.copy())
            losses.append(loss_fn(x))

        return x, np.array(history), np.array(losses)


##############################################################
# Momentum GD
##############################################################

class MomentumGD:

    def __init__(self, lr=0.001, momentum=0.9):

        self.lr = lr
        self.momentum = momentum

    def optimize(self, grad_fn, loss_fn, x0, steps):

        x = x.copy() if False else x0.copy()
        velocity = np.zeros_like(x)

        history = []
        losses = []

        for _ in range(steps):

            grad = grad_fn(x)

            velocity = self.momentum * velocity - self.lr * grad

            x = x + velocity

            history.append(x.copy())
            losses.append(loss_fn(x))

        return x, np.array(history), np.array(losses)


##############################################################
# Adam
##############################################################

class Adam:

    def __init__(self, lr=0.05):

        self.lr = lr
        self.beta1 = 0.9
        self.beta2 = 0.999
        self.eps = 1e-8

    def optimize(self, grad_fn, loss_fn, x0, steps):

        x = x0.copy()

        m = np.zeros_like(x)
        v = np.zeros_like(x)

        history = []
        losses = []

        for t in range(1, steps + 1):

            grad = grad_fn(x)

            m = self.beta1 * m + (1 - self.beta1) * grad
            v = self.beta2 * v + (1 - self.beta2) * grad**2

            m_hat = m / (1 - self.beta1**t)
            v_hat = v / (1 - self.beta2**t)

            x = x - self.lr * m_hat / (np.sqrt(v_hat) + self.eps)

            history.append(x.copy())
            losses.append(loss_fn(x))

        return x, np.array(history), np.array(losses)


##############################################################
# Experiment 1
##############################################################

print("=" * 60)
print("Learning Rate Sweep")
print("=" * 60)

learning_rates = [0.0001, 0.0005, 0.001, 0.005, 0.01]

best_lr = None

for lr in learning_rates:

    gd = GradientDescent(lr=lr)

    x, history, losses = gd.optimize(
        rosenbrock_grad,
        rosenbrock,
        np.array([-1.2, 1.0]),
        5000
    )

    print(f"lr={lr:<8} final loss={losses[-1]:.6f}")

    if np.isfinite(losses[-1]) and losses[-1] < 0.01:
        best_lr = lr

print("\nLargest learning rate that converged:", best_lr)


##############################################################
# Experiment 2
##############################################################

print("\n" + "=" * 60)
print("Momentum Comparison")
print("=" * 60)

momenta = [0.0, 0.5, 0.9, 0.99]

best_loss = float("inf")
best_momentum = None

plt.figure(figsize=(8, 5))

for m in momenta:

    optimizer = MomentumGD(
        lr=0.001,
        momentum=m
    )

    x, history, losses = optimizer.optimize(
        rosenbrock_grad,
        rosenbrock,
        np.array([-1.2, 1.0]),
        5000
    )

    print(f"Momentum={m:<4} Final Loss={losses[-1]:.6f}")

    if losses[-1] < best_loss:
        best_loss = losses[-1]
        best_momentum = m

    plt.plot(losses, label=f"m={m}")

print("\nFastest / Best Momentum =", best_momentum)

plt.yscale("log")
plt.xlabel("Iteration")
plt.ylabel("Loss")
plt.title("Momentum Comparison")
plt.legend()
plt.grid(True)

##############################################################
# Experiment 3
##############################################################

print("\n" + "=" * 60)
print("Saddle Point Escape")
print("=" * 60)

x0 = np.array([0.01, 0.01])

methods = {
    "Gradient Descent": GradientDescent(lr=0.1),
    "Momentum": MomentumGD(lr=0.1, momentum=0.9),
    "Adam": Adam(lr=0.05)
}

plt.figure(figsize=(8, 5))

for name, optimizer in methods.items():

    x, history, losses = optimizer.optimize(
        saddle_grad,
        saddle,
        x0,
        200
    )

    print(f"{name:18s} Final Point={x}  Final Loss={losses[-1]:.6f}")

    plt.plot(losses, label=name)

plt.xlabel("Iteration")
plt.ylabel("Loss")
plt.title("Saddle Point Escape")
plt.legend()
plt.grid(True)

##############################################################
# Experiment 4
##############################################################

print("\n" + "=" * 60)
print("Learning Rate Decay")
print("=" * 60)

plt.figure(figsize=(8, 5))

for decay in [False, True]:

    optimizer = GradientDescent(
        lr=0.001,
        decay=decay
    )

    x, history, losses = optimizer.optimize(
        rosenbrock_grad,
        rosenbrock,
        np.array([-1.2, 1.0]),
        5000
    )

    print(f"Decay={decay:<5} Final Loss={losses[-1]:.6f}")

    plt.plot(losses, label=f"Decay={decay}")

plt.yscale("log")
plt.xlabel("Iteration")
plt.ylabel("Loss")
plt.title("Learning Rate Decay")
plt.legend()
plt.grid(True)

##############################################################
# Show All Graphs
##############################################################

plt.show()