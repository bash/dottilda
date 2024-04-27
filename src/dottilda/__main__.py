from pathlib import Path
from os import makedirs, symlink
from argparse import ArgumentParser
from typing import List, Optional
import sys
from xdg_base_dirs import xdg_config_home, xdg_state_home
from os.path import relpath

# dottilda init <config_file>
# dottilda sync [--init]
# dottilda add <rel_path> [<rel_src_path>] [-t f|d] [--os linux|macos]
# dottilda rm <rel_path>


def dottilda(raw_args: List[str]) -> None:
    args = _parse_arguments(raw_args)
    match args.command:
        case "init":
            return init(args.path)
        case _:
            return sync()


def _parse_arguments(raw_args: List[str]) -> ArgumentParser:
    parser = ArgumentParser("dottilda", description="Manage dotfiles with symlinks")
    subparsers = parser.add_subparsers(dest="command")
    init = subparsers.add_parser("init")
    init.add_argument("path", type=Path)
    return parser.parse_args(raw_args)


def init(config_file: Path) -> int:
    # TODO: validate if config_file exists
    if _config_dir().exists():
        print("error: dottilda is already initialized")
        return 1
    print("Initializing dottilda")
    makedirs(_config_dir(), exist_ok=True)
    symlink(relpath(config_file, start=_config_dir()), _config_dir() / "config.json")
    sync()
    return 0


def sync() -> int:
    print("TODO: sync")
    return 0


def _config_dir() -> Optional[Path]:
    return xdg_config_home() / "dottilda"


def _state_dir() -> Path:
    return xdg_state_home() / "dottilda"


exit(dottilda(sys.argv[1:]))
