from functions.functions import *

print('Print name of the file from directory text/ (d for default): ', end='')
file_to_open=input()
if file_to_open=='d':
    file_to_open='encrypted_vigenere_variant12.txt'

with open('text/'+file_to_open, 'r', encoding='utf-8') as file:
    text = ''.join(file.readlines())

print('ciphertext: ')
print(text[:100]+'...')
print()
print('indexes of coincidence: ')
indexes=all_indexes(text)
for j in indexes[1:]:
    print(str(indexes.index(j)+1)+': '+str(j))
len=try_guess_length(indexes)
print()
print('automatically calculated key length: '+str(len))
print('did i guess correctly? ("y" if yes, anything else if no): ', end='')
if input()!='y':
    print('please print correct length: ', end='')
    len=int(input())
    print()
k=[0 for _ in range(len)]
while True:
    key=generate_key(text, len, k)
    print('automatically calculated key: '+key)
    print('part of ciphertext decrypted by that key: '+decrypt_vigenere(text[:50], key))
    print('did i guess correctly? (if yes: "y", if no: number of letter to change): ', end='')
    answer=input()
    print()
    if answer=='y':
        break
    k[int(answer)-1]+=1
print('plaintext:')
print(decrypt_vigenere(text, key)[:100]+'...')

with open('text/'+'de'+file_to_open[2:], 'w', encoding='utf-8') as file:
    file.write(decrypt_vigenere(text, key)+":"+key)
print('full_plaintext:key were written to file text/'+'de'+file_to_open[2:])
