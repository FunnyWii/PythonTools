import os
import xml.etree.ElementTree as ET

# 定义一个函数来转换XML标注到YOLO格式
def xml_to_yolo(xml_path, width, height):
    # 解析XML文件
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # 初始化YOLO格式的标注列表
    yolo_annotations = []

    # 遍历每个对象
    for obj in root.findall('object'):
        # 获取对象名称
        name = obj.find('name').text
        # 获取边界框坐标
        bbox = obj.find('bndbox')
        xmin = int(bbox.find('xmin').text)
        ymin = int(bbox.find('ymin').text)
        xmax = int(bbox.find('xmax').text)
        ymax = int(bbox.find('ymax').text)
        if name == 'Use_AC':
            label = 0
        elif name == 'Non_AC':
            label = 1
        # 计算YOLO格式的坐标
        x_center = (xmin + xmax) / 2.0 / width
        y_center = (ymin + ymax) / 2.0 / height
        w = (xmax - xmin) / width
        h = (ymax - ymin) / height

        # 添加到YOLO格式的标注列表
        yolo_annotations.append(f"{label} {x_center:.6f} {y_center:.6f} {w:.6f} {h:.6f}")

    return yolo_annotations

# 指定包含XML文件的源文件夹路径
src_folder_path = '/home/funnywii/Documents/TempDataset/AC/0530/xml'

# 指定保存YOLO格式标注的目标文件夹路径
dst_folder_path = '/home/funnywii/Documents/TempDataset/AC/0530/txt'

# 确保目标文件夹存在
os.makedirs(dst_folder_path, exist_ok=True)

# 遍历源文件夹内的所有文件
for filename in os.listdir(src_folder_path):
    # 检查文件是否为XML文件
    if filename.endswith('.xml'):
        # 构建源文件和目标文件的完整路径
        src_file_path = os.path.join(src_folder_path, filename)
        dst_file_path = os.path.join(dst_folder_path, os.path.splitext(filename)[0] + '.txt')

        # 解析XML文件以获取图像尺寸
        tree = ET.parse(src_file_path)
        root = tree.getroot()
        size = root.find('size')
        width = int(size.find('width').text)
        height = int(size.find('height').text)

        # 转换XML标注到YOLO格式
        yolo_annotations = xml_to_yolo(src_file_path, width, height)

        # 保存YOLO格式的标注到目标文件
        with open(dst_file_path, 'w') as f:
            for annotation in yolo_annotations:
                f.write(f"{annotation}\n")

print(f"所有XML文件已转换为YOLO格式并保存到 {dst_folder_path} 文件夹中。")
