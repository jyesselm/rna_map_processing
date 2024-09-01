from pathlib import Path

LIB_NAME: str = "rna_map_processing"


def get_lib_path() -> Path:
    """
    Get the path to the library root directory.

    Returns:
        Path: The path to the library root directory.
    """
    return Path(__file__).resolve().parent.parent


def get_py_path() -> Path:
    """
    Get the path to the Python package directory.

    Returns:
        Path: The path to the Python package directory.
    """
    return get_lib_path() / LIB_NAME


def get_resources_path() -> Path:
    """
    Get the path to the resources directory.

    Returns:
        Path: The path to the resources directory.
    """
    return get_py_path() / "resources"
