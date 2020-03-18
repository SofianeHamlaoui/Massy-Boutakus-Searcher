#!/usr/bin/env python3
# Massy Boutakus Searcher
# 123 Vive Dz
import os
import requests
import sys
import re
from bs4 import BeautifulSoup
import re
import tempfile
import atexit
import time
from datetime import datetime

yes = set(['yes', 'y', 'ye', 'Y'])
no = set(['no', 'n', 'nop', 'N'])

def exit_handler():
    if os.path.isfile("/tmp/search"):
        os.system('rm /tmp/search')
    else:
        print("")
atexit.register(exit_handler)

def printlogo():
    os.system('clear')
    print("""
\033[0;34m______  ___                       \033[1;35m          ________             _____       ______                 
\033[0;34m___   |/  /_____ ___________________  __    \033[1;35m___  __ )_________  ___  /______ ___  /_____  _________ 
\033[0;34m__  /|_/ /_  __ `/_  ___/_  ___/_  / / /    \033[1;35m__  __  |  __ \  / / /  __/  __ `/_  //_/  / / /_  ___/ 
\033[0;34m_  /  / / / /_/ /_(__  )_(__  )_  /_/ /     \033[1;35m_  /_/ // /_/ / /_/ // /_ / /_/ /_  ,<  / /_/ /_(__  )  
\033[0;34m/_/  /_/  \__,_/ /____/ /____/ _\__, /      \033[1;35m/_____/ \____/\__,_/ \__/ \__,_/ /_/|_| \__,_/ /____/   
                               \033[0;34m/____/\033[0m                                                                       
                    \033[0;31m________                        ______              
                    __  ___/__________ ________________  /______________
                    _____ \_  _ \  __ `/_  ___/  ___/_  __ \  _ \_  ___/
                    ____/ //  __/ /_/ /_  /   / /__ _  / / /  __/  /    
                    /____/ \___/\__,_/ /_/    \___/ /_/ /_/\___//_/\033[0m
                \033[0;34mCopyright Massy Rkhis 2020 with the help of \033[0;31mCoronaVirus\033[0m
                                    \033[0;31mSofiane Hamlaoui 2020\033[0m""")
    print("")

def about():
    printlogo()
    print("""

    #############################################################
    #                  Massy Boutakus Searcher                  #
    #           An HTTP/FTP Files & Directories Seacher         #
    #############################################################
    #    -- Version: v1.0 18/03/2020                            #
    #    -- Developer: Sofiane Hamlaoui                         #
    #    -- Thanks: Massy Boutakus & Corona with its lockdown   #
    #############################################################""")
    ans = input("\n\033[0;36mPress Enter to Continue...\033[0m")


def searchquerie():
    printlogo()
    print("")
    global tempchoice
    file = open( '/tmp/search', 'w' )
    tempchoice = input("""                          \033[0;34mWhat are you looking for ya boutak ?
                \033[0;31m( Never Be like my 2 friends Massy & Zakou the Boutakuses )\033[0m\n
    \033[92mQuery : \033[0m""")
    print("\n \033[0;33m                        The Search Query is set to : \033[92m" + tempchoice+ "\n")
    ans = input("\n\033[0;36mPress Enter to Continue...\033[0m")
    file.write(tempchoice)
    file.close()

