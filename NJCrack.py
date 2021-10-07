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
jalan ( "\t \033[1;92m                      Noyan Jani   and  Ayyan Khan " )


print """\033[1;93m--------------------------------------------------------------"""



def menu():
    print "CHOOSE OPTION:"
    print """[1] Show wordlist
[2] Automate Bruteforce
[3] Create Wordlist
[4] Manual Bruteforce
[0] Exit"""
    mcq()


def mcq():
    op = raw_input(">>>")
    if op == '':
        print "error"
        mcq()
    elif op == '1':
        cmnd = "python2 data/swl.py"
        os.system(cmnd)
    elif op == '2':
        print "CHOOSE OPTION:"
        cae()
    elif op == '3':
        cmnd = "python2 data/cr.py"
        os.system(cmnd)
    elif op == '4':
        print "CHOOSE OPTION:"
        mbf()
    elif op =='0':
        os.sys.exit()
    else :
        print "error"
        mcq()


def cae():
    print """[1] Attack with Proxy
[2] Attack without Proxy"""
    cae = raw_input(">>>")
    if cae == '':
        print "IOError"
        cae()
    elif cae == '1':
        cmnd = "python2 data/caei.py"
        os.system(cmnd)
    elif cae == '2':
        cmnd = "python2 data/caes.py"
        os.system(cmnd)





def mbf():
    print "Choose Option:"
    print """[1] Attack with Proxy
[2] Attack without Proxy"""
    mb  = raw_input(">>>")
    if mb == '':
        print "IO Error"
        mbf()
    elif mb == '1':
        cmnd = "python2 data/mbfi.py"
        os.system(cmnd)
    elif mb == '2':
        cmnd = "python2 data/mbfs.py"
        os.system(cmnd)


menu()
