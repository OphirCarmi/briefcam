import numpy as np


class Shape(object):
    def __init__(self, num_points: int, randomness: float, debug: bool):
        self._num_points = num_points
        self._randomness = randomness
        self._debug = debug
        self._dim = 0
        self._gt_data = None
        self._noisy_data = None

    def GeneratePoints(self):
        separator = int(self._num_points * 0.8)
        self._noisy_data = np.zeros(self._gt_data.shape)

        shuffeled_indices = list(range(self._num_points))
        np.random.shuffle(shuffeled_indices)

        # inliers
        self._noisy_data[:, :separator] = self._gt_data[:, shuffeled_indices[:separator]] + np.random.randn(self._dim,
                                                                                         separator) * self._randomness
        # outliers
        self._noisy_data[:, separator:] = self._gt_data[:, shuffeled_indices[separator:]] + np.random.randn(self._dim,
                                                                                         self._num_points - separator)

    def EstimateModel(self):
        pass

    def PlotEstimatedPoints(self) -> np.ndarray:
        pass

    def Test(self) -> float:
        pass

    def PlotTest(self):
        pass

    def Fit(self):
        pass

    def CalcError(self):
        pass
