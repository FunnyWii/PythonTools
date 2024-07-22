import os
import xml.etree.ElementTree as ET

# 找到XML文件内的name字段，修改其中错别字

def modify_xml_files(directory, old_value, new_value):
    for filename in os.listdir(directory):
        if filename.endswith(".xml"):
            file_path = os.path.join(directory, filename)
            tree = ET.parse(file_path)
            root = tree.getroot()
            for name in root.iter('name'):
                if name.text == old_value:
                    name.text = new_value
                    # print("The outlier file is  " + file_path)
            tree.write(file_path)

# 调用函数，将包含特定字段值的XML文件中的字段值修改为新的值
old_value = 'use-AC'
new_value = 'Use_AC'
folder_path = '/home/funnywii/Documents/TempDataset/AC/0530/xml'

modify_xml_files(folder_path, old_value, new_value)