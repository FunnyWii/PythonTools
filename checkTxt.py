import os
from collections import defaultdict

# 指定包含文本文件的文件夹路径
folder_path = '/home/funnywii/Documents/TempDataset/AC/0530/txt'

# 指定包含文本文件的文件夹路径

# 创建一个字典来存储第一个数字的出现次数
first_number_counts = defaultdict(int)

# 创建一个变量来存储空文件的数量
empty_files_count = 0

# 遍历文件夹内的所有文件
for filename in os.listdir(folder_path):
    # 检查文件是否为文本文件
    if filename.endswith('.txt'):
        # 构建完整的文件路径
        file_path = os.path.join(folder_path, filename)
        # 获取文件大小
        file_size = os.path.getsize(file_path)
        # 如果文件为空
        if file_size == 0:
            empty_files_count += 1
            print(file_path)
        else:
            # 打开并读取文件内容
            with open(file_path, 'r') as file:
                # 读取第一行
                first_line = file.readline().strip()
                # 如果第一行不是空的
                if first_line:
                    # 获取第一个数字（假设第一个数字之前没有其他非数字字符）
                    first_number = first_line.split()[0]
                    # 如果第一个数字是数字
                    if first_number.isdigit():
                        # 统计该数字的出现次数
                        first_number_counts[first_number] += 1

# 打印统计结果
for number, count in first_number_counts.items():
    print(f"数字 {number} 出现了 {count} 次。")

print(f"空文件的数量：{empty_files_count}")
