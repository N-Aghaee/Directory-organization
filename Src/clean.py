import shutil
from pathlib import Path
from Src.data import DATA_DIR
from Src.util.io import read_json
from loguru import logger


class Organize_file:
    def __init__(self, directory):
        self.directory = Path(directory)
        if not self.directory.exists():
            raise FileNotFoundError(f"{self.directory} does not exist")

        ext_dir = read_json(DATA_DIR / "extensions.json")

        self.extensions_dest = {}
        for dir_name, ext_list in ext_dir.items():
            for ext in ext_list:
                self.extensions_dest[ext] = dir_name

    def __call__(self):

        file_extension = []

        # Create destination directories outside the loop
        other_dir = self.directory / 'other'

        for file_path in self.directory.iterdir():
            if file_path.is_dir() or file_path.name.startswith(('.', '$')):
                continue

            file_extension.append(file_path.suffix)

            DEST_DIR = (
                other_dir if file_path.suffix not in self.extensions_dest else
                (self.directory / self.extensions_dest[file_path.suffix])
            )

            DEST_DIR.mkdir(exist_ok=True)

            logger.info(f'Moving {file_path} to {DEST_DIR}...')

            shutil.move(str(file_path), str(DEST_DIR))


if __name__ == "__main__":
   organize = Organize_file('/mnt/G')
   organize()
   logger.info("Done!")