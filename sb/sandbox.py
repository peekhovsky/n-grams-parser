import nltk


def test():
    text = "The quick brown fox jumps over the lazy dog."

    # tokenize the text into words
    tokens = nltk.word_tokenize(text)

    # generate bigrams
    bigrams = list(nltk.ngrams(tokens, 2))
    print(bigrams)


if __name__ == '__main__':
    print('running...')
    test()
