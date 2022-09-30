import pandas as pd
import matplotlib.pyplot as plt
from decimal import *

def PlotFunction(data_plt, time_plt):
    # plt.plot(data_plt)
    # plt.show()
    pass

def GetDataFromFile(line):
    num = 0
    line = line.replace('\t', ' ')
    line = line.replace(' ', '', 1)

    while line[num:]:
        if line[num] == ' ':
            num += 1
            line = line[num:]
            break
        num += 1

    while line[num:]:
        if line[num] == ' ':
            line = line[:num]
            break
        num += 1

    line_data = line
    # print(line_data)
    return line_data


def GetTimeFromFile(line):
    point = 13
    line_time = ''
    if line.find("# Timepoint: ") != -1:
        line_time = line[point:]
    else:
        line_time = 'None'
    return line_time


def ParserFunction():
    data = []
    time = []
    data_i = data_j = -1
    time_buff = data_buff = ''
    flag = False
    null_str = False

    first_file_name = 'Tout.txt'
    second_file_name = 'TPkni_out_B.txt'

    with open(second_file_name, encoding='utf-8') as file:
        lines = file.readlines()
    for line in lines:
        if null_str == False and line == '\n':
            null_str = True
            continue

        if line == '\n':
            flag = False
            continue
        ###############################################################
        time_buff = GetTimeFromFile(line)

        if time_buff != 'None':
            ltn = len(time_buff)-1
            time_buff = time_buff[:ltn]
            time.append(time_buff)
        ###############################################################
        if line.find('# Param:') != -1:
            data.append([])
            data_i += 1
            if data_i > -1:
                data_j += 1
            flag = True
            continue

        if flag == True:
            data_buff = Decimal(GetDataFromFile(line))
            data[data_i].append(data_buff)

    PandasWork(data,time)
    #PlotFunction()
    #PandasWork(time)

def PandasWork(data_pd,time_pd):
    ppp = pd.DataFrame(data_pd,time_pd)
    plt.plot(ppp)
    plt.xticks(rotation=45)
    plt.show()
    PlotFunction(data_pd, time_pd)
###############################################################


def main():
    ParserFunction()

if __name__ == "__main__":
    main()