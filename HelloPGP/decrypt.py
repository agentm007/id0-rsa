#!/usr/bin/python3
import subprocess

wordlist = open('/usr/share/dict/words')
words = [i.strip('\n') for i in wordlist]

for i in words:
    output = subprocess.run(["gpg", "-d", "--batch", "--passphrase", i, "message"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if(output.returncode == 0):
        print(i)
        break
