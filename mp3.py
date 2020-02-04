from os import listdir,system,getcwd,chdir,environ
from os.path import abspath,isdir,isfile
r1 = "\x1b[31;1;"
r2 = "\x1b[32;1;"
r3 = "\x1b[33;1;"
r4 = "\x1b[34;1;"
r5 = "\x1b[35;1;"
r6 = "\x1b[36;1;"
r0 = "\x1b[30;1;"
o = "\x1b[0m"
d = (KeyboardInterrupt,EOFError)
d1 = r2+";3m\nthanks gan"+o
w1 = environ.get ("HOME")
w2 = b'\x1b[32;1m \xe2\x96\x88\xe2\x96\x84\xe2\x96\x91\xe2\x96\x84\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x91\xe2\x96\x88 \xe2\x96\x84\xe2\x96\x80\xe2\x96\x80 \xe2\x96\x80 \xe2\x96\x84\xe2\x96\x80 \xe2\x96\x88\xe2\x96\x84\xe2\x96\x91\xe2\x96\x84\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x80\xe2\x96\x84 \xe2\x96\x90\xe2\x96\x8c\xe2\x96\x91\xe2\x96\x90\xe2\x96\x8c\n \xe2\x96\x88\xe2\x96\x91\xe2\x96\x88\xe2\x96\x91\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x91\xe2\x96\x88 \xe2\x96\x91\xe2\x96\x80\xe2\x96\x84 \xe2\x96\x88 \xe2\x96\x88\xe2\x96\x91 \xe2\x96\x88\xe2\x96\x91\xe2\x96\x88\xe2\x96\x91\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x91\xe2\x96\x88 \xe2\x96\x91\xe2\x96\x80\xe2\x96\x84\xe2\x96\x80\xe2\x96\x91\n \xe2\x96\x80\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x80 \xe2\x96\x91\xe2\x96\x80\xe2\x96\x91 \xe2\x96\x80\xe2\x96\x80\xe2\x96\x91 \xe2\x96\x80 \xe2\x96\x91\xe2\x96\x80 \xe2\x96\x80\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x80 \xe2\x96\x88\xe2\x96\x80\xe2\x96\x91 \xe2\x96\x91\xe2\x96\x91\xe2\x96\x80\xe2\x96\x91\xe2\x96\x91\x1b[0m\x1b[36;1m\n==============================\x1b[0m\x1b[35;1m\n# \x1b[33;1mauthor   : \x1b[32;1meren jeager\x1b[35;1m\n# \x1b[33;1mcountry  : \x1b[32;1mindonesia\x1b[35;1m\n# \x1b[33;1mreligion : \x1b[32;1mislam\x1b[0m\n\x1b[36;1m==============================\x1b[0m'.decode ()
w3 = "\n"+r3+"m CTRL + c = berhenti\n"+r3+"m CTRL + v = mengatur volume\n"+r6+"m"+r3+"m CTRL + z = keluar\n\n"+r2+"m\rsedang memutar . . ."+r6+";5m"
def out (c1,c2,c3=""):
    try:
        if c2 == "home":
            print (r0+"m# "+r5+"m["+r3+"m01"+r5+"m] "+r6+"mpenyimpanan internal"+o)
            print (r0+"m# "+r5+"m["+r3+"m02"+r5+"m] "+r6+"mpenyimpanan lain"+o)
            dr3 = "/sdcard /storage".split ()
        elif c2 == "tem":
            chdir (c1)
            tt = listdir ()
            dr1 = [ff for ff in tt if isdir (ff)]
            dr2 = [ff for ff in tt if ff.endswith (".mp3")]
            dr3 = dr1 + dr2
            if len (dr3) > 0:
                for ii in range (len (dr3)):
                    if isdir (dr3 [ii]):
                        wr = r6
                    elif isfile (dr3 [ii]):
                        wr = r5
                    if ii < 9:
                        ss = "0"
                    else:
                        ss = ""
                    print (r0+"m# "+r5+"m["+r3+"m"+ss+str (ii+1)+r5+"m] "+wr+"m"+dr3 [ii]+o)
            else:
                print (r1+";3mtidak terdapat folder atau file musik disini"+o)
        elif c2 == "fi":
            chdir (w1)
            try:
                with open ("....","r") as aa:
                    dr2 = aa.read ().strip ("\n").split ("\n")
            except  (FileNotFoundError):
                print (r1+";7mfilenya udah lu hapus bangsat"+o)
                aa = open ("....","w").close ()
                exit ()
            dr3 = []
            try:
                for ii in dr2:
                    if not ii in dr3:
                        dr3.append (ii)
                print ()

                for ii in range (len (dr3)):
                    if ii < 9:
                        ss = "0"
                    else:
                        ss = ""
                    print (r0+"m# "+r5+"m["+r3+"m"+ss+str (ii+1)+r5+"m] "+r6+"m"+dr3 [ii][dr3 [ii].rindex ("/")+1:]+o)
            except (ValueError):
                print (r2+";7mtidak terdapat lagu"+o)

        if len (c3) > 0:
            print (c3)
        if   ((c2 != "fi") and (c2 != "home")):
            print (r0+"m# "+r5+"m["+r3+"m"+"b"+r5+"m] "+r3+"m"+"back"+o)
            print (r0+"m# "+r5+"m["+r3+"m"+"a"+r5+"m] "+r3+"m"+"awal"+o)
        elif c2 == "fi":
            print (r0+"m# "+r5+"m["+r3+"m"+"p"+r5+"m] "+r3+"m"+"mainkan semua"+o)
            print (r0+"m# "+r5+"m["+r3+"m"+"d"+r5+"m] "+r3+"m"+"delete list"+o)
        print (r0+"m# "+r5+"m["+r3+"m"+"h"+r5+"m] "+r3+"m"+"home"+o)
        print (r0+"m# "+r5+"m["+r3+"m"+"e"+r5+"m] "+r3+"m"+"exit"+o)
        return dr3
    except d:
        exit (d1)
