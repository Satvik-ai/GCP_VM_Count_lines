import sys

def count_lines(file_path):
    output_file = "output_file.txt"
    
    try:
        with open(file_path, 'r') as file:
            line_count = sum(1 for line in file)

        result = f"Total lines in '{file_path}': {line_count}\n"
        print(result.strip())  # Print to console

        # Create the output file if it doesn't exist and write the output
        with open(output_file, 'w') as out_file:
            out_file.write(result)

        print(f"Output written to '{output_file}'")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please entre the input file. Usage: python count_lines.py <file_path>")
    else:
        count_lines(sys.argv[1])