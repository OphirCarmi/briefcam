import numpy as np

from Shape3D import Shape3D
from RANSAC_regressor import RANSAC_regressor


class Line3D(Shape3D):
    def GeneratePoints(self):
        end_points = np.random.rand(self._dim, 2)
        return self.GeneratePointsInner(end_points)

    def GeneratePointsInner(self, points):
        gt_x = np.linspace(points[0, 0], points[0, 1], self._num_points)
        gt_y = np.linspace(points[1, 0], points[1, 1], self._num_points)
        gt_z = np.linspace(points[2, 0], points[2, 1], self._num_points)
        self._gt_data = np.vstack([gt_x, gt_y, gt_z])
        super().GeneratePoints()

        return points, self._noisy_data

    def EstimateModel(self, noisy_data : np.array):
        self._RANSAC_regressor = RANSAC_regressor(2, self.Fit, self.CalcError, self._num_points / 20)
        return self._RANSAC_regressor.Run(noisy_data)