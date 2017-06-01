from lib.natural_language_processing import *

if __name__ == "__main__":

    document = get_document()

    bigrams = zip(document, document[1:])
    transitions = defaultdict(list)
    for prev, current in bigrams:
        transitions[prev].append(current)

    random.seed(0)
    print "bigram sentences"
    for i in range(20):
        print i, generate_using_bigrams(transitions)
    print

    # trigrams

    trigrams = zip(document, document[1:], document[2:])
    trigram_transitions = defaultdict(list)
    starts = []

    for prev, current, next in trigrams:

        if prev == ".":              # if the previous "word" was a period
            starts.append(current)   # then this is a start word

        trigram_transitions[(prev, current)].append(next)

    print "trigram sentences"
    for i in range(20):
        print i, generate_using_trigrams(starts, trigram_transitions)
    print

    grammar = {
        "_S"  : ["_NP _VP"],
        "_NP" : ["_N",
                 "_A _NP _P _A _N"],
        "_VP" : ["_V",
                 "_V _NP"],
        "_N"  : ["data science", "Python", "regression"],
        "_A"  : ["big", "linear", "logistic"],
        "_P"  : ["about", "near"],
        "_V"  : ["learns", "trains", "tests", "is"]
    }

    print "grammar sentences"
    for i in range(20):
        print i, " ".join(generate_sentence(grammar))
    print

    print "gibbs sampling"
    comparison = compare_distributions()
    for roll, (gibbs, direct) in comparison.iteritems():
        print roll, gibbs, direct


    # topic MODELING

    for k, word_counts in enumerate(topic_word_counts):
        for word, count in word_counts.most_common():
            if count > 0: print k, word, count

    topic_names = ["Big Data and programming languages",
                   "Python and statistics",
                   "databases",
                   "machine learning"]

    for document, topic_counts in zip(documents, document_topic_counts):
        print document
        for topic, count in topic_counts.most_common():
            if count > 0:
                print topic_names[topic], count,
        print
