import os
output_file = 'extra_files.txt'
# 检查两个文件夹内的文件名是否一致，并输出不一致的文件名

# 设定两个文件夹的路径
jpg_folder = '/media/funnywii/47CCF48AB06977A3/DATASET/TrashDet/南通实习生/sd/img'
txt_folder = '/media/funnywii/47CCF48AB06977A3/DATASET/TrashDet/南通实习生/sd/xml'

# 获取两个文件夹内的文件名（不包括扩展名）
jpg_files = set(os.path.splitext(file)[0] for file in os.listdir(jpg_folder) if file.endswith('.jpg'))
txt_files = set(os.path.splitext(file)[0] for file in os.listdir(txt_folder) if file.endswith('.xml'))

# 找出多出来的TXT文件
extra_txt_files = txt_files - jpg_files
extra_jpg_files = jpg_files - txt_files
print("多出来的TXT文件有：")
i = 0
for file in extra_txt_files:
    print(f"{file}.xml")
    i = i + 1
print(i)
i = 0
print("\n多出来的JPG文件有：")
for file in extra_jpg_files:
    print(f"{file}.jpg")
    i += 1
print(i)

# 打开输出文件并写入结果
with open(output_file, 'w') as f:
    # 写入多出来的TXT文件
    f.write("多出来的TXT文件有：\n")
    for file in extra_txt_files:
        f.write(f"'{file}.xml',\n")
    f.write("\n")
    
    # 写入多出来的JPG文件
    f.write("多出来的JPG文件有：\n")
    for file in extra_jpg_files:
        f.write(f"'{file}.jpg',\n")

print(f"结果已写入到文件 {output_file} 中。")