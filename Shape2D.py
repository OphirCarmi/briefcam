import matplotlib.pyplot as plt
import numpy as np

from Shape import Shape


class Shape2D(Shape):
    def __init__(self, num_points: int, randomness: float):
        super().__init__(num_points, randomness)
        self._dim = 2
        self._gt_data = np.zeros((num_points, self._dim))
        self._noisy_data = np.zeros((num_points, self._dim))

    def GeneratePoints(self):
        super().GeneratePoints()

    def PlotGeneratedPoints(self):
        plt.figure()
        plt.plot(self._noisy_data[0, :], self._noisy_data[1, :], ".")
        plt.plot(self._gt_data[0, :], self._gt_data[1, :], ".")
        plt.title("generator")
        plt.legend(["noisy_data", "ground_truth"])
        plt.show()

    def PlotEstimatedPoints(self, noisy_data: np.ndarray, model: np.ndarray):
        plt.figure()
        plt.plot(noisy_data[0, :], noisy_data[1, :], ".")
        plt.plot(model[0, :], model[1, :], ".")
        plt.title("estimator")
        plt.legend(["noisy_data", "estimated_model"])
        plt.show()

    def EstimateModel(self, noisy_data : np.array):
        pass

    def Test(self) -> float:
        pass
