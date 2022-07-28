

import math
from os import listdir
from os.path import isfile, join
import json

# step 1 list all files infolder temp 
# read file 
# get the numbre of object 
# split file into multiple files 
def splitFile(nameFile):

     pathFile =  pathTempFolder+nameFile
     with open(pathFile) as f:
          content = f.read()
     products  = json.loads(content)

     nbProducts = len(products)
     maxProductPerFile = 200

     print(len(products))
     f.close()

     # write and split 
     nbFile = math.ceil(nbProducts/maxProductPerFile)
     for i in range(nbFile):
          newNameFile = pathTempFolder+nameFile.replace(".json","")+"_"+str(i)+".json"
          start = i*maxProductPerFile
          end = start + maxProductPerFile
          # start:end (end not included)
          file = open(newNameFile, "a")    
          data = json.dumps(products[start:end])
          file.write(data)
          file.close()

pathTempFolder = "/opt/lampp/htdocs/learn/bubeph/data/PROD/TEMP/"
onlyfiles = [f for f in listdir(pathTempFolder) if isfile(join(pathTempFolder, f))]


#nameFile = onlyfiles[1]
for pathFile in onlyfiles:     
     splitFile(pathFile)




