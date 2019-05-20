'''
Dataloader.py
'''
import cv2
import sys,os
import xml.etree.ElementTree as ET
import numpy as np
print(os.listdir())

'''
Gets the coordinates of the bounding box of the object
returns the bounding box
'''
def get_coords(path):
    #gets the XML source
    root = ET.parse(path).getroot()
    #different required data params for bbox
    bbt = ['xmax','xmin','ymax','ymin']
    bbx = []
    #extract all the data
    for i in bbt:
        val = root.find('object/bndbox/'+i)
        bbx.append(int(val.text))
    return bbx

'''
Returns the one hot encoded label list as a numpy array
'''
def get_label(cat,lbl_list):
    #extract text based label from folder name
    clean_cat =''.join(list(filter(lambda x: x.isalpha(),cat)))
    #create onehot 0s array
    one_hot = np.zeros(len(lbl_list))
    #set index to 1
    one_hot[lbl_list.index(clean_cat)] = 1
    #return one hot array
    return one_hot
'''
This is the function that should be called to extract the data
Returns bounding box coordinates, labels, and actual images of all
data points in that order
'''
def proc():
    #cat stores the possible text based categories
    cat = []
    #all folders
    dirs = os.listdir()
    #iterate through all folders and extract text labels
    for i in os.listdir():
        cat.append(''.join(list(filter(lambda x: x.isalpha(),i))))
    #remove redundancies and unnecessary files
    cat = list(set(cat))
    cat.remove('dataloadpy')
    dirs.remove('dataload.py')
    #storage images, labels, bbs lists
    images = []
    labels = []
    bbs = []
    #for every folder in directory 
    for folder in dirs:
        files = os.listdir(folder)
        files = [i[:-4] for i in files if i.endswith('.xml')]
        for file in files:
            images.append(cv2.imread(folder+'/'+file+'.jpg'))
            labels.append(get_label(folder,cat))
            bbs.append(get_coords(folder+'/'+file+'.xml'))
            
    return bbs,labels,imgs
if __name__ == '__main__':
    proc()
