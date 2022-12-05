import re
import os
from DataEntity import DataEntity

if __name__ == '__main__':
    dataregex = re.compile(r'(\d+)-(\d+)-(\d+)T(\d+):(\d+):(\d+)Z,(\d+),(\w+),(\w+),(\d+\w),(\d+.\d+),(\d+.\d+),(\d+)')
    path = r'data'
    filenames = [r'PM25history_2016_01_101010100_201601.txt','PM25history_2016_01_101220101_201601.txt']
    datafile = os.path.join(path, filenames[1])
    with open(datafile, 'r') as f:
        line1 = f.readline()
        list=[]
        for index, line in enumerate(f):
            mo = dataregex.search(line)
            res = mo.groups()
            data = DataEntity(res)
            list.append(data)
        print(len(list))
        for item in list:
            print(item)