import cv2
import sys,os
import xml.etree.ElementTree as ET
import numpy as np
print(os.listdir())
cat = []
dirs = os.listdir()
for i in os.listdir():
    
    cat.append(''.join(list(filter(lambda x: x.isalpha(),i))))
cat = list(set(cat))
cat.remove('dataloadpy')
cat.remove('group')
images = []
lables = []
bounding_box = []
def get_coords(path):
    root = ET.parse(path).getroot()
    bbt = ['xmax','xmin','ymax','ymin']
    bbx = []
    for i in bbt:
        val = root.find('object/bndbox/'+i)
        bbx.append(int(val.text))
    return bbx
def get_label(cat,lbl_list):
    one_hot = np.zeros(len(lbl_list))
    one_hot[lbl_list.index(cat)] = 1
    return one_hot
print(get_label('car',cat))
    
    
get_coords(dirs[0]+'/000001.xml')
