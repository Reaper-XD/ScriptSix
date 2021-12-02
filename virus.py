#!/bin/python

# Jangan recode ngentottt!!!!

# module
import os
import sys
import time


# mengetik otomatis
def auto(z):
        for e in z + "\n":
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(0.05)



# pertanyaan (y/t)
def nanya():
        nanya =raw_input("\033[34;1mApakah \033[32;1m anda \033[35;1m ingin \033[36;1matack lagi? \033[36;1m[\033[32;1mY\033[34;1m/\033[35;1mT\033[33;1m] \033[35;1m~\033[33;1m=> ")
        if nanya =="Y" or nanya =="y":
                menu()
        elif nanya =="T" or nanya =="t":
                auto("\033[35;1mBye \033[32;1mBye \033[33;1m:)")
                time.sleep(1)
                sys.exit()
        elif nanya =="" or nanya =='':
                auto("\033[32;1mJangan \033[35;1msampe \033[36;1mkosong \033[32;1mya")
                time.sleep(1)
                nanya()
        else:
                auto("\033[32;1mSalah, \033[35;1mMasukkan \033[36;1minput \033[32;1mpilihan \033[36;1mdengan \033[33;1mbenar!")
                time.sleep(1)
                nanya()
                         
##menu

def menu():
        os.system("clear")
        os.system("figlet Trojan Nih!!")
        os.system("figlet Ini Virus Anjing!")
        logo = """
\033[32;1m=========================================================================
\033[35;1m=            [+] Author     : Reza Alfauzan               [+]           =
\033[31;1m=            [+] Github     : https://github.com/GRCR4K3R [+]           =
\033[1;91m=            [+] Facebook   : Rzaa Ajaa                   [+]           =
\033[36;1m==============[+]==========================================[+]===========
\033[33;1m===========================[+] Jangan Di Recode  [+]=====================
\033[36;1m===========================[+] Love You Woii<3   [+]=====================
\033[31;1m======================[+] Ini Sama di script sebelah [+]================="""
        print logo
        nomor = raw_input("\033[34;1mMasukkan \033[36;1mNomor \033[33;1mTarget : ") # input untuk si user memasukkan nomornya
        jumlah = int(input("\033[31;1mMasukkan \033[35;1mjumlahnya : ")) # input untuk menyuruh si user memasukkan jumlahnya
        time.sleep(1)

        try:
                for i in range(jumlah):
                        print "\033[34;1mBerhasil \033[36;1mmengirim \033[33;1mVirus \033[35;1m\033[36;1mKe \033[36;1m=>",nomor
                        time.sleep(0.1)
        except KeyboardInterrupt:
                print "\033[36;1m### \033[33;1mSelesai \033[32;1m###"
        nanya()
menu()
