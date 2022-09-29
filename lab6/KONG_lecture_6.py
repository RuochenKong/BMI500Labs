from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import nltk
from nltk.corpus import brown

from pickle import dump, load


def pre_process(fn):
    f = open('texts/%s' % fn)
    content = f.read().lower()
    f_out = open('p_%s' % fn, 'w')
    f_out.write(content)
    f.close()
    f_out.close()


def jaccard_similarity(s1, s2):
    num_intersect = 0
    num_union = len(s1)
    for v1, v2 in zip(s1, s2):
        if v1 * v2 > 0:
            num_intersect += 1

    return num_intersect / num_union


def problem1():
    pre_process('text1')
    pre_process('text2')

    text = [open('p_text1').read(), open('p_text2').read()]

    vectorizer = CountVectorizer(ngram_range=(1, 3))
    v_t1, v_t2 = vectorizer.fit_transform(text)

    cosine = cosine_similarity(v_t1, v_t2).item()
    jaccard = jaccard_similarity(v_t1.toarray().flatten(), v_t2.toarray().flatten())

    print('##### Problem 1 #####')
    print('Cosine similarity: %.4f' % cosine)
    print('Jaccard similarity: %.4f' % jaccard)


def save_tagger(tagger, name: str):
    f_out = open('%s.pkl' % name, 'wb')
    dump(tagger, f_out, -1)
    f_out.close()


def load_tagger(name: str):
    f_in = open('%s.pkl' % name, 'rb')
    tagger = load(f_in)
    f_in.close()
    return tagger


def train_taggers():
    brown_tagged_sents = brown.tagged_sents(categories='news')
    brown_size = len(brown_tagged_sents)
    train_size = int(brown_size * 0.9)
    train_sents = brown_tagged_sents[:train_size]
    val_sents = brown_tagged_sents[train_size:]

    unigram_tagger = nltk.UnigramTagger(train_sents)
    bigram_tagger = nltk.BigramTagger(train_sents)
    default_tagger = nltk.DefaultTagger('NN')
    t1 = nltk.UnigramTagger(train_sents, backoff=default_tagger)
    combined_tagger = nltk.BigramTagger(train_sents, backoff=t1)

    save_tagger(unigram_tagger, 'unigram')
    save_tagger(bigram_tagger, 'bigram')
    save_tagger(combined_tagger, 'combine')

    eval_unigram = unigram_tagger.accuracy(val_sents)
    eval_bigram = bigram_tagger.accuracy(val_sents)
    eval_combined = combined_tagger.accuracy(val_sents)

    print('Accuracy achieved by Unigram tagger: %.4f' % eval_unigram)
    print('Accuracy achieved by Bigram tagger: %.4f' % eval_bigram)
    print('Accuracy achieved by Combined tagger: %.4f' % eval_combined)


def test_taggers():
    trained_tagger = load_tagger('combine')

    text1_origin = nltk.word_tokenize(open('texts/text1').read())
    text1_lower = nltk.word_tokenize(open('p_text1').read())

    origin_tag = trained_tagger.tag(text1_origin)
    lower_tag = trained_tagger.tag(text1_lower)

    print('Tags for Origin text1:')
    print(origin_tag)
    print()
    print('Tags for Lower cased text1:')
    print(lower_tag)


def problem2():
    print('##### Problem 2 #####')
    train_taggers()
    test_taggers()


if __name__ == '__main__':
    problem1()
    problem2()
