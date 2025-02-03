from niro_ai_package.datasets.KaggleDataset import KaggleDataset


class AIvsHumanDataset(KaggleDataset):
    def __init__(self, dataset_config):
        super().__init__(dataset_config, kaggle_path='alessandrasala79/ai-vs-human-generated-dataset')
