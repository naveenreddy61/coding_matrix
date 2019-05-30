# -*- coding: utf-8 -*-
"""
Created on Fri May 17 08:44:04 2019

@author: admin
"""

# -*- coding: utf-8 -*-
"""
Created on Sun May 12 18:44:21 2019
@author: naveenpc
"""
from GF2 import one
from GF2 import zero
gf2_int_to_str_dict = {0:zero,1:one}
gf2_str_to_int_dict = {zero:0,one:1}
def gf2_to_str(L):
    return ([gf2_int_to_str_dict[int(i)] for i in L])
def gf2_to_int(L):
    return ([gf2_str_to_int_dict[i] for i in L])
in1='101'
in2='100'
cypher = "1010100100101010101111001000110101110101001001100111010"
cypher_list = gf2_to_str(cypher)
#in1_= gf2_int_to_str(in1)
#in1__ = gf2_str_to_int(in1_)
#print(in1_)
#print(in1__)
base =2
key_length = 5
digits = set(range(base))
digits_dic = {i:i for i in digits}
all_keys = [list(digits_dic[(i//base**k)%base] for k in reversed(range(key_length))) for i in range(base**key_length)]
repeat = int(len(cypher_list)/key_length)
len_all_keys = len(all_keys)
#key = ["11111"]
#key_list = gf2_to_str(key[0])

key_list_full = []
for j in range(len_all_keys):
    allx = all_keys[j]
    for i in range(10):
        all_keys[j]=all_keys[j]+allx

all_keys_gf2 = [gf2_to_str(all_keys[i]) for i in range(len_all_keys)]
message_list = [[a-b for (a,b) in zip(cypher_list,all_keys_gf2[i])] for i in range(len_all_keys) ]    
message_list_int = [gf2_to_int(message_list[i]) for i in range(len_all_keys)]
L=[[[] for i in range(11)] for _ in range(32)]
for i in range(32):
    j,k = 0,0
    while j<55:
        L[i][k].extend([str(message_list_int[i][j])+str(message_list_int[i][j+1])+str(message_list_int[i][j+2])+str(message_list_int[i][j+3])+str(message_list_int[i][j+4])])
        j = j+5
        k = k+1

final_dict={'00000':'A',
            '00001':'B',
            '00010':'C',
            '00011':'D',
            '00100':'E',
            '00101':'F',
            '00110':'G',
            '00111':'H',
            '01000':'I',
            '01001':'J',
            '01010':'K',
            '01011':'L',
            '01100':'M',
            '01101':'N',
            '01110':'O',
            '01111':'P',
            '10000':'Q',
            '10001':'R',
            '10010':'S',
            '10011':'T',
            '10100':'U',
            '10101':'V',
            '10110':'W',
            '10111':'X',
            '11000':'Y',
            '11001':'Z',
            '11010':'0',
            '11011':'1',
            '11100':'2',
            '11101':'3',
            '11110':'4',
            '11111':'5'
            }

J=[[] for _ in range(32)]

for i in range(32):
   for j in range(11):
       J[i].extend(final_dict[L[i][j][0]])