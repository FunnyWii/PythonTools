import os
import xml.etree.ElementTree as ET
from collections import defaultdict
import imghdr
import glob
# 本程序不应该修改文件夹中的任何内容，只做统计用
# 统计 XML 文件中共有几种类别，及其该类别的数量
output_file = 'static.txt'

def count_xml_names(folder_path):
    # 创建一个默认字典来存储<name>标签中的内容和对应的数量
    name_counts = defaultdict(int)

    # 获取文件夹内所有的xml文件路径
    xml_file_paths = [f for f in os.listdir(folder_path) if f.endswith('.xml')]
    with open(output_file, 'w') as f:

        # 遍历xml文件路径
        for xml_path in xml_file_paths:
            # 打开xml文件
            tree = ET.parse(os.path.join(folder_path, xml_path))
            root = tree.getroot()

            # 查找并统计<name>标签中的内容
            for name_elem in root.iter('name'):
                name = name_elem.text.strip()
                f.write(f"{name},\n")
                name_counts[name] += 1

    return dict(name_counts)

# 查看 IMG 文件夹中的图像为真实 JPG 格式的图片数量，以及其他格式的数量。
def gain_true_format(image_path):
    format_counts = defaultdict(int)
    file_paths = glob.glob(os.path.join(image_path, '*'))
    for i, file_path in enumerate(file_paths):
        # 获取文件名和拓展名
        filename, extension = os.path.splitext(file_path)
        imgType = imghdr.what(filename+extension)
        if imgType is not None:
            if imgType == 'jpg' or imgType == 'jpeg':
                format_counts['jpg'] += 1
            else:
                format_counts['other'] += 1
        else:
            print('The UNKNOWN format file is :'+filename+extension)
            format_counts['unknown'] += 1
    return format_counts        

# 指定文件夹路径
folder_path = '/media/funnywii/47CCF48AB06977A3/DATASET/TrashDet/南通实习生/wx/xml'
image_path = '/media/funnywii/47CCF48AB06977A3/DATASET/TrashDet/南通实习生/wx/img'

# 调用函数统计<name>标签中内容的数量
result = count_xml_names(folder_path)
format_result = gain_true_format(image_path)

# 打印结果
temp = 0
print("Static Results for" + str(folder_path))
print('The class static data: ')
for name, count in result.items():
    print(f'{name}: {count}')
    temp += count
print(temp) 
print('------------------------------------')
print('The file format static data: ')
for name, count in format_result.items():
    print(f'{name}: {count}')
