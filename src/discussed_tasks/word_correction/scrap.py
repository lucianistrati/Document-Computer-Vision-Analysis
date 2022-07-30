def get_from_moroco():
    pass

def get_from_wordnet():
    pass

import spacy

from src.discussed_tasks.word_corection import Trie
from tqdm import tqdm
def main():
    """
    ROMANIAN LANGUAGE HAS:
    DEX - 67.000
    DULR - 80.000

    take into account declination by doing lemmatization/stemming with spacy
    is there a library for declinations?

    ro_core_news_sm = 69893
    ro_core_news_md = 633781 probably with inflections
    ro_core_news_lg = 633797
    """

    pipelines = ["ro_core_news_sm", "ro_core_news_md", "ro_core_news_lg"]
    for pipeline in pipelines:
        nlp = spacy.load(pipeline)
        t = Trie()
        words = nlp.vocab.strings
        for word in tqdm(words):
            t.insert(word)


        # print(len(list(nlp.vocab.strings)))
        # print(type(nlp.vocab.strings[0]))

"""
two ways:
1. load a small model and perform lemmatization/stemming with spacy in order to check for declinations/conjugations
2. load a medium model and perform no lemmatization/stemming
3. don't load a large model, not worth it from a perspective of vocab size
"""

if __name__ == "__main__":
    main()
