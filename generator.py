import json

from Shape import Shape
from Line2D import Line2D
from Circle2D import Circle2D

SHAPES = {
    "Line2D" : Line2D,
    "Circle2D" : Circle2D
}


def main(config_path, output_path, debug):
    with open(config_path) as f:
        config_data = json.load(f)
    num_points = config_data["num_points"]
    randomness = config_data["randomness"]
    shapes = []
    for shape, num in config_data["shapes"].items():
        for i in range(num):
            if shape in SHAPES:
                shapes.append(SHAPES[shape](num_points, randomness, debug))

    for shape in shapes:
        shape.GeneratePoints()
        if debug:
            shape.PlotGeneratedPoints()


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
