# Demonstration of file handling in Python

def write_text_to_file(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
        print(f"written to {file_name}")
    except Exception as e:
        print(f"Error writing to file: {e}")


def append_text_to_file(file_name, content):
    try:
        with open(file_name, 'a') as file:
            file.write(content)
        print(f"appended to {file_name}")
    except Exception as e:
        print(f"Error appending to file: {e}")


def read_text_from_file(file_name, read_lines=False):
    try:
        with open(file_name, 'r') as file:
            if read_lines:
                lines = file.readlines()
                print(f"Lines read from {file_name}:")
                for line in lines:
                    print(line, end='')
                return lines
            else:
                read_text = file.read()
                print(f"Read from {file_name}:\n{read_text}")
                return read_text
    except FileNotFoundError:
        print(f"{file_name} not found.")
    except Exception as e:
        print(f"Error reading from file: {e}")


if __name__ == "__main__":
    filename = "my_file.txt"

    # Writing to a file
    to_write = "How to do file handling in Python? Now I have an Idea.\n"
    write_text_to_file(filename, to_write)

    # Appending to a file
    to_append = "Adding additional line to the file. Got it, how to append.\n"
    append_text_to_file(filename, to_append)

    # Reading from a file
    read_text_from_file(filename)

    # Reading lines from a file
    read_text_from_file(filename, read_lines=True)
