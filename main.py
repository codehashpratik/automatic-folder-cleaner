import os

def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folderName, files):
     for file in files:
         os.replace(file, f"{folderName}/{file}")        

files=os.listdir()
files.remove("main.py") 
createIfNotExist("images") 
createIfNotExist("media")
createIfNotExist("docs")   
createIfNotExist("others")
imgexts = [".jpg",".png",".jpeg"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgexts] 
docexts = [".docx",".txt",".pdf",".xls","doc"]
doc = [file for file in files if os.path.splitext(file)[1].lower() in docexts] 
mediaexts=[".mp3",".mp4",".mkv",".3gp",".avi"]
medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaexts]
others =[]
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in mediaexts) and(ext not in imgexts) and (ext not in docexts) and os.path.isfile(file):
        others.append(file)
        
move("images", images)
move("media", medias)
move("docs", doc)
move("others", others)

