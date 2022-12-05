
path=r'D:\Test\Python'

import os

os.mkdir(os.path.join(path,'bb'))
os.mkdir(os.path.join(path,'cc'))
os.mkdir(os.path.join(path,'dd'))
path1=os.path.join(path,'bb')
os.mkdir(os.path.join(path1,'aa'))
os.mkdir(os.path.join(path1,'bb'))
os.mkdir(os.path.join(path1,'cc'))

