from functions.functions import *


f=open('text/12.txt', 'r')
line=''.join(f.readlines()).replace('\n', '')
f.close()
x=sort_dict(count_bigrams(line, False))
first_elements = [i[0] for i in list(x.items())[:5]]
flag = 0

for i in itertools.permutations(five_most_often, 2):
    for j in itertools.permutations(first_elements, 2):
        print('-> X: '+str(i)+'; Y: '+str(j)+';')

        a, b=get_coefs(i, j)
        if len(a)<1:
            print('      error: coef a does not exist')

        for (ael, bel) in zip(a, b):
            print('   a: '+str(ael)+'; b: '+str(bel) )
            plaintext = decipher_afin_bigrams(ael, bel, line)

            if len(plaintext)>0 and is_plaintext(plaintext):
                print('      plaintext: '+plaintext[:100]+'...')

                if flag==0:
                    fileout = open('results/decrypted_12.txt', 'w')
                    fileout.write(plaintext)
                    fileout.close()
                    flag+=1
                    
                    #exit() #uncomment to end program on first plaintext found
        print()
