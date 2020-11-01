import collections
import matplotlib.pyplot as plt

alphabet = [chr(i) for i in range(ord('а'),ord('я')+1)]
max_key_length= 30

def encrypt_vigenere(pt, key):
    ct=''
    n=0
    for i in range(0, len(pt)):
        if pt[i] in alphabet:
            ct+=alphabet[(alphabet.index(pt[i])+alphabet.index(key[n%len(key)]))%len(alphabet)]
            n+=1
        else:
            ct+=pt[i]
    return ct

def decrypt_vigenere(ct, key):
    pt=''
    n=0
    for i in range(0, len(ct)):
        if ct[i] in alphabet:
            pt+=alphabet[(alphabet.index(ct[i])-alphabet.index(key[n%len(key)])+len(alphabet))%len(alphabet)]
            n+=1
        else:
            pt+=ct[i]
    return pt


def index_of_coincidence(text):
    sum =0
    for i in set(text):
        count = text.count(i)
        sum+=count*(count-1)
    return sum/(len(text)*(len(text)-1))

def all_indexes(ct):
    indexes=[]
    for i in range(1, max_key_length+1):
        ct_part=[ct[p] for p in range(0, len(ct), i)]
        indexes.append(index_of_coincidence(''.join(ct_part)))
    return indexes


def try_guess_length(indexes):
    for l in range(2, max_key_length+1):
        if all(z==True for z in [all(p<indexes[i-1] for p in indexes[i-l:i-1]) for i in [l+k*l for k in range(0, int(len(indexes)/l))]]):
            return l

def count_frequencies(part_ct):
    c = collections.Counter(part_ct)
    frequencies = {c[i]/len(part_ct):i  for i in c}
    return frequencies

def find_most_frequent(part_ct):
    frequencies=count_frequencies(part_ct)
    return frequencies[max(frequencies)]


def generate_key(ct, key_len, chan):
    most_frequent=['о', 'а', 'е', 'и', 'н', 'т', 'р', 'с']
    key=''
    for i in range(key_len):
        fr=find_most_frequent([ct[k] for k in range(i, len(ct), key_len)])
        key+=alphabet[(alphabet.index(fr)-alphabet.index(most_frequent[chan[i]%len(most_frequent)])+len(alphabet))%len(alphabet)]
    return key

def paint_bar(indexes):
    x=range(len(indexes))
    y=indexes

    plt.bar([xel+2 for xel in x],y,align='center')
    plt.title('indexes of coincidence bar chart')
    plt.xlabel('r')
    plt.ylabel('indexes')
    plt.show()
