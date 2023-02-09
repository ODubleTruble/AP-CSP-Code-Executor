import os 

# Removes the \n at the end of each line.
# All lines except the last line have a \n.
def removeNewLineIndicators(all_lines):
    # Runs for all lines except the last.
    for i in range(len(all_lines) - 1):
        line_len = len(all_lines[i])
        all_lines[i] = all_lines[i][:line_len-1]

    return all_lines


def lineToPython(line):
    line = line.replace('←', '=')
    line = line.replace('DISPLAY', 'print')

    return line


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path + '\AP CSP Code.txt')
    code_file = open(dir_path + '\AP CSP Code.txt', 'r', encoding="utf8")
    lines = code_file.readlines()
    lines = removeNewLineIndicators(lines)

    print('\n-----ALL LINES OF AP CSP CODE-----\n')
    for line in lines:
        print(line)
    print('\n-----ALL LINES OF EQUIVALENT PYTHON CODE-----\n')
    for line in lines:
        print(lineToPython(line))
    print()
    
    code_file.close()
