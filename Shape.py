import numpy as np


class Shape(object):
    def __init__(self, num_points: int, randomness: float):
        self._num_points = num_points
        self._randomness = randomness
        self._dim = 0
        self._gt_data = None
        self._noisy_data = None
        self._RANSAC_regressor = None

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

    def EstimateModel(self, noisy_data : np.array):
        pass

    def PlotEstimatedPoints(self, noisy_data: np.ndarray, model: np.ndarray):
        pass

    def Test(self, gt_model : np.array, estimated_model : np.array) -> float:
        gt_points = self.Fit(gt_model)
        est_points = self.Fit(estimated_model)
        sum_err = 0
        for ind in range(self._num_points):
            sum_err += self.CalcError(np.expand_dims(est_points[:, ind], axis=1), gt_points)
        return sum_err

    def PlotTest(self, gt_model: np.array, estimated_model: np.array, noisy_data: np.array, distance: float):
        pass

    def Fit(self, points : np.ndarray):
        self.GeneratePointsInner(points)
        return self._gt_data

    def CalcError(self, point: np.ndarray, model_points : np.ndarray):
        point_repeated = np.repeat(point, self._num_points, axis=1)
        err_sqr = (point_repeated - model_points)**2
        amin_err = np.amin(np.sum(err_sqr, axis=0))
        return amin_err

