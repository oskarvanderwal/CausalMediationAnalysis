"""Code borrowed from https://github.com/abersheeran/poetry2setup/blob/master/poetry2setup.py"""

from __future__ import print_function

from pathlib import Path

from poetry.core.factory import Factory
from poetry.core.masonry.builders.sdist import SdistBuilder


def build_setup_py():
    return SdistBuilder(Factory().create_poetry(Path(".").resolve())).build_setup()


def main():
    print(build_setup_py().decode("utf8"))


if __name__ == "__main__":
    main()