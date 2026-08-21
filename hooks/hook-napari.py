from PyInstaller.utils.hooks import (
    collect_data_files,
    collect_entry_point,
)

datas = collect_data_files("napari")

plugin_datas, plugin_hiddenimports = collect_entry_point("napari.manifest")

datas += plugin_datas

hiddenimports = [
    "napari.__main__",
    "napari._event_loop",
    *plugin_hiddenimports,
]