import numpy as np

from Shape2D import Shape2D


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
        pass

    def Test(self) -> float:
        pass

    def Fit(self):
        pass

    def CalcError(self):
        pass
