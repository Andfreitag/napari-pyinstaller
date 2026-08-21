from pathlib import Path

import debugpy
from PyInstaller.utils.hooks import collect_submodules

debugpy_path = Path(debugpy.__file__).parent
vendored_path = debugpy_path / "_vendored"

datas = [
    (str(vendored_path), "debugpy/_vendored"),
]

hiddenimports = collect_submodules("debugpy")