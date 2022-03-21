import numpy as np

from Shape3D import Shape3D
from RANSAC_regressor import RANSAC_regressor


class Plane3D(Shape3D):
    def generate_points(self):
        end_points = np.random.rand(self._dim, 3)
        return self.generate_points_inner(end_points)

    def generate_points_inner(self, points):
        divisors = []
        for i in range(2, int(np.sqrt(self._num_points)) + 1):
            if self._num_points % i == 0:
                divisors.append([i, self._num_points // i])
        min = self._num_points
        argmin = -1
        for i, (div1, div2) in enumerate(divisors):
            diff = abs(div1 - div2)
            if diff < min:
                min = diff
                argmin = i
        t1 = np.linspace(0, 1, divisors[argmin][0])
        t2 = np.linspace(0, 1, divisors[argmin][1])
        tt1, tt2 = np.meshgrid(t1, t2)

        gt_x = points[0, 0] + tt1 * (points[0, 1] - points[0, 0]) + tt2 * (points[0, 2] - points[0, 0])
        gt_y = points[1, 0] + tt1 * (points[1, 1] - points[1, 0]) + tt2 * (points[1, 2] - points[1, 0])
        gt_z = points[2, 0] + tt1 * (points[2, 1] - points[2, 0]) + tt2 * (points[2, 2] - points[2, 0])
        self._gt_data = np.vstack([gt_x.flatten(), gt_y.flatten(), gt_z.flatten()])
        super().generate_points()

        return points, self._noisy_data

    def estimate_model(self, noisy_data : np.array):
        self._RANSAC_regressor = RANSAC_regressor(3, self.fit, self.calc_error, self._num_points / 20)
        return self._RANSAC_regressor.Run(noisy_data)