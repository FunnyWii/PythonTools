import os
base_path = '/media/funnywii/47CCF48AB06977A3/DATASET/TrashDet/南通实习生/sxw/xml'
# 文件列表
files_to_delete = [
'13.xml',
'16.xml',
'15.xml',
'14.xml',
]

# 遍历文件列表并删除文件
for file_name in files_to_delete:
    file_path = os.path.join(base_path, file_name)
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"文件 {file_path} 已删除。")
    else:
        print(f"文件 {file_path} 不存在。")
