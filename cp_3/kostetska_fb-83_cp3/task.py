from collections import Counter

alphabet = "абвгдежзийклмнопрстуфхцчшщыьэюя"

def count_bigrams(text, intersection):
    bigrams_number = len(text2) - 1 if intersection else len(text) // 2
    bigrams = [(i + j) for (i, j) in zip(text[0::1 if intersection else 2], text[1::1 if intersection else 2])]
    coun = Counter(bigrams)
    frequencies = {i: coun[i] / bigrams_number for i in coun}
    return frequencies


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
        if b%d!=0:
            return []
        else:
            x0=b/d*inverse_element(a/d)%m
            return [x0+m/d*i for i in range(d)]

def letters_from_upper_letter(x):
    return alphabet[int((x-x%len(alphabet))/len(alphabet))]+alphabet[x%len(alphabet)]

def decipher_afin_bigrams(a, b, text):
    bigrams = [(i + j) for (i, j) in zip(text[0::2], text[1::2])]
    for i in bigrams:
        x = inverse_element(a, pow(len(alphabet),2))*(upper_letter(i[0], i[1])-b)%pow(len(alphabet),2)
        print(letters_from_upper_letter(x), end='')




f=open('text/V1', 'r')
line=f.readlines()[0]
x=count_bigrams(line, False)
x={k: v for k, v in sorted(x.items(), key=lambda item: item[1])[::-1]}
first_elements = [i[0] for i in list(x.items())[:5]]
five_most_often = ["ст", "но", "то", "на", "ен"]
#print(upper_letter("б", "а"))
a = solve_linear(upper_letter(five_most_often[0][0], five_most_often[0][1])-upper_letter(five_most_often[1][0], five_most_often[1][1]), upper_letter(first_elements[0][0], first_elements[0][1])-upper_letter(first_elements[1][0], first_elements[1][1]), pow(len(alphabet), 2))
b = (upper_letter(first_elements[0][0], first_elements[0][1])-a[0]*upper_letter(five_most_often[0][0], five_most_often[0][1]))%pow(len(alphabet), 2)
#decipher_afin_bigrams(a[0], b, line)
print(extended_euclid(133432,803429054))
