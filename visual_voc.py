import os
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.colors as mcolors
from PIL import Image


# 可视化图像及对应标注（VOC格式）
def visualize_voc_annotations(image_folder, annotation_folder, output_folder):
    image_files = os.listdir(image_folder)
    annotation_files = os.listdir(annotation_folder)
    color_palette = {
        'green straight': (0, 255, 0),
        'red straight': (255, 0, 0),
        'yellow straight': (255, 255, 0),
        'green left': (0, 255, 0),
        'red left': (255, 0, 0),
        'yellow left': (255, 255, 0),
        'green right': (0, 255, 0),
        'red right': (255, 0, 0),
        'yellow right': (255, 255, 0),
        'unknown': (0, 0, 0)  # 黑色
    }    
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        annotation_file = image_file.replace('.jpg', '.xml')
        annotation_path = os.path.join(annotation_folder, annotation_file)
        print('Working on ' + annotation_file)
        # 加载图像
        image = Image.open(image_path)
        plt.imshow(image)

        # 加载标注文件
        tree = ET.parse(annotation_path)
        root = tree.getroot()

        # 解析标注文件
        for obj in root.findall('object'):
            # 获取边界框坐标
            bbox = obj.find('bndbox')
            xmin = int(bbox.find('xmin').text)
            ymin = int(bbox.find('ymin').text)
            xmax = int(bbox.find('xmax').text)
            ymax = int(bbox.find('ymax').text)

            label = obj.find('name').text
            # print(label)
            color = color_palette.get(label, (255, 0, 0))  # 默认为红色
            color_normalized = (color[0] / 255, color[1] / 255, color[2] / 255)
            # 创建矩形框
            rect = patches.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin,
                                     linewidth=0.8, edgecolor=color_normalized, facecolor='none')

            # 添加矩形框到图像
            plt.gca().add_patch(rect)

            # 添加标签
            plt.text(xmin, ymin - 5, label, color=color_normalized)

        # 保存可视化结果
        output_file = image_file.replace('.jpg', '_annotated.jpg')
        output_path = os.path.join(output_folder, output_file)
        plt.axis('off')
        # plt.savefig(output_path)
        plt.savefig(output_path, bbox_inches='tight', pad_inches=0)
        # plt.savefig(output_path, dpi=150, bbox_inches='tight', pad_inches=0)
        plt.close()

# 指定图像文件夹、标注文件夹和输出文件夹的路径
image_folder = '/home/funnywii/Documents/TempDataset/TempProcess/TACO/img'
annotation_folder = '/home/funnywii/Documents/TempDataset/TempProcess/TACO/xml'
output_folder = '/home/funnywii/Documents/TempDataset/TempProcess/TACO/VisResults'

# 创建输出文件夹，如果该文件夹不存在
os.makedirs(output_folder, exist_ok=True)

# 调用函数进行可视化并保存结果
visualize_voc_annotations(image_folder, annotation_folder, output_folder)
