import os
import shutil

apath='D:\\Test\\a.txt'
print(shutil.move(r'D:\Test\a.txt',r'D:\\b.txt'))      #移动或者重命名文件或目录
print(shutil.move(r'D:\Test\Python\aa',r'D:\Test\Python\aaa'))
print(shutil.move(r'D:\Test\Python\aaa',r'D:\Test\Python\aa'))
print(shutil.copy(r'D:\b.txt',apath))  #只能复制文件，如果右边是文件，左边也是文件，就复制过去，并替换文件名 返回复制后的路径
print(shutil.copytree(r'D:\Test\Python\aa',r'D:\Test\aa'))  #递归复制目录的时候，会将源目录名替换目的目录名，所以目录目录名不存在才能成功。
print(shutil.rmtree(r"D:\Test\aa"))  #递归删除目标目录
