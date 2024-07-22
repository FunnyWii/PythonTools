import os
# 计算当前文件夹内 存在几种文件扩展名以及对应文件数量
def count_file_extensions(directory):
    extension_count = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            extension = os.path.splitext(file)[1]
            if extension in extension_count:
                extension_count[extension] += 1
            else:
                extension_count[extension] = 1
    return extension_count

# Example usage
# directory_path = "path_to_your_directory"
# result = count_file_extensions(directory_path)
# print(result)

# The function is ready to use. Just provide the path to the directory you want to analyze.
directory_path = "/media/funnywii/47CCF48AB06977A3/DATASET/TrashDet/南通实习生/wx/img"
result = count_file_extensions(directory_path)
print(result)
