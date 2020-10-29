import os
print '''To read the program file of question type "1"
            To append(change) the program file of question type "2"
            To read the answer of the choosen question type "3"
            To Logout successfully type "4"'''
            # Execution of user function
            # Question program file must be created before execution
            while True:
                b=int(raw_input("Enter your appropiate choise from above"))
                if b==1:
                    if os.path.isfile("Questions program file.txt"):
                        fobj=open("Questions program file.txt","r")
                        while True:
                            str=fobj.readline()
                            print str
                            if not str:
                                break
                    else:
                        print "File does not exit"
                if b==2:
                    print "If you want to change the data of the file,go to the source file and edit it"
                if b==3:
                    if os.path.isfile("answerkey.txt"):
                        fobj=open("answerkey.txt","r")
                        while True:
                            str=fobj.readline()
                            print str
                            if not str:
                                break
                if b==4:
                    print "Successfully logout"
                    break
