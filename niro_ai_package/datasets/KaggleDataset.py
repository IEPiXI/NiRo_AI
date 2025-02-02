from niro_ai_package.datasets.BaseDataset import BaseDataset
import kagglehub

class KaggleDataset(BaseDataset):
    def __init__(self, dataset_config, kaggle_path):
        super().__init__(dataset_config)
        self.kaggle_path = kaggle_path

    def download(self):
        path = kagglehub.dataset_download(self.kaggle_path)
        return path

