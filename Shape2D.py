import matplotlib.pyplot as plt
import numpy as np

from Shape import Shape


class Shape2D(Shape):
    def __init__(self, num_points: int, randomness: float):
        super().__init__(num_points, randomness)
        self._dim = 2
        self._gt_data = np.zeros((num_points, self._dim))
        self._noisy_data = np.zeros((num_points, self._dim))

    def generate_points(self):
        super().generate_points()

    def generate_points_inner(self, points):
        pass

    def plot_generated_points(self):
        plt.figure()
        plt.plot(self._noisy_data[0, :], self._noisy_data[1, :], ".")
        plt.plot(self._gt_data[0, :], self._gt_data[1, :], ".")
        plt.title("generator")
        plt.legend(["noisy_data", "ground_truth"])
        plt.show()

    def plot_estimated_points(self, noisy_data: np.ndarray, model: np.ndarray):
        plt.figure()
        plt.plot(noisy_data[0, :], noisy_data[1, :], ".")
        self.generate_points_inner(model)
        plt.plot(self._gt_data[0, :], self._gt_data[1, :], ".")
        plt.title("estimator")
        plt.legend(["noisy_data", "estimated_model"])
        plt.show()

    def estimate_model(self, noisy_data : np.array):
        pass

    def plot_test(self, gt_model: np.array, estimated_model: np.array, noisy_data: np.array, distance: float):
        plt.figure()
        plt.plot(noisy_data[0, :], noisy_data[1, :], ".")
        self.generate_points_inner(gt_model)
        plt.plot(self._gt_data[0, :], self._gt_data[1, :], ".")
        self.generate_points_inner(estimated_model)
        plt.plot(self._gt_data[0, :], self._gt_data[1, :], ".")
        plt.title("test - distance = {}".format(distance))
        plt.legend(["noisy_data", "gt_model", "estimated_model"])
        plt.show()
