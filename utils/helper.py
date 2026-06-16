from __future__ import annotations

import sys
from pathlib import Path


def resource_path(relative_path: str) -> str:
    """Return an absolute resource path for both dev mode and PyInstaller."""
    if hasattr(sys, "_MEIPASS"):
        base_path = Path(sys._MEIPASS)
    else:
        base_path = Path(__file__).resolve().parent.parent

    return str(base_path / relative_path)
