s = input('Expression:')
tokens = []
while True:
    for index, ch in enumerate(s):
        if ch in ('+', '-', '/', '*'):
            # append all numbers to array not include the character
            tokens.append(float(s[:index]))
            # append character to array
            tokens.append(s[index])
            # "25+32*2"
            s = s[index + 1:]
            break
    else:
        tokens.append(float(s))
        break
# search for multiply/devide
for index in range(len(tokens) - 1, 0, -1):
    # value from array under index
    value = tokens[index]
    if value == '*':
        tokens[index - 1] = tokens[index - 1] * tokens[index + 1]
        del tokens[index:index + 2]
    elif value == '/':
        tokens[index - 1] = tokens[index - 1] / tokens[index + 1]
        # i+2 is a separate expression
        del tokens[index:index + 2]
# search for plus/minus
for index in range(len(tokens) - 1, 0, -1):
    value = tokens[index]
    if value == '+':
        tokens[index - 1] = tokens[index - 1] + tokens[index + 1]
        del tokens[index:index + 2]
    elif value == '-':
        tokens[index - 1] = tokens[index - 1] - tokens[index + 1]
        del tokens[index:index + 2]

print(tokens)

