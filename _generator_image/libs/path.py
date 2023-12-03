
from pathlib import Path


def create_path(path: Path) -> None:
    # print(path)
    if not path.exists():
        path_result = Path(path.parts[0])
        # print(path.parts)
        for index_dir, _ in enumerate(path.parts):
            if index_dir >= 0:
                path_result = path_result.joinpath(path.parts[index_dir])
                if not path_result.exists():
                    path_result.mkdir()
