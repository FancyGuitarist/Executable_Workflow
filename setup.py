from setuptools import setup

APP = ['tkapp.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': False,
    'packages': ['numpy', 'PIL', 'tkinter', 'zlib'],
    'includes': ['numpy', 'PIL', 'tkinter', 'zlib'],
    'iconfile': 'Bliq_logo_stitch.icns',
    'plist': {
        'CFBundleName': 'ExecutableApp',
        'CFBundleDisplayName': 'ExecutableApp',
        'CFBundleIdentifier': 'com.bliq.executableapp',
        'CFBundleShortVersionString': '0.1.0',
        'CFBundleVersion': '0.1.0',
        'CFBundleDevelopmentRegion': 'en-CA',
        'CFBundleExecutable': 'ExecutableApp',
        'CFBundleIconFile': 'Bliq_logo_stitch.icns',
        'NSHumanReadableCopyright': '© 2024 Bliq Photonics',

    },
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    install_requires=['numpy', 'Pillow']
)
