import sys

MAX_GRAM = 4

def make_n_gram(words, n):
    lenw = len(words)
    words = ["BBBB"] * (n-1) + words + ["EEEE"] * (n-1)
#    print "9:", words
    ngrams = []

    for i in range(lenw):
        str = ""
        for j in range(n):
            str += words[i + j] + "_"
        str = str[:-1]
        ngrams.append(str)
        i += n
#    print "17:", ngrams
    return ngrams

def make_all_n_gram(datas):
    all_words = len(datas)
    all_ngram = [[] for i in range(4)]
    all_ngram_len = []
    all_ngram_score = []

    all_ngram[0] += make_n_gram(datas, 1)
    all_ngram[1] += make_n_gram(datas, 2)
    all_ngram[2] += make_n_gram(datas, 3)
    all_ngram[3] += make_n_gram(datas, 4)
#    print all_ngram[0]
#    print all_ngram[1]
#    print all_ngram[2]
#    print all_ngram[3]

    for i in range(4):
        all_ngram_len.append(get_uniq_length(all_ngram[i]))
        all_ngram_score.append(all_ngram_len[i] * 1.0 / all_words)

    return all_ngram, all_ngram_len, all_words, all_ngram_score

def get_uniq_length(ngram):
#    print ngram
#    print set(ngram)
    return len(list(set(ngram)))

def uniq_n_gram_length(words, n):
    ngrams = make_n_gram(words, n)
    return len(list(set(ngrams)))

def distinct(words):
    dis = []

    #dis.append(uniq_n_gram_length(words, 1))
    #dis.append(uniq_n_gram_length(words, 2))
    #dis.append(uniq_n_gram_length(words, 3))
    #dis.append(uniq_n_gram_length(words, 4))

    word_count = len(words)
    if 0 == word_count:
        return [], 0, []
    dis_score = []

    for diss in dis:
        dis_score.append(diss * 1.0 / word_count)

    return dis, word_count, dis_score

def readinput():
    datas = []
    for line in sys.stdin:
        words = line.strip().split()
        datas.append(words)
    return datas

def readinput(k):
    datas = []
    count = 0
    for line in sys.stdin:
        words = line.strip().split()
        if len(words) == 0:
            count = 0
            continue
        if count >= k:
            continue
        count += 1
            
        datas.append(words)
    return datas

def deal_by_all(datas):
    dataall = []
    for data in datas:
        dataall += data
    ngram, dis, word_count, dis_score = make_all_n_gram(dataall)

    print("dis 1~4:", dis)
    print("word_count:", word_count)
    print("dis_score 1~4:", dis_score)

def main(argv):
    k = int(argv[1])
#    datas = readinput()
    datas = readinput(k)
    deal_by_all(datas)

if "__main__" == __name__:
    main(sys.argv)