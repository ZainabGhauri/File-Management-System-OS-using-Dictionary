

import collections
import os
import shutil
import json

#name of dir
log = [0]
#name of files
log2 = [0]
#size of files
log3 = [0]
d={}
def menu(option):
    
    if option == 1: #select option 7 to map the memory
        Create()
    elif option == 2:             #incase an invalid option is selected
        Open()
    elif option == 3:             #incase an invalid option is selected
        Write()
    elif option == 4:
        Read()
    elif option == 5:
        DeleteFile()
    elif option == 6:
        show_Memory_Map()
    elif option == 7:
        makeDir()
    elif option == 8:
        changeDir()
    elif option == 9:
        size()
    elif option == 10:
        Truncate()
        



def Create():

    directory_name= input("Enter directory name you want to create:")
    file_name= input("Enter file name you want to create:")
    file_type= input("Enter file type you want to create:")
     # Changing and adding Dictionary Elements
     
    if os.path.exists(file_name):
        print(" This File Already Exist ")
        print(" SORRY TRY AGAIN !!! ")
    else:
        
         
          if directory_name in d:
            d[directory_name]['name'].append(file_name)
            d[directory_name]["type"].append(file_type)
          else:
            d[directory_name] = {}
            d[directory_name]['name'] = [file_name]
            d[directory_name]['type'] = [file_type]

            
        
        
     
     # print(d)

    full_file_name = os.path.join(file_name, file_type)  
    with open(file_name, 'w') as file:
        json.dump(d,file)
        
    print(f"File '% s' created" % full_file_name)
    if directory_name in log:
            log2.append(file_name)
            size = os.path.getsize(file_name)
            log3.append(size)
            size = 0
    else:
            log.append(directory_name)
            log2.append(file_name)
            size = os.path.getsize(file_name)
            log3.append(size)
            size = 0
     
         
def Open():
     file_name= input("Enter file name you want to Open:")
     file_type= input("Enter file type you want to Open:")
     f = open(file_name, "r")
     return file_name
   
    
def Truncate():
    dir_name = input("Enter dir :")
    file_name= input("Enter file name you want to Open:")
    file_size= input("Enter file size you want to truncate:")
    size = os.path.getsize(file_name)
    if size in log3:
        log3.remove(size)
        log3.append(file_size)

    
def size():
    x = Open()
    size = os.path.getsize(x) 
    print('Size o1 f file is', size, 'bytes')

    
def show_Memory_Map():
    print("Name of Directories \n")
    print(d)
    print("\n")
    print("Name of Files \n")
    print(log2)
    print("Size of Files \n")
    print(log3)
    
def Write():
    file_name =  Open()
    option = input("If you want to append enter 'a' , If you want to write enter 'w' ")
    if(option=='a'):
         text= input("what do you want to write     :")
         f = open(file_name, "a")
         f.write("\n")
         f.write(text)
         f.close()
            
    elif option=='w':
         text= input("what do you want to write   :")
         f = open(file_name, "w")
         f.write("\n")
         f.write(text)
         f.close()
   


def Read():
    file_name = Open()
    print("Reading from the file %s" %file_name)    
    file1 = open(file_name, 'r')
    print(file1.read())
   
def DeleteFile():
    dir_name = input("Enter The Name of dir file is in you want to delete:")
    file_name = input("Enter The Name of file you want to delete:")
    for x in d:
         if dir_name==x:
            d[dir_name]['name']=None
            d[dir_name]['type']=None
            log2.remove(file_name)
            size = os.path.getsize(file_name)
            log3.remove(size)
            
        
         else:
           print("The file does not exist")
        
        
def makeDir():
       dirt_name=input("Enter the name of directory you want to create:")
       print(d)
       exists=False
       for x in d:
         if dirt_name==x:
           exists=True
           print("This directory is already created!!!")
           break
       if(exists==False):
           d[dirt_name]=d
           print("This directory is created!!!")
       print(d)


def changeDir():    

       file_name=input("Enter the name of the file you want to change directory of:")
       dir_name=input("Enter the name of the dir it is in:")
       dir_name2=input("Enter the name of the dir you want to move to:")
       for x in d:
          if dir_name==x:
            d[dir_name]['name'] = ''
            typez=d[dir_name]['type']
            d[dir_name]['type'] = ''
            d[dir_name2] = {}
            d[dir_name2]['name'] = file_name
            d[dir_name2]['type'] = typez
            print("The directory is changed!!!")
       print(d)

     
          
def truncate():
   
        truncate_name=input("Enter the name of the file you want to truncate:")
        truncate_size=input("Enter the size:")
        truncate_file(truncate_name,truncate_size)
        
if __name__ == '__main__':
   

    # printing the menu
    while(1):
        print("File Manager\n"+
              "Select any option:\n"
              "1. Create File\n"
              "2. Open File \n"
              "3. Write to file \n"
              "4. Read from file \n"
              "5. Delete file \n"
              "6. Show memory map \n"
              "7. Create Directory \n"
              "8. Change Directory \n"
              "9. Get Size of The file \n"
              "10.Truncate \n"
              "0: Quit Program\n ")
        # getting the option of the user
        option = int(input("Enter a number: "))

        # calling menu function to further run the program
        menu(option)
