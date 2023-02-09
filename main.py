import os 

counter_variable = ''

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
    global counter_variable
    
    indents = 0
    while line[:4] == '    ':
        indents += 1
        line = line[4:]
    
    # Arithmetic Operators and Numeric Procedures
    line = line.replace('MOD', '%')
    line = line.replace('RANDOM', 'random.randint')
    
    # Relational and Boolean Operators
    line = line.replace('true', 'True')
    line = line.replace('false', 'False')
    line = line.replace('=', '==')
    line = line.replace('NOT', 'not')
    line = line.replace('AND', 'and')
    line = line.replace('OR', 'or')
    
    # Assignment, Display, and Input
    line = line.replace('<--', '=')
    line = line.replace('DISPLAY', 'print')
    line = line.replace('INPUT()', "convertInput(input('input: '))")
    
    # Selection
    if line[0] == '{' or line[0] == '}':
        return ''
    if line[:2] == 'IF':
        line = 'if' + line[2:]
        line += ':'
    if line[:4] == 'ELSE':
        line = 'else:'
    
    # Iteration
    if line[:6] == 'REPEAT' and line[-5:] == 'TIMES':
        loopNum = int(line[7:-6])
        counter_variable += '_'
        line = f'for {counter_variable} in range({loopNum}):'
    
    return ('    ' * indents) + line


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path + '\AP CSP Code.txt')
    code_file = open(dir_path + '\AP CSP Code.txt', 'r')
    
    lines = code_file.readlines()
    lines = removeNewLineIndicators(lines)
    
    python_code = ['from functions_for_output import *', 'import random', '']
    for line in lines:
        python_line = lineToPython(line)
        if python_line != '':
            python_code.append(python_line)
    python_code = '\n'.join(python_code)
    
    printAllCSPLines(lines)
    print('\n-----ALL LINES OF EQUIVALENT PYTHON CODE-----\n\n' + python_code + '\n\n')
    
    copyOutputToPythonFile(dir_path+'\code_in_python.py', python_code)
    
    code_file.close()

