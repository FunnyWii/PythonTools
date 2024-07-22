import os
import glob
import xml.etree.ElementTree as ET

# 将文件夹内 xml 文件的 <filename> **** </filename> 修改为对应的 IMG 文件名
def update_xml_filenames(folder_path):
    # 获取文件夹内所有的xml文件路径
    xml_file_paths = glob.glob(os.path.join(folder_path, '*.xml'))

    # 遍历xml文件路径
    for xml_path in xml_file_paths:
        # 打开xml文件
        tree = ET.parse(xml_path)
        root = tree.getroot()

        # 获取文件名（不包含拓展名）
        filename = os.path.splitext(os.path.basename(xml_path))[0]

        # 修改<filename>标签的内容
        filename_elem = root.find('filename')
        filename_elem.text = f'{filename}.jpg'

        # 保存修改后的xml文件
        tree.write(xml_path)

# 将xml文件中的<name>cig_butt</name> 统一修改为 trash
def modify_class_name(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    for name_element in root.iter('name'):
        name_element.text = 'trash'

    tree.write(file_path)

def process_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.xml'):
            file_path = os.path.join(folder_path, filename)
            modify_class_name(file_path)

# 指定文件夹路径
folder_path = '/home/funnywii/Documents/TrashDetTemp/label'

# 调用函数进行xml文件内容修改
update_xml_filenames(folder_path)
# process_folder(folder_path)