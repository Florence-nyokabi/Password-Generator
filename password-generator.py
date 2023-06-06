import random as rand

chars = "abcdefghijklmnopqrstuvwxyz"
CHARS = chars.upper()
symbols = "[]{}()*;/,._-%^&$#@!"
numbers = "0123456789"

all_variables = chars + CHARS + symbols + numbers
len = 16

password = "".join(rand.sample(all_variables, len))

print(password)


'''
Output:

n/d-XW[IYl0m1V.8
G^Q6#)O%hoNkfaDW
C;WxcVwp0G3-]QFf
,_TXRKsN;g%u-zY#
xe,!U#KRA{a53mNC
#A$M^O}Ps&@g_kC7
[9%g2DF7M;.O0G4-
!oQ]@Tu,L3P56C1;

'''