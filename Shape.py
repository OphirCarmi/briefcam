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
        pass

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
