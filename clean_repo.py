import os
import shutil


def fast_scandir(dirname):
    sub_folders = [f.path for f in os.scandir(dirname) if f.is_dir()]
    for dirname in list(sub_folders):
        sub_folders.extend(fast_scandir(dirname))
    return sub_folders


def main():
    for folder in fast_scandir(f"{os.path.dirname(__file__)}/src"):
        if "build" in folder \
                or "__pycache__" in folder \
                or ".egg-info" in folder:

            try:
                shutil.rmtree(folder)
            except FileNotFoundError:
                continue


if __name__ == "__main__":
    main()
