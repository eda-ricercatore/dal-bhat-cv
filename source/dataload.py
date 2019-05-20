import cv2
import sys,os
import xml.etree.ElementTree as ET
import numpy as np
print(os.listdir())


def get_coords(path):
    root = ET.parse(path).getroot()
    bbt = ['xmax','xmin','ymax','ymin']
    bbx = []
    for i in bbt:
        val = root.find('object/bndbox/'+i)
        bbx.append(int(val.text))
    return bbx
def get_label(cat,lbl_list):
    clean_cat =''.join(list(filter(lambda x: x.isalpha(),cat)))
    one_hot = np.zeros(len(lbl_list))
    one_hot[lbl_list.index(clean_cat)] = 1
    return one_hot

def proc():
    cat = []
    dirs = os.listdir()
    for i in os.listdir():
    
        cat.append(''.join(list(filter(lambda x: x.isalpha(),i))))
    
    cat = list(set(cat))
    cat.remove('dataloadpy')
    dirs.remove('dataload.py')
    images = []
    labels = []
    bbs = []
    
    
    for folder in dirs:
        files = os.listdir(folder)
        files = [i[:-4] for i in files if i.endswith('.xml')]
        for file in files:
            images.append(cv2.imread(folder+'/'+file+'.jpg'))
            labels.append(get_label(folder,cat))
            bbs.append(get_coords(folder+'/'+file+'.xml'))
            print(bbs,labels)
    return bbs,labels,imgs
proc()
