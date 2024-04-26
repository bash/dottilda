from pathlib import Path
from os import environ


def _state_dir() -> Path:
    state_home = Path(environ.get("XDG_STATE_HOME", Path.home() / ".local" / "state"))
    return state_home / "dottilda"


print(_state_dir())
