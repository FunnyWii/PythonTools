import os
#修改文件后缀

def change_file_extension(folder_path, old_extension, new_extension):
    # 遍历文件夹中的文件
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # 判断是否为文件
        if os.path.isfile(file_path):
            # 检查文件后缀
            _, file_ext = os.path.splitext(filename)
            if file_ext == old_extension:
                # 构建新的文件路径
                new_filename = os.path.splitext(filename)[0] + new_extension
                new_file_path = os.path.join(folder_path, new_filename)

                # 重命名文件
                os.rename(file_path, new_file_path)
                print(f'Renamed: {filename} -> {new_filename}')

if __name__ == "__main__":
    folder_path = '/media/funnywii/47CCF48AB06977A3/DATASET/TrashDet/南通实习生/sxw/img'
    old_extension = '.JPG'  # 旧的文件后缀
    new_extension = '.jpg'  # 新的文件后缀

    change_file_extension(folder_path, old_extension, new_extension)
