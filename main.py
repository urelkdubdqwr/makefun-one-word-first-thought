import os
from pathlib import Path

ENTRY_TEXT = "brontide\n"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    target = Path(output_dir)
    target.mkdir(parents=True, exist_ok=True)
    (target / "entry.txt").write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
