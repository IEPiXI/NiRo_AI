from niro_ai_package.datasets.BaseDataset import BaseDataset


class AIvsHumanDataset(BaseDataset):
    def __init__(self, dataset_config):
        super().__init__(dataset_config)
