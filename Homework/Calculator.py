s = input('Expression:')
tokens = []
while True:
    for index, ch in enumerate(s):
        if ch in ('+', '-', '/', '*'):
            # append all numbers to array not include the character
            tokens.append(float(s[:index]))
            # append charcter to array
            tokens.append(s[index])
            # "25+32*2"
            s = s[index + 1:]
            break
    else:
        tokens.append(float(s))
        break
# search for multiply
for index in range(len(tokens) - 1, 0, -1):
    # value from array uder index
    value = tokens[index]
    if value == '*':
        tokens[index - 1] = tokens[index - 1] * tokens[index + 1]
        # i+2 is a separate expression
        del tokens[index:index + 2]
# search for divide
for index in range(len(tokens) - 1, 0, -1):
    value = tokens[index]
    if value == '/':
        tokens[index - 1] = tokens[index - 1] / tokens[index + 1]
        del tokens[index:index + 2]
# search for plus
for index in range(len(tokens) - 1, 0, -1):
    value = tokens[index]
    if value == '+':
        tokens[index - 1] = tokens[index - 1] + tokens[index + 1]
        del tokens[index:index + 2]
# search for minus
for index in range(len(tokens) - 1, 0, -1):
    value = tokens[index]
    if value == '-':
        tokens[index - 1] = tokens[index - 1] - tokens[index + 1]
        del tokens[index:index + 2]
print(tokens)
