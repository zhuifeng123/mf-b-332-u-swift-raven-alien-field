#!/usr/bin/env python3
import os

ENTRY = (
    "Earth: 3.5 stars. Oceans excellent, sunsets overrated, oxygen complimentary. "
    "The dominant species pays to watch other humans pretend to be someone else. "
    "Would not return."
)

def main() -> None:
    assert len(ENTRY) <= 200, len(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(len(ENTRY))

if __name__ == "__main__":
    main()
