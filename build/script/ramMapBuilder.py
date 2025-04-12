import re
import sys

def convert_ram_macros_and_comments(input_text):
    output_lines = []

    for line in input_text.splitlines():
        line = line.rstrip()

        # Convert C++ style comments to ';' comments
        line = re.sub(r'//(.*)', r';\1', line)

        # Convert #ram(label, size) to label: skip size
        ram_match = re.match(r'#ram\(\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*,\s*(\d+)\s*\)', line)
        if ram_match:
            label, size = ram_match.groups()
            output_lines.append(f"{label}: skip {size}")
        else:
            output_lines.append(line)

    return "\n".join(output_lines)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Run this via make.bat")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    try:
        with open(input_filename, "r") as infile:
            input_data = infile.read()

        output_data = convert_ram_macros_and_comments(input_data)

        with open(output_filename, "w") as outfile:
            outfile.write(output_data)

        print(f"RAM.config converted to asar-valid ASM")
    except FileNotFoundError:
        print(f"File not found: {input_filename}")
    except Exception as e:
        print(f"An error occurred: {e}")
