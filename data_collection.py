import kaggle
from pathlib import Path

kaggle.api.authenticate()

dataset = 'uciml/iris'

save_dir = Path('D:\Georgian-AI\Sem2\AI infra & archi\Assignment4')

kaggle.api.dataset_download_files(dataset, path=save_dir, unzip=True)
