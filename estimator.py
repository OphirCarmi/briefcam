import numpy as np
import json

from Shapes import SHAPES


def main(input_path, output_path, debug):
    with open(input_path) as f:
        data = json.load(f)
        for shape_dict in data:
            shape_name = shape_dict["name"]
            noisy_data = np.array([np.array(x) for x in shape_dict["noisy_data"]])
            if shape_name in SHAPES:
                shape = SHAPES[shape_name](noisy_data.shape[1], 0)
                model = shape.EstimateModel(noisy_data)
                if model is None:
                    print("couldn't estimate model")
                    continue
                if debug:
                    shape.PlotEstimatedPoints(noisy_data, model)


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
