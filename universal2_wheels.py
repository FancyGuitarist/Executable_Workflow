from delocate.fuse import fuse_wheels
from pathlib import Path


def main():
    if not Path('combined_wheels').exists():
        Path('combined_wheels').mkdir()
    if not Path('combined_wheels/opencv_python-4.10.0.84-cp37-abi3-macosx_12_0_universal2.whl').exists():
        fuse_wheels('wheels_to_combine/opencv_python-4.10.0.84-cp37-abi3-macosx_11_0_arm64.whl',
                    'wheels_to_combine/opencv_python-4.10.0.84-cp37-abi3-macosx_12_0_x86_64.whl',
                    'combined_wheels/opencv_python-4.10.0.84-cp37-abi3-macosx_12_0_universal2.whl')
    else:
        print('Universal2 wheel for opencv already exists')
    if not Path('combined_wheels/numpy-2.0.0-cp312-cp312-macosx_11_0_universal2.whl').exists():
        fuse_wheels('wheels_to_combine/numpy-2.0.0-cp312-cp312-macosx_10_9_x86_64.whl',
                    'wheels_to_combine/numpy-2.0.0-cp312-cp312-macosx_11_0_arm64.whl',
                    'combined_wheels/numpy-2.0.0-cp312-cp312-macosx_11_0_universal2.whl')
    else:
        print('Universal2 wheel for numpy already exists')
    if not Path('combined_wheels/pillow-10.3.0-cp312-cp312-macosx_11_0_universal2.whl').exists():
        fuse_wheels('wheels_to_combine/pillow-10.3.0-cp312-cp312-macosx_10_10_x86_64.whl',
                    'wheels_to_combine/pillow-10.3.0-cp312-cp312-macosx_11_0_arm64.whl',
                    'combined_wheels/pillow-10.3.0-cp312-cp312-macosx_11_0_universal2.whl')
    else:
        print('Universal2 wheel for pillow already exists')


if __name__ == '__main__':
    main()
    # Test app
