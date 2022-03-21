import numpy as np

from Shape2D import Shape2D
from RANSAC_regressor import RANSAC_regressor


def determinant(A):
    a = A[0, 0]
    b = A[0, 1]
    c = A[0, 2]
    d = A[1, 0]
    e = A[1, 1]
    f = A[1, 2]
    g = A[2, 0]
    h = A[2, 1]
    i = A[2, 2]
    return a * e * i + b * f * g + c * d * h - c * e * g - b * d * i - a * f * h


class Circle2D(Shape2D):
    def __init__(self, num_points: int, randomness: float):
        super().__init__(num_points, randomness)
        self._shape_name = "Circle2D"

    def generate_points(self):
        points = np.random.rand(self._dim, 3)
        return self.generate_points_inner(points)

    def generate_points_inner(self, points : np.ndarray):
        x1, x2, x3 = points[0, :]
        y1, y2, y3 = points[1, :]
        M12 = determinant(np.array([[x1**2 + y1**2, y1, 1], [x2**2 + y2**2, y2, 1], [x3**2 + y3**2, y3, 1]]))
        M11 = determinant(
            np.array([[x1, y1, 1], [x2, y2, 1], [x3, y3, 1]]))
        M13 = determinant(
            np.array([[x1**2 + y1**2, x1, 1], [x2**2 + y2**2, x2, 1], [x3**2 + y3**2, x3, 1]]))
        M14 = determinant(
            np.array([[x1 ** 2 + y1 ** 2, x1, y1], [x2 ** 2 + y2 ** 2, x2, y2], [x3 ** 2 + y3 ** 2, x3, y3]]))

        x0 = 0.5 * M12 / M11
        y0 = -0.5 * M13 / M11
        r = np.sqrt(x0 **2 + y0 ** 2 + M14/M11)

        angle = np.linspace(0, 2 * np.pi, self._num_points)
        gt_x = x0 + r * np.cos(angle)
        gt_y = y0 + r * np.sin(angle)
        self._gt_data = np.vstack([gt_x, gt_y])
        super().generate_points()
        return points, self._noisy_data

    def estimate_model(self, noisy_data : np.array):
        self._RANSAC_regressor = RANSAC_regressor(3, self.fit, self.calc_error, self._num_points / 10)
        return self._RANSAC_regressor.Run(noisy_data)

