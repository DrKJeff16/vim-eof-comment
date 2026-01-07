from argparse import ArgumentParser
from typing import NoReturn

__all__ = ['complete_parser', 'complete_validator']

def complete_validator(completion_candidate: list[str], current_input: str) -> bool:
    """
    Complete non-prefix substring matches.

    Parameters
    ----------
    completion_candidate : List[str]
        All the completion candidates.
    current_input : str
        The current input string.

    Returns
    -------
    bool
        Whether the current input fits the completion candidates pool.
    """
def complete_parser(parser: ArgumentParser, **kwargs) -> NoReturn:
    """
    Complete the script argument parser.

    Parameters
    ----------
    parser : argparse.ArgumentParser
        The ``ArgumentParser`` object.
    **kwargs
        Extra parameters to be passed to ``argcomplete.autocomplete()``.
    """

# vim: set ts=4 sts=4 sw=4 et ai si sta:
