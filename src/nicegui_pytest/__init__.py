"""書籍管理システム"""

from importlib.metadata import metadata

import fire

from .pages import run_app

_package_metadata = metadata(str(__package__))
__version__ = _package_metadata["Version"]
__author__ = _package_metadata.get("Author-email", "")

__all__ = ["__author__", "__version__", "run_app"]


def main() -> None:
    """スクリプト実行"""
    fire.Fire(run_app)
