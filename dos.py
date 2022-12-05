import os

myfile = ['aaaa.txt', 'bbb.txt', 'cccc.txdt']
for name in myfile:
    print(os.path.join('c\\dd\\bb', name))  #利用join函数拼接路径，与平台无关。
print(os.getcwd())  # 获取当前工作路径
os.chdir("D:\\")  #改变工作路径
print(os.getcwd())
os.chdir(os.path.join(os.getcwd(),"Test","Python"))
print(os.getcwd())
#os.makedirs(os.path.join(os.getcwd(),'aa','bb','vv','dd')) #递归建立文件夹
print(os.path.abspath('.'))  #根据相对路径返回绝对路径
print(os.path.isabs('.'))   #判断是否是绝对路径
print(os.path.isabs(os.path.abspath('.')))
print(os.path.relpath('D:\\Test','D:\\'))    #以后面参数为基准（当作绝对根路径），返回路径的相对地址
print(os.path.basename('D:\\Test\\a.txt'))   #返回路径末尾的最后一个斜杠后的名字（返回文件名）
print(os.path.dirname('D:\\Test\\a.txt'))    #返回最后斜杠之前文件路径（返回文件所在路径)
apath='D:\\Test\\a.txt'
print(apath.split(os.path.sep))  #os.path.sep获取当前系统文件路径分割符 ，在动用字符串方法发分割。
print(os.path.getsize(apath) ) #获得文件大小
print(os.path.getsize(os.path.dirname(apath)))   #获取路径大小不会递归4096
print(os.path.getsize('D:\\'))  #获取路径大小是错误的，8192
print(os.listdir(os.path.dirname(apath)))  #获取目录下文件列表
print(os.path.exists(apath))  #几个判断函数
print(os.path.isdir(apath))
print(os.path.isfile(apath))
