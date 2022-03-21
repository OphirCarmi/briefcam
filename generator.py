import json

from Shapes import SHAPES


def main(config_path, output_path, debug):
    with open(config_path) as f:
        config_data = json.load(f)
    num_points = config_data["num_points"]
    randomness = config_data["randomness"]
    shapes = []
    for shape, num in config_data["shapes"].items():
        for i in range(num):
            if shape in SHAPES:
                shapes.append((shape, SHAPES[shape](num_points, randomness)))

    with open(output_path, "w") as f:
        f.write("[\n")
        for i, (shape_name, shape_obj) in enumerate(shapes):
            shape_dict = dict()
            params, noisy_data = shape_obj.GeneratePoints()
            shape_dict["name"] = shape_name
            shape_dict["params"] = params.tolist()
            shape_dict["noisy_data"] = noisy_data.tolist()

            json_str = json.dumps(shape_dict)
            f.write(json_str)

            if i < len(shapes) - 1:
                f.write(",\n")
            else:
                f.write("\n")

            if debug:
                shape_obj.PlotGeneratedPoints()
        f.write("]\n")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Generate Points for shapes')
    parser.add_argument('config_path', type=str,
                        help='path to the config file')
    parser.add_argument('output_path', type=str,
                        help='path to the output file')
    parser.add_argument('--debug', action='store_true',
                        help='plot debug data')


    args = parser.parse_args()

    main(args.config_path, args.output_path, args.debug)
