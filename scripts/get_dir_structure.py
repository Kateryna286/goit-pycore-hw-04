
from pathlib import Path
import sys
from colorama import init, Fore, Style

init(autoreset=True) 

def get_dir_structure(path: Path, indent: str = ""):
    if not path.exists():
        print(f"{Fore.RED}Path does not exist: {path}")
        return

    if path.is_dir():
        print(f"{Fore.BLUE}{indent}{path.name}/")
        for item in path.iterdir():
            get_dir_structure(item, indent + "  ")
    else:
        print(f"{Fore.GREEN}{indent}{path.name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{Fore.YELLOW}Usage: python get_dir_structure.py <path_to_directory>")
        sys.exit(1)

    dir_path = Path(sys.argv[1])

    if not dir_path.exists():
        print(f"{Fore.RED}Path does not exist: {dir_path}")
        sys.exit(1)

    if not dir_path.is_dir():
        print(f"{Fore.RED}The provided path is not a directory: {dir_path}")
        sys.exit(1)

    get_dir_structure(dir_path)
