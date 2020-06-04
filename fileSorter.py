import os
import shutil

#It is very important to add "/" at the end of the path.
#For exemple : /Users/user/Desktop/folder_name/

path = input("Path:")
names = os.listdir(path)
folder_name = ["pdf","pages","key","doc","docx","css","html","javaScript","exel","php","jpg","png","mp4"]

for x in range(0,13):
    if not os.path.exists(path + folder_name[x]):
        os.makedirs(path + folder_name[x])

for files in names :
    if ".pdf" in files and not os.path.exists(path + "pdf/" + files):
        shutil.move(path + files, path + "pdf/" + files)
    if ".pages" in files and not os.path.exists(path + "pages/" + files):
        shutil.move(path + files, path + "pages/" + files)
    if ".key" in files and not os.path.exists(path + "key/" + files):
        shutil.move(path + files, path + "key/" + files)
    if ".doc" in files and not os.path.exists(path + ".doc/" + files):
        shutil.move(path + files, path + "doc/" + files)
    if ".docx" in files and not os.path.exists(path + "docx/" + files):
        shutil.move(path + files, path + "docx/" + files)
    if ".css" in files and not os.path.exists(path + "css/" + files):
        shutil.move(path + files, path + "css/" + files)
    if ".html" in files and not os.path.exists(path + "html/" + files):
        shutil.move(path + files, path + "html/" + files)
    if ".js" in files and not os.path.exists(path + "javaScript/" + files):
        shutil.move(path + files, path + "javaScript/" + files)
    if ".xsl" in files and not os.path.exists(path + "exel/" + files):
        shutil.move(path + files, path + "exel/" + files)
    if ".xslb" in files and not os.path.exists(path + "exel/" + files):
        shutil.move(path + files, path + "exel/" + files)
    if ".xslm" in files and not os.path.exists(path + "exel/" + files):
        shutil.move(path + files, path + "exel/" + files)
    if ".xslx" in files and not os.path.exists(path + "exel/" + files):
        shutil.move(path + files, path + "exel/" + files)
    if ".php" in files and not os.path.exists(path + "php/" + files):
        shutil.move(path + files, path + "php/" + files)
    if ".JPG" in files and not os.path.exists(path + "jpg/" + files):
        shutil.move(path + files, path + "jpg/" + files)
    if ".jpg" in files and not os.path.exists(path + "jpg/" + files):
        shutil.move(path + files, path + "jpg/" + files)
    if ".jpeg" in files and not os.path.exists(path + "jpg/" + files):
        shutil.move(path + files, path + "jpg/" + files)
    if ".png" in files and not os.path.exists(path + "png/" + files):
        shutil.move(path + files, path + "png/" + files)
    if ".mp4" in files and not os.path.exists(path + "mp4/" + files):
        shutil.move(path + files, path + "mp4/" + files)
for y in range(0,13):
    if len(os.listdir(path + folder_name[y])) == 0:
        shutil.rmtree(path + folder_name[y])
