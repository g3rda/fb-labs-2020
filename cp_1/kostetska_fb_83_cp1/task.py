import math


def count_unigrams(text1):
    frequencies1 = {i: text1.count(i) / len(text1) for i in sorted(set(text1))}
    return frequencies1


def count_bigrams(text2, intersection):
    bigrams_number = len(text2) - 1 if intersection else len(text2) // 2
    bigrams = sorted(set([(i+j) for (i, j) in zip(text2[0::1 if intersection else 2], text2[1::1 if intersection else 2])]))
    frequencies2 = {i: text2.count(i) / bigrams_number for i in bigrams}
    # for i in frequencies2:
    #     print(i+": "+"{:.3f}".format(frequencies2[i]*100))
    return frequencies2


def entropy(frequencies):
    h = 0
    for i in frequencies:
        h -= frequencies[i] * math.log2(frequencies[i])
    h = h / len(list(frequencies.keys())[0])
    return h


def redundancy(h, letters_number):
    return 1 - (h / math.log2(letters_number))


def print_bigrams_table(fr, file):
    letters = 'абвгдежзийклмнопрстуфхцчшщыьэюя '
    table = [[0.0 for i in range(len(letters))] for i in range(len(letters))]
    for i in fr:
        table[letters.index(i[0])][letters.index(i[1])] = fr[i]
    file.write('   ')
    for i in letters:
        file.write('  '+i+'   ')
    file.write('\n')
    for i in table:
        file.write(letters[table.index(i)]+'  ')
        for j in i:
            file.write("{:.3f}".format(j*100)+' ')
        file.write('\n')


# print('Print name of the file with text: ', end='')
# file_to_open = input()
file_to_open = 'cleared_text.txt'

with open(file_to_open, 'r', encoding='utf-8') as file:
    text = file.readline()

text_no_spaces = text.replace(' ', '')

res_file = open('results.txt', 'w')


res_file.write('               FREQUENCIES                         \n')


res_file.write('---------------unigrams with spaces---------------\n')
fr_uni_with_spaces = count_unigrams(text)
for c in fr_uni_with_spaces:
    res_file.write(c + ": " + "{:.3f}".format(fr_uni_with_spaces[c]*100) + '\n')

res_file.write('---------------unigrams no spaces---------------\n')
fr_uni_no_spaces = count_unigrams(text_no_spaces)
for c in fr_uni_no_spaces:
    res_file.write(c + ": " + "{:.3f}".format(fr_uni_no_spaces[c]*100) + '\n')

res_file.write('---------------bigrams with spaces, intersection yes---------------\n')
fr_bi_with_spaces_yes = count_bigrams(text, True)
print_bigrams_table(fr_bi_with_spaces_yes, res_file)

res_file.write('---------------bigrams no spaces, intersection yes---------------\n')
fr_bi_no_spaces_yes = count_bigrams(text_no_spaces, True)
print_bigrams_table(fr_bi_no_spaces_yes, res_file)

res_file.write('---------------bigrams with spaces, intersection no---------------\n')
fr_bi_with_spaces_no = count_bigrams(text, False)
print_bigrams_table(fr_bi_with_spaces_no, res_file)

res_file.write('---------------bigrams no spaces, intersection no---------------\n')
fr_bi_no_spaces_no = count_bigrams(text_no_spaces, False)
print_bigrams_table(fr_bi_no_spaces_no, res_file)

res_file.write('                                         ENTROPY                         \n')
res_file.write('Unigrams with spaces:                                    '+str(entropy(fr_uni_with_spaces))+'\n')
res_file.write('Unigrams no spaces:                                      '+str(entropy(fr_uni_no_spaces))+'\n')
res_file.write('Bigrams with spaces, intersection yes:                   '+str(entropy(fr_bi_with_spaces_yes))+'\n')
res_file.write('Bigrams no spaces, intersection yes:                     '+str(entropy(fr_bi_no_spaces_yes))+'\n')
res_file.write('Bigrams with spaces, intersection no:                    '+str(entropy(fr_bi_with_spaces_no))+'\n')
res_file.write('Bigrams no spaces, intersection no:                      '+str(entropy(fr_bi_no_spaces_no))+'\n')

res_file.write('                                         REDUNDANCY                         \n')
res_file.write('Unigrams with spaces:                                    '+str(redundancy(entropy(fr_uni_with_spaces), 32))+'\n')
res_file.write('Unigrams no spaces:                                      '+str(redundancy(entropy(fr_uni_no_spaces), 31))+'\n')
res_file.write('Bigrams with spaces, intersection yes:                   '+str(redundancy(entropy(fr_bi_with_spaces_yes), 32))+'\n')
res_file.write('Bigrams no spaces, intersection yes:                     '+str(redundancy(entropy(fr_bi_no_spaces_yes), 31))+'\n')
res_file.write('Bigrams with spaces, intersection no:                    '+str(redundancy(entropy(fr_bi_with_spaces_no), 32))+'\n')
res_file.write('Bigrams no spaces, intersection no:                      '+str(redundancy(entropy(fr_bi_no_spaces_no), 31))+'\n')


res_file.close()
