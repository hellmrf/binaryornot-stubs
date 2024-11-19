import logging
import os

logger: logging.Logger

def is_binary(filename: str | bytes | os.PathLike) -> bool: ...
