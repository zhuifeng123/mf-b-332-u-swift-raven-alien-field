#!/usr/bin/env python3
import os

ENTRY = (
    "Earth: 4 stars. Oceans superb, oxygen on the house, service dreadful: "
    "nobody answered my comet. The locals pay to watch other humans pretend. "
    "Would not return; would recommend."
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
