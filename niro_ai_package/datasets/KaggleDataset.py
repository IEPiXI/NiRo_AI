import os

import kagglehub

from niro_ai_package.datasets.BaseDataset import BaseDataset


class KaggleDataset(BaseDataset):
    def __init__(self, dataset_config, kaggle_path):
        super().__init__(dataset_config)
        # use the parent of the data_path as kaggle already downloads to '/datasets'
        os.environ['KAGGLEHUB_CACHE'] = str(self.data_path.parent.resolve())
        self.kaggle_path = kaggle_path

    def download(self):
        path = kagglehub.dataset_download(self.kaggle_path)
        return path
