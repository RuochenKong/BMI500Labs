from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


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
    print('Cosine similarity: %.4f'%cosine)
    print('Jaccard similarity: %.4f'%jaccard)


