from collections import Counter
import itertools
import math

alphabet = "абвгдежзийклмнопрстуфхцчшщыьэюя"

def count_unigrams(text1):
    frequencies1 = {i: text1.count(i) / len(text1) for i in sorted(set(text1))}
    return frequencies1

def count_bigrams(text, intersection):
    bigrams_number = len(text2) - 1 if intersection else len(text) // 2
    bigrams = [(i + j) for (i, j) in zip(text[0::1 if intersection else 2], text[1::1 if intersection else 2])]
    coun = Counter(bigrams)
    frequencies2 = {i: coun[i] / bigrams_number for i in coun}
    return frequencies2

def entropy(frequencies):
    h = 0
    for i in frequencies:
        h -= frequencies[i] * math.log2(frequencies[i])
    h = h / len(list(frequencies.keys())[0])
    return h

def euclid(a, b):
    if b==0:
        return abs(a)
    else:
        return euclid(b, a%b)

def extended_euclid(a, b):
    if b==0:
        return [1, 0, abs(a)]
    u, v, gcd = extended_euclid(b, a%b)
    return [v, u-a//b*v, gcd]



def inverse_element(a, n):
    u,v,gcd=extended_euclid(a,n)
    if gcd==1:
        return u

def upper_letter(a, b):
    return alphabet.index(a)*len(alphabet)+alphabet.index(b)

def solve_linear(a, b, m):
    gcd = euclid(a, m)
    if gcd==1:
        return [inverse_element(a, m)*b%m]
    elif gcd>1:
        if b%gcd!=0:
            return []
        else:
            x0=(b/gcd*inverse_element(a/gcd, m))%m
            return [x0+m/gcd*i for i in range(gcd)]

def letters_from_upper_letter(x):
    return alphabet[int((x-x%len(alphabet))/len(alphabet))]+alphabet[x%len(alphabet)]

def decipher_afin_bigrams(a, b, text):
    out = []
    bigrams = [(i + j) for (i, j) in zip(text[0::2], text[1::2])]
    for i in bigrams:
        inv = inverse_element(a, pow(len(alphabet),2))
        if inv!=None:
            x = int(inv*(upper_letter(i[0], i[1])-b)%pow(len(alphabet),2))
            out.append(letters_from_upper_letter(x))
    return ''.join(out)

def get_coefs(a, b):
    coefa = solve_linear(upper_letter(a[0][0], a[0][1]) - upper_letter(a[1][0], a[1][1]), upper_letter(b[0][0], b[0][1])-upper_letter(b[1][0], b[1][1]), pow(len(alphabet), 2))
    coefb=[]
    for ael in coefa:
        coefb.append((upper_letter(b[0][0], b[0][1])-ael*upper_letter(a[0][0], a[0][1]))%pow(len(alphabet), 2))
    return [coefa, coefb]


def sort_dict(a):
    return {k: v for k, v in sorted(a.items(), key=lambda item: item[1])[::-1]}


def is_plaintext(text):
    frequencies = count_unigrams(text)
    entr = entropy(frequencies)
    frequencies = list(sort_dict(frequencies).keys())
    if all([i in frequencies[:13] for i in ['о', 'а', 'е']]) and 4.15 <= entr <= 4.55:
        return True



f=open('text/12.txt', 'r')
line=''.join(f.readlines()).replace('\n', '')
x=count_bigrams(line, False)
x=sort_dict(x)
first_elements = [i[0] for i in list(x.items())[:5]]
five_most_often = ["ст", "но", "то", "на", "ен"]

for i in itertools.permutations(five_most_often, 2):
    for j in itertools.permutations(first_elements, 2):
        a, b=get_coefs(i, j)
        for (ael, bel) in zip(a, b):
            plaintext = decipher_afin_bigrams(ael, bel, line)
            if len(plaintext)>0 and is_plaintext(plaintext):
                print(plaintext[:100])
                #print(ael)
                #print(bel)
                #print(i)
                #print(j)
