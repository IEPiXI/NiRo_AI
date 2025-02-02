# niro_ai_package/main.py
import argparse
import json
from pathlib import Path

from niro_ai_package.datasets.AIvsHumanDataset import AIvsHumanDataset


def main(config):
    dataset = AIvsHumanDataset(config)
    dataset.download()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='NiRo-AI',
        description='Package for training and testing AI tasks',
        epilog='Created by Nicolas Freitag and Robert Krug',
    )
    default_config_path = Path(__file__).resolve().parent / 'configs' / 'config.json'
    parser.add_argument('-c', '--config', default=default_config_path)
    args = parser.parse_args()

    with open(args.config, 'r') as config_path:
        config = json.load(config_path)
    main(config)
