import numpy as np


class RANSAC_regressor:
    def __init__(self, n, get_model, calc_error, d, t=0.0002, k=100):
        self._k = k
        self._n = n
        self._t = t
        self._d = d
        self._get_model = get_model
        self._calc_error = calc_error

    def Run(self, data : np.ndarray):
        best_fit = None
        best_err = 1e30

        for iterations in range(self._k):
            indices = list(range(data.shape[1]))
            while True:
                maybe_inliers = np.random.choice(indices, self._n)
                # no duplicate
                if self._n == len(np.unique(maybe_inliers)):
                    break
            maybe_model = self._get_model(data[:, maybe_inliers])
            also_inliers = []

            for maybe_inlier in sorted(maybe_inliers)[::-1]:
                indices.remove(maybe_inlier)
            for also_inlier_ind in indices:
                # if point fits maybe_model with an error smaller than t
                point = np.expand_dims(data[:, also_inlier_ind], axis=1)
                err = self._calc_error(point, maybe_model)
                if err < self._t:
                    also_inliers.append(also_inlier_ind)

            maybe_inliers = maybe_inliers.tolist()
            # This implies that we may have found a good model now test how good it is.
            all_inliers = maybe_inliers + also_inliers
            len_inliers = len(all_inliers)
            this_err = sum([self._calc_error(np.expand_dims(data[:, x], axis=1), maybe_model) for x in all_inliers])
            this_err /= (len_inliers**2)
            if this_err < best_err:
                best_fit = maybe_model
                best_err = this_err

        return best_fit