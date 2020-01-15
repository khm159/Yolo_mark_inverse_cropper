
import os
import cv2
from PIL import Image, ImageTk
import numpy
import datetime

input_path = './input' 
output_path = './output'

def get_img_shape(path):
    img = cv2.imread(path)
    try:
        return img.shape
    except AttributeError:
        print('error! ', path)
        return (None, None, None)

def findlinenum(line): #find class id 
    if line == '':
        return ' '
    return line[0]  
    
def openfile(tag_name, jpg_name): #file load and processing
    openpath_tag = input_path+'/'+ tag_name
    openpath_jpg = input_path+'/'+ jpg_name

    pure_image_name = os.path.splitext(jpg_name)
    pure_txt_name = os.path.splitext(tag_name)

    
    f = open(openpath_tag,'r')
    i = 0
    while True:
        if pure_txt_name != pure_txt_name : continue
        
        line = f.readline()
        if not line: break
        classnum = findlinenum(line)
        print('input image : ' + openpath_jpg)
       
       
    
        #load original coordinates
        ox=float(line[2:10]) #yolov3 transformed point of middle of x
        oy=float(line[11:19]) #ylolv3 transformed point of middle of y
        ow=float(line[20:28]) #yolov3 transformed point of width
        oh=float(line[29:38]) #yolov3transformed point of height

        #load original image imformation
        img = Image.open(openpath_jpg)
        w_tot,h_tot = img.size

    
        #inverse transform
        x = ox*w_tot
        y = oy*h_tot
        w = ow*w_tot
        h = oh*h_tot

        #calculate inverse roi coordinates
        x_max = int(((2*x)+w)/2.0)
        x_min = int(x_max - w)
        y_max = int(((2*y)+h)/2.0)
        y_min = int(y_max - h)

        #Cropping
        crop_img = img.crop((x_min,y_min,x_max,y_max))
        
        #convert pil format to opencv format
        opencv_crop = numpy.array(crop_img)
        opencv_crop = opencv_crop[:, :, ::-1].copy()
        
        #save images
        new_path = os.path.splitext(jpg_name)
           
        savepath = './output/'+classnum+'_'+new_path[0]+'_'+str(i)+'.jpg'
        i= i+1
        print ('saved : '+savepath+'\n')
        cv2.imwrite(savepath,opencv_crop)

        
    f.close

def sorting(l1, l2):
        if l1 > l2:
            lmax, lmin = l1, l2
            return lmax, lmin
        else:
            lmax, lmin = l2, l1
            return lmax, lmin



listofall = os.listdir(input_path)
listofjpg = [file for file in listofall if file.endswith(".jpg") or file.endswith(".JPG")]
listoftag = [file for file in listofall if file.endswith(".txt") or file.endswith(".TXT")]

for i in range(len(listofjpg)):
    openfile(listoftag[i],listofjpg[i])




