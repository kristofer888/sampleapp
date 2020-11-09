import pwd1
from studentfile import Studentdata
pwd1.Pwd('kris', 'kris888')
st = 'n'
while(st=='n'):
    print('Welcome to Student record system')
    print('1. Student Data')
    print('2. Add Data')
    print('3. Update Data')
    print('4. Delete Data')
    print('5. Exit the program')
    n = int(input('Enter the number you wish to proceed: '))
    if (n==1):
        Studentdata.datal()
    elif(n==2):
        Studentdata.dataad()
    elif(n==3):
        Studentdata.update()
    elif(n==4):
        Studentdata.datadel()
    elif (n==5):
        break
    else:
        print('Not on the list')
        break
    st = input('Exit the program(y/n): ')