def mu (a1,a2=1):
    chdir (w1)
    for ii in range (a2):
        system ('mpv "'+a1+'" > ...')
        if a2 > 1:
            print ("\r"+r2+"mtunggu . . ."+r6+"m",end="")
    print ()

def cari ():
    try:
        a1 = ""
        a2 = "home"
        a3 = ""
        while True:
            try:
                dr1 = out (a1,a2,a3)
                t1 = getcwd ()
                pil = str (input (r3+";7mpilih :"+o+r6+"m ")).lower ()
                if pil.isnumeric () and int (pil)-1 in range (len (dr1)):
                    if dr1 [int (pil)-1].endswith (".mp3"):
                        try:
                            print (r2+";7m"+dr1 [int (pil)-1]+o)
                            mn = str (input (r3+";7mmainkan [y/n/u] "+o+r6+"m ")).lower ()
                            if mn == "y":
                                chdir (w1)
                                with open ("....","a") as aa:
                                    aa.write (t1+"/"+dr1 [int (pil)-1]+"\n")
                                print (w3,end="")
                                mu (t1+"/"+dr1 [int (pil)-1])
                                chdir (t1)
                            elif mn == "u":
                                try:
                                    uu = int (input (r3+";7mjumlah ulangi "+o+r6+"m "))
                                except (ValueError):
                                    print ("\t"+r1+";7mmasukan angka cuk"+o)
                                except d:
                                    exit (d1)
                                else:
                                    if uu == 1:print (w3,end="")
                                    else:print (w3.replace ("berhenti","next part"),end="")
                                    mu (t1+"/"+dr1 [int (pil)-1],uu)

                        except d:
                            exit (d1)
                    else:
                        a1 = abspath (dr1 [int (pil)-1])
                        a2 = "tem"
                if pil == "h":home ()
                elif pil == "b":a1 = abspath ("..")
                elif pil == "e": exit (d1)
                elif pil == "a":a1="";a2 = "home"
            except d:
                exit (d1)
            except (PermissionError):a3 = r1+";7mizin akses ditolak"+o;a1 = t1
            else:a3 = ""
    except d:
        exit (d1)
def ter ():
    try:
        while True:
            try:
                dr1 = out ("","fi")
                pil = str (input (r3+";7mpilih : "+o+r6+"m ")).lower ()
                if pil.isnumeric () and int (pil)-1 in range (len (dr1)):
                    se = dr1 [int (pil)-1]
                    print (r2+";7m"+se [se.rindex ("/")+1:]+o)
                    ya = str (input (r3+";7mmainkan [y/n/u] "+o+r6+"m ")).lower ()
                    if ya == "y":
                        chdir (w1)
                        print (w3,end="")
                        mu (se)
                    elif ya == "u":
                        try:
                            uu = int (input (r3+";7mjumlah ulangi "+o+r6+"m "))
                            if uu > 1:
                                print (w3.replace ("berhenti","next part"),end="")
                            else:
                                print (w3,end="")
                            mu (se,uu)
                        except d:exit (d1)
                        except (ValueError):print ("\t"+r1+";7mmasukan angka cuk"+o)
                elif pil == "p":
                    chdir (w1)
                    print (w3.replace ("berhenti","next music"),end="")
                    for ii in range (len(dr1)):
                        mu (dr1 [ii])
                        print (r2+";m\rtunggu . . ."+r6+"m",end="")
                elif pil == "h":
                    home ()
                elif pil == "e":
                    exit (d1)
                elif pil == "d":
                    chdir (w1)
                    system ("false > ....")
            except d:
                exit (d1)
    except d:
        exit (d1)
def home ():
    try:
        while True:
            system ("clear")
            print (w2)
            print (f"\n\t {r5};m[{r6};m01{r5};m] {r2};mcari lagu\n\t {r5};m[{r6};m02{r5};m] {r2};mterakhir diputar\n\t {r5};m[{r6};m03{r5};m] {r2};mexit"+o)
            sd = [cari,ter,exit]
            try:
                pil = int (input (r3+";7mpilih : "+o+r6+"m "))
                if pil-1 in range (len (sd)):
                    sd [pil-1]()
            except (ValueError):
                print (r1+";7mmasukan angka cuk"+o)
            except d:exit (d1)
    except d:exit (d1)
def install ():
    try:
        chdir (environ.get ("PREFIX")+"/"+"bin")
        if "mpv" in listdir ():
            home ()
        else:
            print (r6+";7msedang menginstall package"+o)
            system ("pkg install mpv -y")
            exit (r6+";7mpackage telah terinstall\nsilahkan ketik ulang python mp3.py"+o)
    except d:exit (d1)
install ()
