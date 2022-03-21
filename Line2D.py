import numpy as np

from Shape2D import Shape2D
from RANSAC_regressor import RANSAC_regressor


class Line2D(Shape2D):
    def generate_points(self):
        end_points = np.random.rand(self._dim, 2)
        return self.generate_points_inner(end_points)

    def generate_points_inner(self, points):
        gt_x = np.linspace(points[0, 0], points[0, 1], self._num_points)
        gt_y = np.linspace(points[1, 0], points[1, 1], self._num_points)
        self._gt_data = np.vstack([gt_x, gt_y])
        super().generate_points()

        return points, self._noisy_data

    def estimate_model(self, noisy_data : np.array):
        self._RANSAC_regressor = RANSAC_regressor(2, self.fit, self.calc_error, self._num_points / 20)
        return self._RANSAC_regressor.Run(noisy_data)