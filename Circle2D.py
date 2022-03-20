import numpy as np

from Shape2D import Shape2D


class Circle2D(Shape2D):
    def GeneratePoints(self):
        x_center, y_center, r = np.random.rand(self._dim + 1)
        angle = np.linspace(0, 2 * np.pi, self._num_points)
        gt_x = x_center + r * np.cos(angle)
        gt_y = y_center + r * np.sin(angle)
        self._gt_data = np.vstack([gt_x, gt_y])
        self._noisy_data = self._gt_data + np.random.randn(self._dim, self._num_points) * self._randomness

    def EstimateModel(self):
        pass

    def Test(self) -> float:
        pass

    def Fit(self):
        pass

    def CalcError(self):
        pass
