# 对文件夹内的内容进行重新排序并重命名。
# 适用于有多个文件夹的内的内容，但是存在命名冲突。

import os
import os.path
rootdir = "/home/funnywii/Documents/TrashDetTemp/img2/" #末尾斜杠不要丢
files = os.listdir(rootdir)
files.sort()
b = 2353
for name in files:
    a=os.path.splitext(name)
    newname = str(b)+'.jpg'
    print(a[0] + "->" + newname)
    b = b + 1
    os.rename(rootdir+name,rootdir+newname)


# def rename_files(folder_path, start_number):
#     # 获取文件夹中所有文件名
#     files = [f for f in os.listdir(folder_path) if f.endswith(".xml")]

#     # 确保文件按照数字顺序排序
#     files.sort(key=lambda x: int(x.split('.')[0]))

#     # 从指定数字开始，为每个文件重命名
#     for i, file_name in enumerate(files):
#         new_name = f"{start_number + i}.xml"
#         old_path = os.path.join(folder_path, file_name)
#         new_path = os.path.join(folder_path, new_name)
        
#         # 使用绝对路径进行重命名
#         os.rename(old_path, new_path)
#         print(f"Renamed: {file_name} -> {new_name}")

# # 用法示例
# folder_path = '/home/funnywii/Documents/TempDataset/tf-lights-v2.0/label' # 修改为你的文件夹路径
# start_number = 820  # 修改为你想要的起始数字
# rename_files(folder_path, start_number)
