'''
    Here we parse the labeled info to the csv
'''

import pandas as pd
import xml.etree.ElementTree as xet
from glob import glob

# get all the image xml path
path = r'E:\YOLO-ALPD\Notebook\data\images_labeled'
xml_paths = glob(path+"/*.xml")

data = []

for xml_file in xml_paths:
    tree = xet.parse(xml_file)
    root = tree.getroot()
    
    
    filename = root.find('filename').text
    objects = root.findall('object')
    
    for obj in objects:
        label = obj.find('name').text
        xmin = int(obj.find('bndbox').find('xmin').text)
        ymin = int(obj.find('bndbox').find('ymin').text)
        xmax = int(obj.find('bndbox').find('xmax').text)
        ymax = int(obj.find('bndbox').find('ymax').text)
        data.append(
            [filename, label, xmin, ymin, xmax, ymax]
        )
        
df = pd.DataFrame(
    data=data,
    columns=["filename", "label", "xmin", "ymin", "xmax", "ymax"]
)

df.to_csv(r'E:\YOLO-ALPD\Notebook\data\labeled_data.csv', index=False)

print("CSV file has been created successfully.")

