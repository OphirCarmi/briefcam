import numpy as np

from Shape import Shape


class Shape2D(Shape):
    def __init__(self, num_points: int, randomness: float, debug: bool):
        super().__init__(num_points, randomness, debug)
        self._dim = 2
        self._gt_data = np.zeros((num_points, self._dim))
        self._noisy_data = np.zeros((num_points, self._dim))

    def GeneratePoints(self):
        pass

    def EstimateModel(self, noisy_data : np.array):
        pass

    def Test(self) -> float:
        pass
