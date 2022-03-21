import numpy as np

from Shape3D import Shape3D
from RANSAC_regressor import RANSAC_regressor


class Line3D(Shape3D):
    def __init__(self, num_points: int, randomness: float):
        super().__init__(num_points, randomness)
        self._shape_name = "Lane3D"

    def generate_points(self):
        end_points = np.random.rand(self._dim, 2)
        return self.generate_points_inner(end_points)

    def generate_points_inner(self, points):
        gt_x = np.linspace(points[0, 0], points[0, 1], self._num_points)
        gt_y = np.linspace(points[1, 0], points[1, 1], self._num_points)
        gt_z = np.linspace(points[2, 0], points[2, 1], self._num_points)
        self._gt_data = np.vstack([gt_x, gt_y, gt_z])
        super().generate_points()

        return points, self._noisy_data

    def estimate_model(self, noisy_data : np.array):
        self._RANSAC_regressor = RANSAC_regressor(2, self.fit, self.calc_error, self._num_points / 20)
        return self._RANSAC_regressor.Run(noisy_data)