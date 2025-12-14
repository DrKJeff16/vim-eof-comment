from .types.typeddict import BatchPairDict as BatchPairDict, BatchPathDict as BatchPathDict
from .util import die as die, error as error
from io import TextIOWrapper

def bootstrap_paths(paths: tuple[str], exts: tuple[str]) -> list[BatchPairDict]:
    """Bootstraps all the matching paths in current dir and below."""
def open_batch_paths(paths: list[BatchPairDict]) -> dict[str, BatchPathDict]:
    """Return a list of TextIO objects given file path strings."""
def modify_file(file: TextIOWrapper, comments: dict[str, str], ext: str, newline: bool, has_nwl: bool) -> str:
    """Modifies a file containing a bad EOF comment."""
# vim:ts=4:sts=4:sw=4:et:ai:si:sta:
