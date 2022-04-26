import os, sys
from WG import WordlistGenerator
import argpars as argparse
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
for i in range(passwd.len_password):
    pwd = passwd.next()
    print(f'\rPassword: {pwd} | {c}/{passwd.len_password}', end='')
    os.system(f'Rar.exe -inul x -o+ -p{pwd} "{arch}" extract_dir > nul')
    if len(os.listdir('extract_dir')) != 0:
        print('\r----------------------')
        print(f'PASSWORD FOUND: {pwd}')
        print('----------------------')
        break
    c += 1