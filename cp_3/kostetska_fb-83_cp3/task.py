from collections import Counter

def count_bigrams(text2, intersection):
    bigrams_number = len(text2) - 1 if intersection else len(text2) // 2
    bigrams = [(i + j) for (i, j) in zip(text2[0::1 if intersection else 2], text2[1::1 if intersection else 2])]
    coun = Counter(bigrams)
    frequencies2 = {i: coun[i] / bigrams_number for i in coun}
    # frequencies2 = {i: bigrams.count(i) / bigrams_number for i in sorted(set(bigrams))} # very slow
    return frequencies2


def euclid(a, b):
    if b==0:
        return abs(a)
    else:
        return euclid(b, a%b)

def extended_euclid(a, b):
    if b==0:
        return [0, 1, abs(a)]
    u1, v1, gcd = extended_euclid(b, a%b)
    return [v1-a//b*u1, u1, gcd]


def inverse_element(a, n):
    v,u,gcd=extended_euclid(a,n)
    if gcd==1:
        return u


f=open('text/V1', 'r')
line=f.readlines()[0]
x=count_bigrams(line, False)
print({k: v for k, v in sorted(x.items(), key=lambda item: item[1])[::-1]})
