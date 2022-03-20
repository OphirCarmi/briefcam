import numpy as np

from Shape2D import Shape2D


class Line2D(Shape2D):
    def GeneratePoints(self):
        end_points = np.random.rand(self._dim, self._dim)
        gt_x = np.linspace(end_points[0, 0], end_points[1, 0], self._num_points)
        gt_y = np.linspace(end_points[0, 1], end_points[1, 1], self._num_points)
        self._gt_data = np.vstack([gt_x, gt_y])
        super().GeneratePoints()

    def EstimateModel(self):
        pass

    def Test(self) -> float:
        pass

    def Fit(self):
        pass

    def CalcError(self):
        pass
