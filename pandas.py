# -*- coding: utf8 -*-
def ReadAllFilesInLins(fileName):
    with open(fileName, 'r', encoding='utf-8') as file:
        fileInLines = file.readlines()
    return fileInLines

def WriteAllFilesInLins(fileName,data):
    pass


def getDatafromLine(lines, time):
    temp = ''
    for num in range(1):
        tab = lines.find('\t')
        if lines.find('#') == -1:
            temp = lines[:tab]
        print(temp)
    point = lines.rfind('# Timepoint: ')
    if point != -1:
        time.append(lines[13:])
        # print(time)
    return time

def SplitLinsInFile():
    global Name1
    time = []
    Name1 = 'Tout.txt'
    Name2 = 'ToutNew.txt'
    data = ''
    dataFromFile = ReadAllFilesInLins(Name1)
    for line in dataFromFile:
        # print(line)
        if line.find('#') == -1:
            # print(line)
            # line = line.replace("\t", " ")
            # print(type(line))

            # print(line)
            data += line
            # data.append(line)
        else:
            getDatafromLine(line, time)
            data += line
            # data.append(line)
            # print(data)
    WriteAllFilesInLins(Name2, data)
    # print(data)

if __name__ == '__main__':
    SplitLinsInFile()


