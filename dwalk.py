import os


for folderName ,subfolders, filenames in os.walk(r'D:\Test\Python'):   #直接递归遍历完给定目录，将三个参数返回在循环里操作。迭代器类似于返回一个目录信息。
    print('current folder is' + folderName)
    for subfolder in subfolders:
        print('subfolder is'+ folderName+':'+subfolder)
    for filename in filenames:
        print('file inside'+folderName+': '+filename)
    print('---------------')
