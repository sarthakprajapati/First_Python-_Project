#Welcome Message
def Welcome():
    x=raw_input("\n \t \t  WELCOME \n \n \n \n \n \n \t \t \t \t \t \t ENTER ANY KEY... TO CONTINUE")
    mainscreen()
    
#mainscreen
def mainscreen():
    import os
    os.system('clear') 
    print("\n \t \t \t MAIN SCREEN \n 1.ADD RECORD \n 2.READ RECORD \n 3.EXIT\n\t\t ")

   #input file name
def filename():
    filename=raw_input("\n \t >>> Enter file name \n\n\t ")
    return filename
  #open file in read mode 
def readmode(filename):
    f1=open(filename,'r+')
    return f1
  #open file in append mode
def amode(filename):
    f1=open(filename,'a+') 
    return f1

def controller():
    x=int(raw_input())
    if x==1:
        f=filename()
        f=amode(f)
        addrecord(f)
    elif x==2:
        f=filename()
        f=readmode(f)
        readrecord(f)    
    elif x==3 :
        import os
        os.system('clear')     
    else:
        print "WRONG CHOICE!! " 
        
   #add record
def addrecord(f1):
        line=raw_input("Enter data \n\n\t ")
        f1.write(line)
        f1.close()
        choice=raw_input("\n \n \t DO YOU WANT TO CONTINUE ?  \n \t 1-YES \n \t 2-NO\n\n\t")
        choice=int(choice)
        if choice==1:
           f1=addrecord(amode(filename()))
        else:
            import os
            os.system('clear') 
            mainscreen() 
            controller()

def readrecord(f):
    x=f.read()
    print x
                 
#CONTROLLER
Welcome()
controller()
   
