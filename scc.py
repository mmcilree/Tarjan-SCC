import sys

def read_instance(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            rows = len(lines)
            cols = len(lines[0].split())
            array = [[0] * cols for _ in range(rows)]

            for i in range(rows):
                line = lines[i].split()
                for j in range(cols):
                    array[i][j] = int(line[j])

            return array

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    except Exception as e:
        print("An error occurred while reading the file:", e)
        return None

def find_sccs(nodes):
    pass

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Please provide the file path as an argument.")
    else:
        file_path = sys.argv[1]
        nodes = read_instance(file_path)
        