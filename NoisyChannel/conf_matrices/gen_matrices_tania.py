# -*- coding: utf-8 -*-
from spell_parser import spell_parse
from collections import defaultdict

conf_matrix = defaultdict(int)


def fill_matrices(typo, correct):
    if ((typo[0].isupper() and correct[0].islower())
          or (typo[0].islower() and correct[0].isupper()))\
            and (typo[0].lower() == correct[0].lower()):
        # print "substitution", typo, correct
        # print correct[0], typo[0]
        conf_matrix[(correct[0], typo[0])] += 1
    typo = typo.lower()
    correct = correct.lower()

    if not " " in correct:
        typo = "^" + typo + "$"
        correct = "^" + correct + "$"
        i = 0
        j = 0
        while i < len(correct)-1 and j < len(typo)-1:
            if correct[i] != typo[j]:
                if correct[i+1] == typo[j] and correct[i+2] == typo[j+1]:
                    # print "deletion", typo, correct
                    # print correct[i-1:i+1], typo[j-1]
                    conf_matrix[(correct[i - 1:i + 1], typo[j - 1])] += 1
                    i += 1
                elif correct[i] == typo[j+1] and correct[i+1] == typo[j+2]:
                    # print "insertion", typo, correct
                    # print correct[i-1], typo[j-1:j+1]
                    conf_matrix[(correct[i - 1], typo[j - 1:j + 1])] += 1
                    j += 1
                elif correct[i+1] == typo[j+1]:
                    # print "substitution: ", typo, correct
                    # print correct[i], typo[j]
                    conf_matrix[(correct[i], typo[j])] += 1
                    i += 1
                    j += 1
                elif correct[i+1] == typo[j] and correct[i] == typo[j+1] and len(typo) == len(correct):
                    # print "transposition: ", typo, correct
                    # print correct[i:i+2], typo[j:j+2]
                    conf_matrix[(correct[i:i + 2], typo[j:j + 2])] += 1
                    i += 2
                    j += 2
                else:
                    # print "Smth is wrong: ", typo, correct
                    break
            else:
                i += 1
                j += 1
        if i == len(correct)-1 and j < len(typo)-1 and correct[:-1] == typo[:-2]:
            # print "insertion at the end: ", typo, correct
            # print correct[i], typo[j:j+2]
            conf_matrix[(correct[i], typo[j:j + 2])] += 1
        elif j == len(typo)-1 and j < len(correct)-1 and correct[:-2] == typo[:-1]:
            # print "deletion at the end: ", typo, correct
            # print correct[-2:], typo[-1]
            conf_matrix[(correct[-2:], typo[-1])] += 1


def write_to_file(dct, file_name):
    with open(file_name, "w") as out_f:
        for k in dct.keys():
            out_f.write("{}:{}~{}\n".format(str(k[0]), str(k[1]), str(dct[k])))

if __name__ == '__main__':
    # Generate matrices
    d_lst = spell_parse("data/misspelled-train.txt")
    for item in d_lst:
        for k in item["corrections"]:
            typo = item["sentence"][k]
            correct = item["corrections"][k]
            if abs(len(typo) - len(correct)) < 3:
                fill_matrices(typo, correct)
            # else:
            #     print "too distorted:\t{}\t{}".format(correct, typo)

    # Write generated matrix to file
    file_name = "confusion_matrices_tania.txt"
    write_to_file(conf_matrix, file_name)


    # Write generated matrices to corresponding files
    # matrices_dct = {"subst":subst, "delet":delet, "insert":insert, "transpos":transpos}
    # for name, dct in matrices_dct.items():
    #     file_name = "data/" + name + ".txt"
    #     write_to_file(dct, file_name)


    # travelling deletion y = e, x = v
    # travlling
    #
    # travelling insertion
    # trkavlling          y = k, x = r
    #
    # travelling   substitution x = i, y = e
    # travilling
    #
    # travelling    transposition x = v, y = e
    # traevlling
