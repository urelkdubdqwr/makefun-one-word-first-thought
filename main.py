"""Write the single-word entry to entry.txt in the output directory.

The output directory is taken from $MAKEFUN_OUTPUT_DIR when it is set and
non-empty, otherwise it defaults to /output. The directory is created if it
does not exist. The file contains exactly "brontide" followed by one newline.
"""

import os
import sys
from pathlib import Path

ENTRY_TEXT = "brontide\n"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    target = Path(output_dir)
    try:
        target.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        print(f"error: cannot create output directory {target!r}: {exc}", file=sys.stderr)
        raise SystemExit(1)
    (target / "entry.txt").write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
