import os
class Studentdata:
    def datal():
        ch = 'y'
        while(ch=='y'):
            fr = open('student.txt','r')
            dl = str(input('Enter student number you want to view: '))            
            s =' '
            while(s):
                s = fr.readline()
                L = s.split('~')
                if dl in L:
                    print(s)
            fr.close()
            ch = input('Do you want to continue(y/n): ')

    def dataad():
        ch = 'y'
        while(ch=='y'):
            stn = int(input('Student Number: '))
            n = input('Name: ')
            a = int(input('Age: '))
            s = input('Gender: ')
            c = input('Civil Status: ')
            s1 = (str(stn)+'~'+n+'~'+str(a)+'~'+s+'~'+c+'\n')
            with open('student.txt', 'a') as f:
                for student in s1:
                    f.write(student)
            ch = input('Do you want to continue(y/n): ')

    def update():
        ch = 'y'
        while(ch=='y'):
            fr = open('student.txt', 'r')
            fw = open('temp.txt', 'w')
            ud = int(input('Enter the number you want to update: '))
            s =' '
            while(s):
                s = fr.readline()
                L = s.split('~')
                if len(s)>0:
                    if int(L[0])==ud:
                        stn = int(input('Student Number: '))
                        n = input('Name: ')
                        a = int(input('Age: '))
                        s = input('Gender: ')
                        c = input('Civil Status: ')
                        fw.write(str(stn)+'~'+n+'~'+str(a)+'~'+s+'~'+c+'\n')
                    else:
                        fw.write(s)
            fw.close()
            fr.close()
            os.remove('student.txt')
            os.rename('temp.txt','student.txt')
            ch = input('Do you want to continue(y/n): ')

    def datadel():
        ch = 'y'
        while(ch=='y'):
            fr = open('student.txt','r')
            fw = open('temp.txt','w')
            dd = int(input('Enter the student number you want to delete: '))
            s =' '
            while(s):
                s = fr.readline()
                L = s.split('~')
                if len(s)>0:
                    if int(L[0])!=dd:
                        fw.write(s)
            fr.close()
            fw.close()
            os.remove('student.txt')
            os.rename('temp.txt','student.txt')
            ch = input('Do you want to continue(y/n): ')

            
