import matplotlib.pyplot as plt
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# import nltk
# nltk.download("stopwords")

def word_frequency(text,language="english", top_n=10, save_plot=False):
    words = []
    stop_words = set(stopwords.words(language))
    for word in word_tokenize(text.lower()):
        if word.isalnum() and word not in stop_words:
            words.append(word)

    freq = Counter(words)
    top_words = freq.most_common(top_n)
    words, counts = zip(*top_words)

    plt.bar(words, counts)
    plt.title("Word Frequency")
    plt.xlabel("Words")
    plt.ylabel("Count")
    plt.xticks(rotation=45)  
    plt.tight_layout()
    if save_plot:
        plt.savefig("word_frequency.png")
    plt.show()

    return freq

text = """This is a simple text, just for analysis and testing! """
print(word_frequency(text))