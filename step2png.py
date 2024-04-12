import os
import time



"""

this part create the 2 repo STEP and PNG where the files are moved after being converted

"""
main_repo = os.getcwd()        
          
try:           
    os.chdir('OUT')      
except FileNotFoundError:          
    os.mkdir('OUT')
OUT_repo = os.getcwd()
os.chdir(main_repo)        
try:           
    os.chdir('IN')
except FileNotFoundError:
    os.mkdir('IN')
    os.chdir('IN')
IN_repo = os.getcwd()
files = os.listdir() 
for file in files:
    try:
        name,ext = file.split(".")
        if ext == 'step':
            new_file = name + '.png'
            print("converting "+name)
            time.sleep(0.2)
            os.rename(IN_repo+'\\'+file,OUT_repo+'\\'+new_file)
            os.chdir(main_repo)

        elif ext == 'png':
            new_file = name + '.step'
            print("converting "+name)
            time.sleep(0.2)
            os.rename(IN_repo+'\\'+file,OUT_repo+'\\'+new_file)
            os.chdir(main_repo)
            
    except ValueError:
        pass