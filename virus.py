# module
import sys,time,os,random

####################################
#             Warna Random         #
####################################
P = "\33[37;1m" # PUTIH
U = "\33[35;1m" # UNGU
H = "\33[30;1m" # HITAM
J = "\33[32;1m" # HIJAU
B = "\33[34;1m" # BIRU
O = "\33[36;1m" # BIRU MUDA
K = "\33[33;1m" # KUNING
M = "\33[31;1m" # MERAH

my_color = [
P, U, H, J, B, O, K, M]
warna = random.choice(my_color)

#### DETIK BERJALAN ####
def detik():
        detik = ["\33[30;1m[\x1b[1;96m01\33[30;1m]","\33[30;1m[\x1b[1;96m02\33[30;1m]","\33[30;1m[\x1b[1;96m03\33[30;1m]","\33[30;1m[\x1b[1;96m04\33[30;1m]","\33[30;1m[\x1b[1;96m05\33[30;1m]","\33[30;1m[\x1b[1;96m06\33[30;1m]","\33[30;1m[\x1b[1;96m07\33[30;1m]","\33[30;1m[\x1b[1;96m08\33[30;1m]","\33[30;1m[\x1b[1;96m09\33[30;1m]","\33[30;1m[\x1b[1;96m10\33[30;1m]","\33[30;1m[\x1b[1;96m11\33[30;1m]","\33[30;1m[\x1b[1;96m12\33[30;1m]","\33[30;1m[\x1b[1;96m13\33[30;1m]","\33[30;1m[\x1b[1;96m14\33[30;1m]","\33[30;1m[\x1b[1;96m15\33[30;1m]"]
        for x in detik:
                print "\r\33[31;1mSedang \33[36;1mProses : %s"%(x),
                sys.stdout.flush()
                time.sleep(1)


###############################################
#                 Mengetik Auto               #
###############################################
def auto(z):
        for e in z + '\n':
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(0.05)
###############################################
#               Menanyakan sesuatu            #
###############################################
def ngentot():
        auto("\n\33[;0mApakah anda ingin \33[31;1mAtack \33[;0mLagi?")
        nanya = raw_input("\33[;0m[\33[36;1mY\33[;0m/\33[31;1mn\33[;0m] : \33[36;1m")
        if nanya =="Y" or nanya =="y":
                auto("Mohon Menunggu...")
                print "%sAnda Harus menunggu %s15 %sdetik."%(O,M,O)
                time.sleep(3)
                os.system("clear")
                detik()
                babi()
        elif nanya =="N" or nanya =="n":
                auto("\33[;0mSelamat tinggal... / Bye Bye")
                time.sleep(1)
        elif nanya =="" or nanya =='':
                auto("\nBodoh, Jangan Sampe Kosong!!")
                raw_input("\33[30;1m[\33[33;1m+\33[30;1m] \33[;0mTekan Enter Untuk \33[36;1mKembali\33[;0m.....");ngentot()
                time.sleep(1)
def babi():
        os.system("clear")
        print "%s______________________________________________"%(O)
        print "%s[%s+%s] %sAuthor  %s: %sReaper-XD                    %s[%s+%s]"%(K,H,K,M,P,O,K,H,K)
        print "%s[%s+%s] %sGithub  %s: %sReaper-XD                    %s[%s+%s]"%(K,H,K,M,P,O,K,H,K)
        print "%s[%s+%s] %sFacebook%s: %sReaperXD277                  %s[%s+%s]"%(K,H,K,M,P,O,K,H,K)
        print "%s[%s+%s] %sDon't Change %sAuthor %sScript Mee         %s[%s+%s]"%(K,H,K,M,P,O,K,H,K)
        print "%s______________________________________________"%(O)


        nomor = raw_input("\33[;0mMasukkan Nomor Target : \33[35;1m")
        jumlah = int(input("\33[;0mMasukkan Jumlah Target : \33[35;1m"))
        time.sleep(1)


        try:
                for i in range(jumlah):
                        print "\33[;0mBerhasil Mengirim Virus ke > \33[36;1m",nomor
                        time.sleep(0.05)
        except KeyboardInterrupt:
                print "\33[36;1m>v< \33[;0mSelesai \33[36;1m^>v<"
                ngentot()
babi()
