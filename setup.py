import os
import re

# Root directory (adjust if needed)
root_dir = '.'

# Regex to match chapter folders
chapter_pattern = re.compile(r'^chapter_\d+$')
# Regex to match Python files starting with pNN (e.g., p01_, p02-, etc.)
file_pattern = re.compile(r'^(p\d+[-_].+)\.py$')

for dirpath, dirnames, filenames in os.walk(root_dir):
    folder = os.path.basename(dirpath)

    if not chapter_pattern.match(folder):
        continue

    for filename in filenames:
        match = file_pattern.match(filename)
        if match:
            base_name = match.group(1)  # e.g., "p01_triplestep" or "p02-foo"
            new_filename = f"{base_name}_my_solution.py"
            new_filepath = os.path.join(dirpath, new_filename)

            if not os.path.exists(new_filepath):
                with open(new_filepath, 'w') as f:
                    f.write(f"# My solution to {filename}\n")
                print(f"Created: {new_filepath}")
