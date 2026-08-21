from PyInstaller.utils.hooks import collect_all, copy_metadata

datas, binaries, hiddenimports = collect_all("napari_nifti")

datas += copy_metadata("napari-nifti")