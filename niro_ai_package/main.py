# niro_ai_package/main.py
import argparse
import json

from datasets import AIvsHumanDataset


def main(config):
    dataset = AIvsHumanDataset(config)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="NiRo-AI",
        description="Package for training and testing AI tasks",
        epilog="Created by Nioclas Freitag and Robert Krug",
    )
    parser.add_argument("-c", "--config", default="../configs/config.json")
    args = parser.parse_args()

    with open(args.config, "r") as config_path:
        config = json.load(config_path)
    main(config)
