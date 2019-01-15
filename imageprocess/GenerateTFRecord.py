import os
from PIL import Image
import numpy as np
import shutil

# 提取folder_path下所有文件路径返回list
def getAllFileName(folder_path):
    file_list = []
    for filename in os.listdir(folder_path):
        if(filename[-4:]=='.png'):
            file_list.append(filename)
    return file_list

# 补全新标定的图片
def imageCompletion():
    folder_path1 = '/Users/ziv/Desktop/ziv/第二次标记文件/road/train_labels1'
    folder_path2 = '/Users/ziv/Desktop/ziv/第二次标记文件/road/train_labels2'
    file_name_list1 = getAllFileName(folder_path1)
    file_name_list2 = getAllFileName(folder_path2)
    for file_name in file_name_list1:
        if(not file_name_list2.__contains__(file_name)):
            shutil.copyfile(folder_path1+'/'+file_name, folder_path2+'/'+file_name)

# 转化成灰度图，背景为0，洞为1，其他为255
def pixelValueTrans():
    folder_path1='/Users/ziv/Desktop/ziv/第二次标记文件/road/train_labels2'
    folder_path2 = '/Users/ziv/Desktop/ziv/第二次标记文件/road/标注_0_1_255'
    file_name_list=getAllFileName(folder_path1)
    for file_name in file_name_list:
        img = np.array(Image.open(folder_path1+'/'+file_name))
        w=img.shape[0]
        h=img.shape[1]
        c=img.shape[2]
        img2=np.zeros((w,h))
        for i in range(w):
            for j in range(h):
                if(img[i,j,1]==50):
                    img2[i,j]=255
                elif(img[i,j,1]==0):
                    img2[i, j] = 1
                else:
                    img2[i,j]=0
        img2=Image.fromarray(img2.astype('uint8')).convert("L")
        img2.save(folder_path2+'/'+file_name)

def resizeAll():
    folder_path1 = '/Users/ziv/Desktop/ziv/第二次标记文件/road/train1'
    folder_path1 = '/Users/ziv/Desktop/ziv/第二次标记文件/road/标注_0_1_255'
    file_name_list=getAllFileName(folder_path1)
    for file_name in file_name_list:
        img = Image.open(folder_path1+'/'+file_name)
        img=img.resize((512,512))
        img.save(folder_path1+'/'+file_name)


def transposeAll():
    folder_path1 = '/Users/ziv/Desktop/项目/道路破损识别/data/road/mask'
    file_name_list=getAllFileName(folder_path1)
    for file_name in file_name_list:
        img = Image.open(folder_path1+'/'+file_name)
        img=img.transpose(Image.FLIP_LEFT_RIGHT)
        img.save(folder_path1+'/'+file_name[:-4]+'_lr.png')

def renameAll():
    folder_path1 = '/Users/ziv/Desktop/ziv/第二次标记文件/road/mask'
    file_name_list=getAllFileName(folder_path1)
    file_name_list.sort()
    index=0
    for file_name in file_name_list:
        img = Image.open(folder_path1+'/'+file_name)
        img.save(folder_path1+'/'+str(index)+'.png')
        index+=1

def indexGenerate():
    fw1=open('/Users/ziv/Desktop/ziv/第二次标记文件/road/index/train.txt',mode='w' ,encoding='UTF-8')
    fw3=open('/Users/ziv/Desktop/ziv/第二次标记文件/road/index/val.txt',mode='w' ,encoding='UTF-8')
    for i in range(309):
        if(i<260):
            fw1.write(str(i)+'\r\n')
        else:
            fw3.write(str(i) + '\r\n')
    fw1.close()
    fw3.close()



if __name__=="__main__":
    indexGenerate()
    print("god")