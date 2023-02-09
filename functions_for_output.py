def convertInput(input):
    output = None
    try:
        output = float(input)
    except TypeError:
        return input
    if output == int(output):
        return int(output)
    return output
