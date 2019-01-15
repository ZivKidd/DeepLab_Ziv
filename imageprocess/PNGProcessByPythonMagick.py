import PythonMagick
import os

# 提取folder_path下所有文件路径返回list
def getAllFileName(folder_path):
    file_list = []
    for filename in os.listdir(folder_path):
        if(filename[-4:]=='.png'):
            file_list.append(filename)
    return file_list

folder_path1=r"\\Mac\Home\Desktop\ziv\第二次标记文件\road\mask"
file_name_list=getAllFileName(folder_path1)
for file_name in file_name_list:
    image = PythonMagick.Image(folder_path1+'\\'+file_name)
    image.magick('PNG')
    image.write(folder_path1+'\\'+file_name)

