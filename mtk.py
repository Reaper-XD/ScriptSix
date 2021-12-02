#!/bin/py

# Jangan Recode ya TOT!!!!!!

#module
import os,sys,time,requests
from time import sleep

#tampilan
os.system("clear")
os.system("figlet kalkulator")
tampilan ="""
\033[33;1m=================\033[37;1m==================\033[35;1m========================
\033[32;1m=       \033[36;1m(+)Author     : \033[32;1mReza Alfauzan                     =
\033[31;1m=       \033[36;1m(+)Github     : \033[31;1mhttps://github.com/GRCR4K3R       =
\033[34;1m=       \033[1;91m(+)Youtube    : \033[2;27mReja Gaming                       =
\033[34;1m=       \033[31;1m(+)Pesan      : \033[1;91mJangan Recode Mas:)               =
\033[36;1m=       (+)Pesan      : \033[36;1mGua Masih Noob:'(                 =
\033[32;1m=              \033[36;1m(+)===  \033[31;1mWelcome To Termux \033[36;1m===(+)           =
\033[36;1m===========================================================
\033[34;1m(+)=====================================================(+)
\033[32;1m(+)==================== \033[34;1mJangan Recode Mas \033[32;1m==============(+)
\033[32;1m(+)\033[36;1m=====================================================\033[32;1m(+)"""
sleep(0.1)
print(tampilan)
print("")
print("1)\033[32;1mPertambahan")
print("2)\033[36;1mPengurangan")
print("3)\033[34;1mPerkalian")
print("4)\033[36;1mPembagian")
print("\033[36;1m__\033[34;1m_______\033[32;1m_______\033[32;1m_______")
pilih =input("\033[32;1mPilih \033[36;1mSalah \033[32;1mSatu :")

#Data Pertambahan
if pilih =="1":
        angka1 =int(input("Angka Pertama :"))
        angka2 =int(input("Angka Kedua :"))
        print(angka1 + angka2)
#Data Pengurangan
if pilih =="2":
        angka1 =int(input("Angka Pertama :"))
        angka2 =int(input("Angka Kedua : "))
        print(angka1 - angka2)
#Data Perkalian
if pilih =="3":
        angka1 =int(input("Angka Pertama :"))
        angka2 =int(input("Angka Kedua :"))
        print(angka1 * angka2)
#Data Pembagian
if pilih =="4":
        angka1 =int(input("Angka Pertama :"))
        angka2 =int(input("Angka Kedua :"))
        print(angka1 / angka2)
