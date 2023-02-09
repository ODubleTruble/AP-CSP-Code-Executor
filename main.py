import os 

# Removes the \n at the end of each line.
# All lines except the last line have a \n.
def removeNewLineIndicators(all_lines):
    # Runs for all lines except the last.
    for i in range(len(all_lines) - 1):
        line_len = len(all_lines[i])
        all_lines[i] = all_lines[i][:line_len-1]

    return all_lines


def printAllCSPLines(lines: list):
    print('\n-----ALL LINES OF AP CSP CODE-----\n')
    for line in lines:
        print(line)


def copyOutputToPythonFile(file_location: str, pythonCode: str):
    output_file = open(file_location, 'w')
    output_file.write(pythonCode)
    output_file.close()
    print('The python code has been copied to ' + file_location + '\n')


def lineToPython(line):
    line = line.replace('<--', '=')
    line = line.replace('DISPLAY', 'print')
    line = line.replace('INPUT()', "float(input('input: '))")
    line = line.replace('MOD', '%')
    line = line.replace('RANDOM', 'random.randint')

    return line


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path + '\AP CSP Code.txt')
    code_file = open(dir_path + '\AP CSP Code.txt', 'r')
    
    lines = code_file.readlines()
    lines = removeNewLineIndicators(lines)
    
    python_code = ['import random', '']
    for line in lines:
        python_code.append(lineToPython(line))
    python_code = '\n'.join(python_code)
    
    printAllCSPLines(lines)
    print('\n-----ALL LINES OF EQUIVALENT PYTHON CODE-----\n\n' + python_code + '\n\n')
    
    copyOutputToPythonFile(dir_path+'\output.py', python_code)
    
    code_file.close()

