from spell_parser import spell_parse
from collections import defaultdict

uni_dct = defaultdict(int)
bi_dct = defaultdict(int)


def calc_ngrams(w_correct):
    word = "^" + w_correct + "$"
    for i in range(len(word)-1):
        uni_dct[word[i]] += 1
        bi_dct[word[i]+word[i+1]] += 1


def write_to_file(dct, file_name):
    with open(file_name, "w") as out_f:
        for ngram, count in dct.items():
            out_f.write("{}:{}\n".format(ngram, count))


if __name__ == '__main__':
    d_lst = spell_parse("../data/misspelled-train.txt")
    for item in d_lst:
        for k in item["corrections"]:
            w_correct = item["corrections"][k]
            calc_ngrams(w_correct)

    ngram_dict = {"unigrams_tania":uni_dct, "bigrams_tania":bi_dct}
    for name, dct in ngram_dict.items():
        write_to_file(dct, name + ".txt")

