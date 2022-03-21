import numpy as np
import json

from Shapes import SHAPES


def main(gt_input_path, est_input_path, output_path, debug):
    with open(output_path, "w") as out_f:
        out_f.write("[\n")
        k = 0
        with open(gt_input_path) as gt_f:
            with open(est_input_path) as est_f:
                next(gt_f)
                next(est_f)
                for line_gt, line_est in zip(gt_f, est_f):
                    line_gt = line_gt.rstrip(",\n")
                    line_est = line_est.rstrip(",\n")
                    if line_gt.startswith("]"):
                        break
                    shape_gt = json.loads(line_gt)
                    shape_est = json.loads(line_est)
                    shape_name = shape_gt["name"]
                    estimated_model = np.array([np.array(x) for x in shape_est["estimated_model"]])
                    gt_params = np.array([np.array(x) for x in shape_gt["params"]])
                    noisy_data = np.array([np.array(x) for x in shape_gt["noisy_data"]])
                    num_points = shape_est["num_points"]
                    if shape_name in SHAPES:
                        shape = SHAPES[shape_name](num_points, 0)
                        distance = shape.test(gt_params, estimated_model)
                        shape_test = dict()
                        shape_test["name"] = shape_name
                        shape_test["distance"] = distance
                        json_str = json.dumps(shape_test)
                        if k > 0:
                            out_f.write(",\n")
                        out_f.write(json_str)
                        k += 1
                        if debug:
                            shape.plot_test(gt_params, estimated_model, noisy_data, distance)

        out_f.write("\n]\n")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Estimate Model for shapes')
    parser.add_argument('gt_input_path', type=str,
                        help='path to the output file of the generator')
    parser.add_argument('est_input_path', type=str,
                        help='path to the output file of the estimator')
    parser.add_argument('output_path', type=str,
                        help='path to the output file')
    parser.add_argument('--debug', action='store_true',
                        help='plot debug data')


    args = parser.parse_args()

    main(args.gt_input_path, args.est_input_path, args.output_file, args.debug)
