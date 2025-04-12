import re
import sys

def convert_cpp_defines(input_text):
    output_lines = []

    for line in input_text.splitlines():
        original_line = line.rstrip()

        # Convert C++ style comments to ';' comments
        line = re.sub(r'//(.*)', r';\1', original_line)

        # Match defines
        define_match = re.match(r'#([A-Z0-9_]+)\s*=\s*(.+)', line)
        if define_match:
            name, value = define_match.groups()
            name = name.lower()
            value = value.strip()

            # Handle TRUE / FALSE
            if value.upper() == "TRUE":
                value = "$1"
            elif value.upper() == "FALSE":
                value = "$0"
            else:
                # Prefix hex value with '$'
                if re.fullmatch(r'[A-Fa-f0-9]+', value):
                    value = f"${value}"

            output_lines.append(f"!{name} = {value}")
        else:
            # Add $ to hex or TRUE/FALSE after '='
            def repl_value(match):
                val = match.group(1).strip()
                if val.upper() == "TRUE":
                    return "= $1"
                elif val.upper() == "FALSE":
                    return "= $0"
                elif re.fullmatch(r'[A-Fa-f0-9]+', val):
                    return f"= ${val}"
                else:
                    return f"= {val}"

            line = re.sub(r'=\s*([A-Za-z0-9]+)', repl_value, line)
            output_lines.append(line)

    return "\n".join(output_lines)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Only run this file with the provided NSMWHF builder")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    try:
        with open(input_filename, "r") as infile:
            input_data = infile.read()

        output_data = convert_cpp_defines(input_data)

        with open(output_filename, "w") as outfile:
            outfile.write(output_data)

        print(f"Defines.config converted to asar-valid ASM")
    except FileNotFoundError:
        print(f"File not found: {input_filename}")
    except Exception as e:
        print(f"An error occurred: {e}")
