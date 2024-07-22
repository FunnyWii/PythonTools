import os
import cv2
import xml.etree.ElementTree as ET
import shutil

def visualize_and_save(image_folder, xml_folder, output_folder):
    # 创建输出文件夹
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历图像文件夹
    for image_file in os.listdir(image_folder):
        if image_file.endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(image_folder, image_file)

            # 生成对应的XML文件路径
            xml_file = os.path.splitext(image_file)[0] + '.xml'
            xml_path = os.path.join(xml_folder, xml_file)

            # 检查XML文件是否存在
            if os.path.exists(xml_path):
                # 解析XML文件
                tree = ET.parse(xml_path)
                root = tree.getroot()

                # 读取图像
                image = cv2.imread(image_path)
                print("Working on " + str(image_path))
                # 在图像上绘制标注框
                for obj in root.findall('object'):
                    bndbox = obj.find('bndbox')
                    xmin = int(bndbox.find('xmin').text)
                    ymin = int(bndbox.find('ymin').text)
                    xmax = int(bndbox.find('xmax').text)
                    ymax = int(bndbox.find('ymax').text)

                    
                    label = str(obj.find('name').text)

                    cv2.putText(image,str(label),(xmin-5,ymin-5),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),1)
                    cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)

                # 保存可视化结果
                output_path = os.path.join(output_folder, image_file)
                cv2.imwrite(output_path, image)

if __name__ == "__main__":
    # 指定图像文件夹、XML文件夹和输出文件夹
    image_folder = "/home/funnywii/Documents/TempDataset/7.5/img3"
    xml_folder = "/home/funnywii/Documents/TempDataset/7.5/xml3"
    output_folder = "/home/funnywii/Documents/TempDataset/visfinal"

    os.makedirs(output_folder, exist_ok=True)

    # 调用函数进行可视化并保存
    visualize_and_save(image_folder, xml_folder, output_folder)
