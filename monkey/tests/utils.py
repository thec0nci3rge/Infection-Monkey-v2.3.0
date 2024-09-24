import filecmp
import threading
from pathlib import Path
from unittest.mock import MagicMock

from monkeytoolbox import get_binary_io_sha256_hash


def raise_(ex):
    raise ex


def get_file_sha256_hash(filepath: Path) -> str:
    """
    Calculates sha256 hash from a file path

    :param filepath: A Path object which defines file on the system
    :return sha256 hash of the file
    """
    with open(filepath, "rb") as f:
        return get_binary_io_sha256_hash(f)


def assert_directories_equal(dir1: Path, dir2: Path):
    assert dir1.is_dir()
    assert dir2.is_dir()

    dircmp = filecmp.dircmp(dir1, dir2, ignore=[])

    _assert_dircmp_equal(dircmp)


def _assert_dircmp_equal(dircmp: filecmp.dircmp):
    assert len(dircmp.diff_files) == 0
    assert dircmp.left_list == dircmp.right_list

    for subdir_cmp in dircmp.subdirs.values():
        _assert_dircmp_equal(subdir_cmp)


class ThreadSafeMagicMock:
    def __init__(self, *args, **kwargs):
        self._lock = threading.Lock()
        self._mock = MagicMock()

    def __call__(self, *args, **kwargs):
        with self._lock:
            return self._mock(*args, **kwargs)

    def __getattr__(self, name):
        with self._lock:
            return getattr(self._mock, name)
