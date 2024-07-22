import os
import glob
import imghdr
from PIL import Image

# 一般 VOC 数据集图像的处理流程
# 1. 将 IMG 和对应标注 XML 修改名称,并指定扩展名。不过此阶段不能保证 PNG -> JPEG 能够正确转换为真 JPEG，仅能修改拓展名。
# 2. 修改 XML 文件中的 <filename> 标志 -> 对应文件名
# 3. 检查 xml 文件中出现的 class num
# 4. 可视化标注结果
# F. split


# 将 IMG 和 XML 文件修改为 Image.xxx 的格式。
def rename_files(folder_path, new_extension):
    # 获取指定文件夹内的所有文件路径
    file_paths = glob.glob(os.path.join(folder_path, '*'))
    # 对文件路径进行排序
    file_paths.sort()

    # 遍历文件路径
    for i, file_path in enumerate(file_paths):
        # 获取文件名和拓展名
        filename, extension = os.path.splitext(file_path)
        # 生成新的文件名
        new_filename =  f'{i}.{new_extension}'
        new_filename = "0530"+new_filename
        new_file_path = os.path.join(folder_path, new_filename)

        # 修改文件拓展名为指定格式
        print(filename + " ->> " + new_filename)
        os.rename(file_path, new_file_path)

# def convert_to_jpeg(image_folder):
#     # 获取文件夹中的所有文件
#     file_list = os.listdir(image_folder)
#     # 遍历文件夹中的每个文件
#     for file_name in file_list:
#         # 检查文件是否为图像文件
#         if file_name.endswith(('.jpg', '.jpeg', '.png', '.gif')):
#             # 构建图像文件的完整路径
#             file_path = os.path.join(image_folder, file_name)

#             # 打开图像文件
#             image = Image.open(file_path)
#             if image.mode == 'RGBA':
#                 image = image.convert('RGB')
#             # 将图像文件保存为JPEG格式
#             jpeg_path = os.path.splitext(file_path)[0] + '.jpg'
#             image.save(jpeg_path, 'JPEG')

#             # 关闭图像文件
#             image.close()

#             # 删除原始图像文件（可选）
#             os.remove(file_path)

# 指定文件夹路径和新的文件拓展名
# folder_path = '/home/funnywii/Documents/TempDataset/JPEGImages'
folder_path = '/home/funnywii/Documents/TempDataset/AC/0530/img'
new_extension = 'jpg'

# 调用函数进行文件重命名
rename_files(folder_path, new_extension)
# 调用函数进行格式转换
# if new_extension == 'jpg':
#     convert_to_jpeg(folder_path)