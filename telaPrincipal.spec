# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['telaPrincipal.py'],
    pathex=[],
    binaries=[],
    datas=[('logo_biblio.png', '.'), ('logo_biblio2.png', '.'), ('logo_biblio3.png', '.'), ('bancoBiblio.db', '.')],
    hiddenimports=["'PIL._tkinter_finder'"],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='telaPrincipal',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icon_biblio.ico'],
)
