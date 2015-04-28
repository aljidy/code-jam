f = open('B-small-practice.in')
yourList = f.readlines()
import re
# yourList = [line.rstrip('\n') for line in f]
# print yourList
for i in yourList:
    i = i[:-1]   # Strips newline
    # print i
    if i.find(" ") != -1:
        currentLine = i.split(' ')
        # currentLine = re.split('(\W)', i)
        currentLine = currentLine[::-1]
        currentLine = ' '.join(currentLine)
        print 'Case #' + str(i) + ':' + currentLine
    elif i.find("[0-9]"):
        continue
    else:
        print i
