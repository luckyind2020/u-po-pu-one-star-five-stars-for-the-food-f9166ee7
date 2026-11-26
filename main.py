"""One-star alien review of Earth: entry printer for make.fun."""
import pathlib

ENTRY_PATH = pathlib.Path(__file__).with_name("entry.txt")


def load_line(path=ENTRY_PATH):
    return path.read_text(encoding="utf-8").strip()


def validate_line(line, limit=200):
    if not line:
        raise ValueError("entry is empty")
    if len(line) > limit:
        raise ValueError(f"entry is {len(line)} chars, over the {limit} limit")
    return line


def main():
    print(validate_line(load_line()))


if __name__ == "__main__":
    main()
