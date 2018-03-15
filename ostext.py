# os 模块

from __future__ import division

import os,sys,stat


filepath = '/Users/pro/Desktop/程序'


files_dict = dict()
def getFileSize(file):
    if os.path.exists(file):
        size = os.path.getsize(file)
        files_dict[file] = size

getFileSize(filepath)
print(files_dict)

# os.access(filepath,os.F_OK)
# os.access(filepath,os.W_OK)
# os.access(filepath,os.R_OK)
# os.access(filepath,os.X_OK)
#
#
# print(os.getcwd())
# 修改路径
# os.chdir('/Users/pro/Desktop')

# 给文件设置权限
# stat.UF_NODUMP: 非转储文件
# stat.UF_IMMUTABLE: 文件是只读的
# stat.UF_APPEND: 文件只能追加内容
# stat.UF_NOUNLINK: 文件不可删除
# stat.UF_OPAQUE: 目录不透明，需要通过联合堆栈查看
# stat.SF_ARCHIVED: 可存档文件(超级用户可设)
# stat.SF_IMMUTABLE: 文件是只读的(超级用户可设)
# stat.SF_APPEND: 文件只能追加内容(超级用户可设)
# stat.SF_NOUNLINK: 文件不可删除(超级用户可设)
# stat.SF_SNAPSHOT: 快照文件(超级用户可设)


# flg = stat.UF_IMMUTABLE
# os.chflags(filepath,flg)

# isw = os.access(filepath,os.W_OK)
# print(isw)
# 修改权限
# os.chmod(filepath,stat.S_IWOTH)
# 修改所有者ID
# os.chown(filepath,100,-1)
# 修改当前进程根目录
# os.chroot(filepath)
# 关闭文件描述
# os.close(f)

# while True:
#     try:
#         x = int(input('输入一个整数'))
#         break
#     except ValueError:
#         print('傻子  这不是整数')

# raise  这个就是抛出异常的类


















