from functions import *

with open('cleared_text.txt', 'r', encoding='utf-8') as file:
    text = ''.join(file.readlines())

key1='ад'
key2='бан'
key3='бант'
key4='стиль'
key5='маленькаястрана'

ct1=encrypt_vigenere(text, key1)
ct2=encrypt_vigenere(text, key2)
ct3=encrypt_vigenere(text, key3)
ct4=encrypt_vigenere(text, key4)
ct5=encrypt_vigenere(text, key5)

print('ciphertext number 1:')
print(ct1)
print('indexes of coincidence:')
indexes1=all_indexes(ct1)
for i in indexes1[1:]:
    print(str(indexes1.index(i)+1)+': '+str(i))
print('automatically calculated key length: ', end='')
len1=try_guess_length(indexes1)
print(len1)
print('did i guess correctly? ("y" if yes, anything else if no):', end=' ')
answer = input()
if answer!='y':
    print('please print correct lenght: ', end='')
    len1=input()
print('this is the key i guessed, input "y" if it is right or number of the letter to change:', end=' ')
k=[0 for _ in range(int(len1))]
generated_key1=generate_key(ct1, int(len1), k)
print(generated_key1)
answer=input()
while answer!='y':
    k[int(answer)-1]+=1
    print('this is the key i guessed, input "y" if it is right or number of the letter to change:', end=' ')
    generated_key1=generate_key(ct1, int(len1), k)
    print(generated_key1)
    answer=input()
print('this is the plaintext:')
print(decrypt_vigenere(ct1, generated_key1)+'\n\n')


print('ciphertext number 2:')
print(ct2)
print('indexes of coincidence:')
indexes2=all_indexes(ct2)
for i in indexes2[1:]:
    print(str(indexes2.index(i)+1)+': '+str(i))
print('automatically calculated key length: ', end='')
len2=try_guess_length(indexes2)
print(len2)
print('did i guess correctly? ("y" if yes, anything else if no):', end=' ')
answer = input()
if answer!='y':
    print('please print correct lenght: ', end='')
    len2=input()
print('this is the key i guessed, input "y" if it is right or number of the letter to change:', end=' ')
k=[0 for _ in range(int(len2))]
generated_key2=generate_key(ct2, int(len2), k)
print(generated_key2)
answer=input()
while answer!='y':
    k[int(answer)-1]+=1
    print('this is the key i guessed, input "y" if it is right or number of the letter to change:', end=' ')
    generated_key2=generate_key(ct2, int(len2), k)
    print(generated_key2)
    answer=input()
print('this is the plaintext:')
print(decrypt_vigenere(ct2, generated_key2)+'\n\n')


print('ciphertext number 3:')
print(ct3)
print('indexes of coincidence:')
indexes3=all_indexes(ct3)
for i in indexes3[1:]:
    print(str(indexes3.index(i)+1)+': '+str(i))
print('automatically calculated key length: ', end='')
len3=try_guess_length(indexes3)
print(len3)
print('did i guess correctly? ("y" if yes, anything else if no):', end=' ')
answer = input()
if answer!='y':
    print('please print correct lenght: ', end='')
    len3=input()
print('this is the key i guessed, input "y" if it is right or number of the letter to change:', end=' ')
k=[0 for _ in range(int(len3))]
generated_key3=generate_key(ct3, int(len3), k)
print(generated_key3)
answer=input()
while answer!='y':
    k[int(answer)-1]+=1
    print('this is the key i guessed, input "y" if it is right or number of the letter to change:', end=' ')
    generated_key3=generate_key(ct3, int(len3), k)
    print(generated_key3)
    answer=input()
print('this is the plaintext:')
print(decrypt_vigenere(ct3, generated_key3)+'\n\n')


print('ciphertext number 4:')
print(ct4)
print('indexes of coincidence:')
indexes4=all_indexes(ct4)
for i in indexes4[1:]:
    print(str(indexes4.index(i)+1)+': '+str(i))
print('automatically calculated key length: ', end='')
len4=try_guess_length(indexes4)
print(len4)
print('did i guess correctly? ("y" if yes, anything else if no):', end=' ')
answer = input()
if answer!='y':
    print('please print correct lenght: ', end='')
    len4=input()
print('this is the key i guessed, input "y" if it is right or number of the letter to change:', end=' ')
k=[0 for _ in range(int(len4))]
generated_key4=generate_key(ct4, int(len4), k)
print(generated_key4)
answer=input()
while answer!='y':
    k[int(answer)-1]+=1
    print('this is the key i guessed, input "y" if it is right or number of the letter to change:', end=' ')
    generated_key4=generate_key(ct4, int(len4), k)
    print(generated_key4)
    answer=input()
print('this is the plaintext:')
print(decrypt_vigenere(ct4, generated_key4)+'\n\n')


print('ciphertext number 5:')
print(ct5)
print('indexes of coincidence:')
indexes5=all_indexes(ct5)
for i in indexes5[1:]:
    print(str(indexes5.index(i)+1)+': '+str(i))
print('automatically calculated key length: ', end='')
len5=try_guess_length(indexes5)
print(len5)
print('did i guess correctly? ("y" if yes, anything else if no):', end=' ')
answer = input()
if answer!='y':
    print('please print correct lenght: ', end='')
    len5=input()
print('this is the key i guessed, input "y" if it is right or number of the letter to change:', end=' ')
k=[0 for _ in range(int(len5))]
generated_key5=generate_key(ct5, int(len5), k)
print(generated_key5)
answer=input()
while answer!='y':
    k[int(answer)-1]+=1
    print('this is the key i guessed, input "y" if it is right or number of the letter to change:', end=' ')
    generated_key5=generate_key(ct5, int(len5), k)
    print(generated_key5)
    answer=input()
print('this is the plaintext:')
print(decrypt_vigenere(ct5, generated_key5)+'\n\n')
