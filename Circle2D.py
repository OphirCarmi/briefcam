import numpy as np

from Shape2D import Shape2D
from RANSAC_regressor import RANSAC_regressor


class Circle2D(Shape2D):
    def GeneratePoints(self):
        x_center, y_center, r = np.random.rand(self._dim + 1)
        angle = np.linspace(0, 2 * np.pi, self._num_points)
        gt_x = x_center + r * np.cos(angle)
        gt_y = y_center + r * np.sin(angle)
        self._gt_data = np.vstack([gt_x, gt_y])
        super().GeneratePoints()
        return np.array([x_center, y_center, r]), self._noisy_data

    def EstimateModel(self, noisy_data : np.array):
        self._RANSAC_regressor = RANSAC_regressor(3, self.Fit, self.CalcError, self._num_points / 10)
        return self._RANSAC_regressor.Run(noisy_data)

    def Test(self) -> float:
        pass

    def Fit(self, points : np.ndarray):
        pass

    def CalcError(self, point : np.ndarray, model : np.ndarray):
        pass
