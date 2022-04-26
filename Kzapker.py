import os, sys
from WG import WordlistGenerator
import argpars as argparse
import threading
from subprocess import PIPE, Popen
import time
parser = argparse.ArgumentParser(description='RAR bruteforce')
parser.add_argument(
    '-fp',
    type=str,
    default=None,
    help='Arch path'
)
parser.add_argument(
    '-c',
    type=str,
    default='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',
    help='Chars bruteforce'
)
parser.add_argument(
    '-n',
    type=int,
    default=None,
    help='Password lenght'
)
parser.add_argument(
    '-t',
    type=int,
    default=10,
    help='Threads'
)
my_namespace = parser.parse_args()
arch = my_namespace.fp
chars = my_namespace.c
n = my_namespace.n
if my_namespace.fp == None:
    print('Arch not detected')
    sys.exit()
if not os.path.exists('extract_dir'):
    os.mkdir('extract_dir')
for item in os.listdir('extract_dir'):
    os.remove(f'extract_dir\\{item}')
passwd = WordlistGenerator(n, chars) # Two args: (leght, words) words not necessary
c = 0
crack_pass = 'None'
th = []
def crack(pwd):
    cmd = Popen(
        f'Rar.exe x -o+ -p{pwd} "{arch}" extract_dir',
        stdout=PIPE,
        stderr=PIPE,
    )
    out, err = cmd.communicate()
    if 'All OK' in out.decode():
        global crack_pass
        crack_pass = pwd

for i in range(passwd.len_password):
    if len(os.listdir('extract_dir')) != 0:
        break
    pwd = passwd.next()
    print(f'\rPassword: {pwd} | {c}/{passwd.len_password}', end='')
    c += 1
    th.append(threading.Thread(target=crack, args=(pwd, )))
    th[-1].start()
    while len(th) >= int(my_namespace.t):
        clear_th = [i.is_alive() for i in th]
        for count, item in enumerate(clear_th):
            if item == False:
                th.pop(count)
                break
time.sleep(2)
print('\r----------------------', " " * 10)
print(f'PASSWORD FOUND: {crack_pass}')
print('----------------------')
