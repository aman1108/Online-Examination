# My Python Program "Online Examination"
import os
class online_examination:
    # Admin Function 
    def admin(self):
        self.Loginid=int(raw_input("Enter your seven digit username"))
        self.password=raw_input("Enter your password")
        #Authentification of admin
        if self.Loginid==1234567 and self.password=="password":
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
                # Successfully Logout from admin function
        else:
            print "Invalid username or password"       
class examination_time:
    def user(self):
            try:
                self.loginid=int(raw_input("Enter enrollment number"))
                self.password=int(raw_input("Enter you password"))
                # Authentification of user
            except ValueError:
                print "Invalid username or password"
            if self.loginid==11 and self.password==123:
                self.name=raw_input("Enter your name")
                if os.path.isfile("Instructions.txt"):
                    fobj=open("Instructions.txt","r")
                    while True:
                        str=fobj.readline()
                        print str
                        if not str:
                            break
                else:
                    print "File does not exit"
                # Starting of Examination
                self.start=raw_input("Enter start to continue examination") 
                if self.start=="start":
                        self.rightans=0
                        self.wrongans=0
                        self.count=0
                        # General Instructions to User
                        print '''To answer first Question type 1
                            To answer second question type 2
                            and so on.'''
                        print'''To check your answer sheet type "1000" in quesno'''
                        print '''To finish the exam type "0" in quesno'''
                        print ''' Instruction for answering
                                You have four options a,b,c,d
                                So answering must be done out of this four
                                If answer rather than that For example 'e','eg' etc then it will be disqualified
                                If you want to not answer type o(it is alphabet o not zero)'''
                        print '''If you have any doubt regarding anything call for examiner present in the lab'''
                        self.ans=["o"]*30 # Empty List For answer
                        self.file="" # Empty string for question
                        while True:
                            self.file=""
                            try:
                                self.quesno=raw_input("Enter your question no") # Asking User for Questions
                                print self.quesno
                                self.quesno_str=self.quesno
                                print self.quesno_str
                                if self.quesno=='0':
                                    break
                                elif self.quesno=='1000':
                                    print self.ans
                                elif int(self.quesno)<31:
                                    self.file=self.file+self.quesno_str+".txt" # Concatinating String
                                    if os.path.isfile(self.file):
                                        fobj=open(self.file,"r")
                                        while True:
                                            str=fobj.readline()
                                            print str
                                            if not str:
                                                break
                                    else:
                                        print "File does not exit"
                                    self.ques=int(self.quesno_str)
                                    self.ans[self.ques-1]=raw_input("Enter your answer")
                                    if self.ans[self.ques-1]<>'a' and self.ans[self.ques-1]<>'b' and self.ans[self.ques-1]<>'c' and self.ans[self.ques-1]<>'d' and self.ans[self.ques-1]<>'o':
                                        print "Please enter answer from a,b,c,d"
                                        print "Please read the instructions carefully"
                                        print "You can reenter your answer by again atempting your question"
                                        self.ans[self.ques-1]=0
                                else:
                                    print "wrong choise"
                            except ValueError:
                                print "Please Enter Question Number in range 0 to 30"
                        print self.ans
                else:
                    print "You have not started your exam"
            else:
                print "Invalid Username or passowrd"
class result_time(examination_time):
    def count_marks(self):
            if os.path.isfile("answerkey.txt"):
                        self.marks=0
                        self.inr=-1
                        self.rans=[ ] # Empty List for right answer
                        self.wans=[ ] # Empty List for wrong answer
                        self.nans=[ ] # Empty List for not answered question
                        fobj2=open("answerkey.txt","r")
                        var=0 
                        while var<31:
                            while True:
                                stra=fobj2.readline()
                                if not stra:
                                    break
                                stra=stra.split()
                                
                                for k in range(len(stra)):
                                    while self.inr<(len(self.ans)-1):
                                        self.inr=self.inr+1
                                        if stra[k]==self.ans[self.inr] and self.ans[self.inr]<>'o': 
                                            self.marks=self.marks+4
                                            self.rans.append(self.inr)
                                            break
                                        elif self.ans[self.inr]=='o': 
                                            self.marks=self.marks+0
                                            self.nans.append(self.inr)
                                            break
                                        else:
                                            self.marks=self.marks-1
                                            self.wans.append(self.inr)
                                            break
                            var=var+1
                        print "Student Name:",self.name
                        print "Enrollement Number: 11"
                        print '''1. To check correct Answers
                                 2. To check wrong Answers
                                 3. To check the Answers not marked
                                 4. To get final result
                                 5. To analysis your result
                                 6. To exit'''
                        while True:
                            y=int(raw_input("Enter your choise"))
                            if y==1:
                                if len(self.rans)==0:
                                    print "No question is answered correctly"
                                else:    
                                    for r in range(len(self.rans)):
                                        print "Question:",self.rans[r]+1 #Calculating right answer
                                        print "Your answered",self.ans[self.rans[r]]
                                        print "You answered correctly"
                            elif y==2:
                                if len(self.wans)==0:
                                    print "No question is answered wrongly"
                                else:
                                    for w in range(len(self.wans)):
                                        print "Question:",self.wans[w]+1 #Calculating wrong answer
                                        print "Your answered",self.ans[self.wans[w]]
                                        print "You answered wrongly"
                            elif y==3:
                                if len(self.nans)==0:
                                    print "Every question is marked"
                                else:
                                    for n in range(len(self.nans)):
                                        print "Question:",self.nans[n]+1
                                        print "Your answered",self.ans[self.nans[n]]
                                        print "You did not answered"
                            elif y==4:
                                print "Total marks",self.marks
                            elif y==5:
                                if self.marks<=10:
                                    print "Below average performance"
                                    print "You can do more well"
                                if self.marks>10 and self.marks<=25:
                                    print "Average performance"
                                    print "You can do more well and you will"
                                if self.marks>25 and self.marks<=50:
                                    print "Fair Performance"
                                    print "You can do more well and you will"
                                if self.marks>50 and self.marks<=75:
                                    print "Good performance"
                                    print "You can do more well and you will"
                                if self.marks>75 and self.marks<=100:
                                    print "Very Good performance"
                                    print "Now Go for a full score"
                                if self.marks>100 and self.marks<=115:
                                    print "Excellent performance"
                                    print "Now its turn for full score"
                                if self.marks>115 and self.marks<=120:
                                    print "Extraordinary Performance"
                                    print "You are the star of this test"
                                    print "All the best for your upcoming exams and keep it up like this"
                            else:
                                break
            else:
                print "Answerkey answerkey does not exist"
print '''If you are admin type "1"
        If you are user type "2" '''
#Asking User for his appropiate Choise
a=int(raw_input("Enter your appropiate choise from above selection"))
if a==1:
    obj=online_examination()
    obj.admin()
elif a==2:
    obj=result_time()
    obj.user()
    obj.count_marks()
else:
    "Please Choose appropiate choise from above"




