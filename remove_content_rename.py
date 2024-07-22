import os
import re

# 去括号
def remove_parentheses_from_filenames(folder_path):
    # 遍历文件夹中的文件
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # 判断是否为文件
        if os.path.isfile(file_path):
            # 使用正则表达式去掉括号及括号内的数字
            new_filename = re.sub(r'^\((\d+)\)', r'\1', filename)

            # 构建新的文件路径
            new_file_path = os.path.join(folder_path, new_filename)

            # 重命名文件
            os.rename(file_path, new_file_path)
            print(f'Renamed: {filename} -> {new_filename}')

if __name__ == "__main__":
    folder_path = '/home/funnywii/Documents/TempDataset/TempProcess/TACO/xml'
    remove_parentheses_from_filenames(folder_path)
