import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

from Shape import Shape


class Shape3D(Shape):
    def __init__(self, num_points: int, randomness: float):
        super().__init__(num_points, randomness)
        self._dim = 3
        self._gt_data = np.zeros((num_points, self._dim))
        self._noisy_data = np.zeros((num_points, self._dim))

    def GeneratePoints(self):
        super().GeneratePoints()

    def GeneratePointsInner(self, points):
        pass

    def PlotGeneratedPoints(self):
        plt.figure()
        ax = plt.axes(projection="3d")
        ax.plot3D(self._noisy_data[0, :], self._noisy_data[1, :], self._noisy_data[2, :], ".")
        ax.plot3D(self._gt_data[0, :], self._gt_data[1, :], self._gt_data[2, :], ".")
        plt.title("generator")
        plt.legend(["noisy_data", "ground_truth"])
        plt.show()

    def PlotEstimatedPoints(self, noisy_data: np.ndarray, model: np.ndarray):
        plt.figure()
        ax = plt.axes(projection="3d")
        ax.plot3D(noisy_data[0, :], noisy_data[1, :], noisy_data[2, :], ".")
        self.GeneratePointsInner(model)
        ax.plot3D(self._gt_data[0, :], self._gt_data[1, :], self._gt_data[2, :], ".")
        plt.title("estimator")
        plt.legend(["noisy_data", "estimated_model"])
        plt.show()

    def EstimateModel(self, noisy_data : np.array):
        pass

    def PlotTest(self, gt_model: np.array, estimated_model: np.array, noisy_data: np.array, distance: float):
        plt.figure()
        ax = plt.axes(projection="3d")
        ax.plot3D(noisy_data[0, :], noisy_data[1, :], noisy_data[2, :], ".")
        self.GeneratePointsInner(gt_model)
        ax.plot3D(self._gt_data[0, :], self._gt_data[1, :], self._gt_data[2, :], ".")
        self.GeneratePointsInner(estimated_model)
        ax.plot3D(self._gt_data[0, :], self._gt_data[1, :], self._gt_data[2, :], ".")
        plt.title("test - distance = {}".format(distance))
        plt.legend(["noisy_data", "gt_model", "estimated_model"])
        plt.show()
