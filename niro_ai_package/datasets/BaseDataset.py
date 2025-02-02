class BaseDataset:
    def __init__(self, dataset_config):
        self.dataset_config = dataset_config
        self.data_path = dataset_config['data_path']
