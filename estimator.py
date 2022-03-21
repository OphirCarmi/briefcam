import numpy as np
import json

from Shapes import SHAPES


def main(input_path, output_path, debug):
    with open(input_path) as in_f:
        next(in_f)
        with open(output_path, "w") as out_f:
            out_f.write("[\n")
            k = 0
            for line in in_f:
                if line.startswith("]"):
                    break
                line = line.rstrip(",\n")
                shape_dict = json.loads(line)
                shape_name = shape_dict["name"]
                noisy_data = np.array([np.array(x) for x in shape_dict["noisy_data"]])
                if shape_name in SHAPES:
                    num_points = noisy_data.shape[1]
                    shape = SHAPES[shape_name](num_points, 0)
                    model = shape.EstimateModel(noisy_data)
                    if debug:
                        shape.PlotEstimatedPoints(noisy_data, model)
                    if k > 0:
                        out_f.write(",\n")
                    del shape_dict["params"]
                    del shape_dict["noisy_data"]

                    shape_dict["estimated_model"] = model.tolist()
                    shape_dict["num_points"] = num_points
                    json_str = json.dumps(shape_dict)
                    out_f.write(json_str)
                    k += 1
            out_f.write("\n]\n")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Estimate Model for shapes')
    parser.add_argument('input_path', type=str,
                        help='path to the output file of the generator')
    parser.add_argument('output_path', type=str,
                        help='path to the output file')
    parser.add_argument('--debug', action='store_true',
                        help='plot debug data')


    args = parser.parse_args()

    main(args.input_path, args.output_path, args.debug)
