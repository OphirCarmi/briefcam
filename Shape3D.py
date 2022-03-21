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

    def generate_points(self):
        super().generate_points()

    def generate_points_inner(self, points):
        pass

    def plot_generated_points(self):
        plt.figure()
        ax = plt.axes(projection="3d")
        ax.plot3D(self._noisy_data[0, :], self._noisy_data[1, :], self._noisy_data[2, :], ".")
        ax.plot3D(self._gt_data[0, :], self._gt_data[1, :], self._gt_data[2, :], ".")
        plt.title("generator - {}".format(self._shape_name))
        plt.legend(["noisy_data", "ground_truth"])
        plt.show()

    def plot_estimated_points(self, noisy_data: np.ndarray, model: np.ndarray):
        plt.figure()
        ax = plt.axes(projection="3d")
        ax.plot3D(noisy_data[0, :], noisy_data[1, :], noisy_data[2, :], ".")
        self.generate_points_inner(model)
        ax.plot3D(self._gt_data[0, :], self._gt_data[1, :], self._gt_data[2, :], ".")
        plt.title("estimator - {}".format(self._shape_name))
        plt.legend(["noisy_data", "estimated_model"])
        plt.show()

    def estimate_model(self, noisy_data : np.array):
        pass

    def plot_test(self, gt_model: np.array, estimated_model: np.array, noisy_data: np.array, distance: float):
        plt.figure()
        ax = plt.axes(projection="3d")
        ax.plot3D(noisy_data[0, :], noisy_data[1, :], noisy_data[2, :], ".")
        self.generate_points_inner(gt_model)
        ax.plot3D(self._gt_data[0, :], self._gt_data[1, :], self._gt_data[2, :], ".")
        self.generate_points_inner(estimated_model)
        ax.plot3D(self._gt_data[0, :], self._gt_data[1, :], self._gt_data[2, :], ".")
        plt.title("test - {} - distance = {}".format(self._shape_name, distance))
        plt.legend(["noisy_data", "gt_model", "estimated_model"])
        plt.show()
