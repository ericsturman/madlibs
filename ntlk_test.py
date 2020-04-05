import nltk
# nltk.download('punkt')
sentence = """At eight o'clock on Thursday morning ... Arthur didn't feel very good."""
tokens = nltk.word_tokenize(sentence)
print(tokens)
# nltk.download('averaged_perceptron_tagger')
tagged = nltk.pos_tag(tokens)
print(tagged[0:6])
# nltk.download('tagsets')
# nltk.help.upenn_tagset()
# tagdict = load("help/tagsets/upenn_tagset.pickle")
