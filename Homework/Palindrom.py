word = str(input('Please provide the string: '))
length = len(word) + 1
part_1 = word[0:length // 2]
part_2 = word[length // 2:]
if len(word) % 2 != 0:
    part_1 = part_1[:-1]
if part_1 == part_2[::-1]:
    print('Yes')
else:
    print('No')
