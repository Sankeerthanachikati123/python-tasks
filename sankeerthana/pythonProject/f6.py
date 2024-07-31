def count_lines_in_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = 0
            for line in file:
                lines += 1
        return lines
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

# Example usage:
filename = "f4.py"
line_count = count_lines_in_file(filename)
print(line_count)