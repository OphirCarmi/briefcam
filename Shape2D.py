import matplotlib.pyplot as plt
import numpy as np

from Shape import Shape


class Shape2D(Shape):
    def __init__(self, num_points: int, randomness: float, debug: bool):
        super().__init__(num_points, randomness, debug)
        self._dim = 2
        self._gt_data = np.zeros((num_points, self._dim))
        self._noisy_data = np.zeros((num_points, self._dim))

    def GeneratePoints(self):
        super().GeneratePoints()

    def PlotGeneratedPoints(self):
        plt.figure()
        plt.plot(self._gt_data[0, :], self._gt_data[1, :], ".")
        plt.plot(self._noisy_data[0, :], self._noisy_data[1, :], ".")
        plt.show()

    def EstimateModel(self):
        pass

    def Test(self) -> float:
        pass

    def Fit(self):
        pass

    def CalcError(self):
        pass