def request(url, choice, page):
    headers = requests.utils.default_headers()
    headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
    durl = url + choice + page
    req = requests.get(durl, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    return soup

def mamont(nb):
    printlogo()
    print(" \033[92m                                Mamont Search ( FTP )\033[0m")
    f = open('/tmp/search')
    searchquerie = f.read().rstrip('\n')
    f.close()
    page = "&ot="
    soup = request("https://www.mmnt.ru/int/get?st=", searchquerie, page + str(nb))
    print("\n\033[0;31m=====================")
    print("======> FTP : <======")
    print("=====================\033[0m\n")
    for tr in soup.find_all('td'):
        for zftp in tr.find_all('a', attrs={'href': re.compile("ftp://")}):
            ftp = (zftp.get('href'))
            print("\033[1;33mFile : \033[1;36m" +ftp.rsplit('/', 1)[-1])
            print("\033[0;32m"+ftp)
            print("\033[1;35m------------------------------------\033[0m")
    print("\n\033[0;31m======================")
    print("======> Http : <======")
    print("======================\033[0m\n")
    for tr in soup.find_all('td'):        
        for zhttp in tr.find_all('a', attrs={'href': re.compile("https")}):
            http = (zhttp.get('href'))
            if 'https://www.mmnt.ru' not in http:
                print("\033[1;33mFile : \033[1;36m" +http.rsplit('/', 1)[-1])
                print("\033[0;32m"+http)
                print("\033[1;35m------------------------------------\033[0m")
    ans = input("\n               \033[1;31mGet results of the next page ? ( \033[1;33mY/yes, N/no\033[0m\033[1;31m ) : \033[0m")
    if not ans in no:
        nb += 20
        mamont(nb)
    else:
        print("\n\033[1;33m                        T'es Clairement un Boutakus :D\033[0m")
        time.sleep(2)
        menu()

def freeware(nb):
    printlogo()
    print(" \033[92m                                FreeWareWeb Search ( FTP )\033[0m")
    f = open('/tmp/search')
    searchquerie = f.read().rstrip('\n')
    f.close()
    page = "&m=20&f="
    soup = request("http://www.freewareweb.com/cgi-bin/ftpsearch.pl?q=", searchquerie, page + str(nb))
    print("\n\033[0;31m=============================")
    print("======> FTP : [Files] <======")
    print("=============================\033[0m\n")
    for tr in soup.find_all('a', {"class": "lf"}):
        files = (tr.get('href'))
        print("\033[1;33mFile : \033[1;36m" +files.rsplit('/', 1)[-1])
        print("\033[0;32m"+files)
        print("\033[1;35m------------------------------------\033[0m")
    print("\n\033[0;31m===================================")
    print("======> FTP : [Directories] <======")
    print("===================================\033[0m\n")
    for tr in soup.find_all('a', {"class": "lg"}):
        directory = (tr.get('href'))
        print("\033[1;33mDirectory : \033[1;36m" +directory.rsplit('/', 1)[-1])
        print("\033[0;32mhttp://www.freewareweb.com"+directory)
        print("\033[1;35m------------------------------------\033[0m")
    ans = input("\n               \033[1;31mGet results of the next page ? ( \033[1;33mY/yes, N/no\033[0m\033[1;31m ) : \033[0m")
    if not ans in no:
        nb += 20
        freeware(nb)
    else:
        print("\n\033[1;33m                        T'es Clairement un Boutakus :D\033[0m")
        time.sleep(2)
        menu()

def filesearching(nb):
    printlogo()
    print(" \033[92m                                FreeWareWeb Search ( FTP )\033[0m")
    f = open('/tmp/search')
    searchquerie = f.read().rstrip('\n')
    f.close()
    url = "http://www.filesearching.com/cgi-bin/s?q="
    page = "&m=20&f="
    durl = url + searchquerie + page + str(nb)
    req = requests.get(durl, headers={'referer': "http://www.filesearching.com/"})
    soup = BeautifulSoup(req.content, 'html.parser')
    print("\n\033[0;31m=============================")
    print("======> FTP : [Files] <======")
    print("=============================\033[0m\n")
    for tr in soup.find_all('a', {"class": "lf"}):
        files = (tr.get('href'))
        print("\033[1;33mFile : \033[1;36m" +files.rsplit('/', 1)[-1])
        print("\033[0;32m"+files)
        print("\033[1;35m------------------------------------\033[0m")
    print("\n\033[0;31m===================================")
    print("======> FTP : [Directories] <======")
    print("===================================\033[0m\n")
    for tr in soup.find_all('a', {"class": "lg"}):
        directory = (tr.get('href'))
        print("\033[1;33mDirectory : \033[1;36m" +directory.rsplit('/', 1)[-1])
        print("\033[0;32mftp://"+directory.rsplit('=', 1)[-1])
        print("\033[1;35m------------------------------------\033[0m")
    ans = input("\n               \033[1;31mGet results of the next page ? ( \033[1;33mY/yes, N/no\033[0m\033[1;31m ) : \033[0m")
    if not ans in no:
        nb += 20
        filesearching(nb)
    else:
        print("\n\033[1;33m                        T'es Clairement un Boutakus :D\033[0m")
        time.sleep(2)
        menu()

def Searchshared():
    

def menu():
    printlogo()
    engine = input("""
                            \033[0;33mThe Seach Query is : \033[0m\033[92m""" + tempchoice + "\n"
        +"""\n\033[0;33m                            Choose a Search Option :

            \033[0;36m0 )\033[0m \033[1;33mChange the Search Query

            \033[0;36m1 )\033[0m \033[1;33mMamont (FTP) [The Best One]
            \033[0;36m2 )\033[0m \033[1;33mFreewareWeb (FTP)
            \033[0;36m3 )\033[0m \033[1;33mFilesearching (FTP)
            \033[0;36m4 )\033[0m \033[1;33mSearch Shared (Links)

            \033[0;36ma )\033[0m \033[1;33mLeave MBS\033[0m
            \033[0;36mq )\033[0m \033[1;33mLeave MBS\033[0m

\033[92mMassy Boutakus Searcher~# \033[0m """)
    if engine == "1":
        mamont(1)
    elif engine == "2":
        freeware(1)
    elif engine == "3":
        filesearching(1)
    elif engine == "q":
        os.system('clear')
        printlogo()
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print("                 \033[91m-[!]- \033[92mMassy Boutakus Searcher \033[90m\033[91mIS EXITING -[!]-\033[0m")
        print("")
        print("                 \033[91m-[!]- EXITING AT " + dt_string + " -[!]-\033[0m")
        sys.exit()
    elif engine == "0":
        searchquerie()
        menu()
    elif engine == "a":
        about()
        menu()
    elif engine == "":
        menu()
    else:
        menu()

if __name__ == "__main__":
    try:
        searchquerie()
        menu()
    except (KeyboardInterrupt):
        print("")
        ans = input("           \n\033[91m-[!]- SIGINT or CTRL-C detected. Are You sure to exit \033[92mMassy Boutakus Searcher \033[90m\033[91m-[!] ? (Y/N)\033[0m : ")
        if not ans in yes:
            menu()
        else:
            os.system('clear')
            printlogo()
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            print("                 \033[91m-[!]- \033[92mMassy Boutakus Searcher \033[90m\033[91mIS EXITING -[!]-\033[0m")
            print("")
            print("                 \033[91m-[!]- EXITING AT " + dt_string + " -[!]-\033[0m")
            sys.exit()