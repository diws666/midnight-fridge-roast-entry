import os

# Verified count: 124 characters (124 UTF-8 bytes), 1 line, no trailing newline.
LINE = "It is 2 a.m. The fridge light is on, the door is locked, and the fridge is pretending it cannot hear me begging for a snack."

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
output_path = os.path.join(output_dir, 'entry.txt')

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(LINE)

print(len(LINE))
