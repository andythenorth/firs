#!/bin/zsh

# Directory with Python files
DIRECTORY="./src/cargos"

# Loop through each Python file in the directory
for file in $DIRECTORY/*.py; do
    # 1. Replace cargo_classes = "bitmask(...)" with cargo_classes = ["..."]
    sed -i '' -E \
    's/cargo_classes\s*=\s*"bitmask\(([^)]+)\)"/cargo_classes = [\1]/g' "$file"

    # 2. Add quotes around each CC_* entry inside the list, even if there are multiple entries
    sed -i '' -E \
    's/CC_([A-Za-z_0-9]+)/"CC_\1"/g' "$file"
done
