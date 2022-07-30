import langid
from langdetect import detect
from langid.langid import LanguageIdentifier, model
from spacy_langdetect import LanguageDetector
from textblob import TextBlob
import numpy as np
from typing import List
from urllib.error import HTTPError
lang_identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)
import rowordnet as rwn
import spacy
from tqdm import tqdm


class TrieNode:
    """A node in the trie structure"""

    def __init__(self, char):
        # the character stored in this node
        self.char = char

        # whether this can be the end of a word
        self.is_end = False

        # a counter indicating how many times a word is inserted
        # (if this node's is_end is True)
        self.counter = 0

        # a dictionary of child nodes
        # keys are characters, values are nodes
        self.children = {}


class Trie(object):
    """The trie object"""

    def __init__(self):
        """
        The trie has at least the root node.
        The root node does not store any character
        """
        self.root = TrieNode("")

    def insert(self, word):
        """Insert a word into the trie"""
        node = self.root

        # Loop through each character in the word
        # Check if there is no child containing the character, create a new child for the current node
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                # If a character is not found,
                # create a new node in the trie
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        # Mark the end of a word
        node.is_end = True

        # Increment the counter to indicate that we see this word once more
        node.counter += 1

    def dfs(self, node, prefix):
        """Depth-first traversal of the trie

        Args:
            - node: the node to start with
            - prefix: the current prefix, for tracing a
                word while traversing the trie
        """
        if node.is_end:
            self.output.append((prefix + node.char, node.counter))

        for child in node.children.values():
            self.dfs(child, prefix + node.char)

    def query(self, x):
        """Given an input (a prefix), retrieve all words stored in
        the trie with that prefix, sort the words by the number of
        times they have been inserted
        """
        # Use a variable within the class to keep all possible outputs
        # As there can be more than one word with such prefix
        self.output = []
        node = self.root

        # Check if the prefix is in the trie
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                # cannot found the prefix, return empty list
                return []

        # Traverse the trie to get all candidates
        self.dfs(node, x[:-1])

        # Sort the results in reverse order and return
        return sorted(self.output, key=lambda x: x[1], reverse=True)


rwn = rwn.RoWordNet()
nlp = spacy.load("ro_core_news_sm")
def detect_language(text: str, detection_options: List[str] = ["lang_detect", "text_blob", "lang_identifier"]):
    if not len(text) or text is None:
        raise Exception("Text cannot be empty string or None")

    if " " not in text:
        synsets = rwn.synsets(literal=text)
        if len(synsets):
            return "ro"

    detected_languages_list = []
    if "lang_detect" in detection_options:
        try:
            detected_languages_list.append(detect(text))
        except:
            pass

    if "text_blob" in detection_options:
        try:
            detected_languages_list.append(TextBlob(text).detect_language())
        except HTTPError:
            pass

    if "lang_identifier" in detection_options:
        try:
            detected_languages_list.append(lang_identifier.classify(text)[0])
        except:
            pass

    if len(detected_languages_list):
        return max(set(detected_languages_list), key=detected_languages_list.count)
    return "unknown"


romanian_words_set = set()

def correct_word(word):
    if word in romanian_words_set:
        return word
    else:
        lang = detect_language(word)
        if lang in ["en"]:
            return word
        else:
            pass


from Levenshtein import distance as levenshtein_distance


def main():
    # print(detect_language("Eu nu sunt aici."))
    words = ["coralac", "mier", "crae", "mrae"]
    good_form = ["corala", "miere", "care", "mare"]
    for (gf, w) in zip(good_form, words):
        print(levenshtein_distance(gf, w), gf, w)

    # for word in words:
    #     print(correct_word(word))
    nlp = spacy.load("ro_core_news_md")
    t = Trie()
    all_words = nlp.vocab.strings
    # t.insert(word)
    for w in words:
        similarities = []
        for word in tqdm(all_words):
            d = levenshtein_distance(w, word)
            similarities.append((word, d))
            if d == 1:
                break
        similarities = sorted(similarities, key=lambda x: x[1])
        print([tup[0] for tup in similarities if tup[0][0] == w[0] if tup[1] <= 2])
        # print([w_[0] for w_ in similarities[:10]])

    for word in words:
        query_result = t.query(word)
        word_exists = False
        for (query_word, _) in query_result:
            if query_word == word:
                print(f"{word} exists")
                word_exists = True
                break
        if not word_exists:
            print(f"{word} does not exist")


def demo_phunspell():
    import phunspell

    pspell = phunspell.Phunspell('ro_RO')
    print(pspell.lookup("crae"))
    print(pspell.lookup("care"))

    mispelled = pspell.lookup_list("El e cel crae a furat .".split(" "))
    print(mispelled)
    # contextualize
    for suggestion in pspell.suggest("crae"):
        # only distance 1 levenshtein, or 2 or what is the lowest possible
        print(levenshtein_distance(suggestion, "crae"), suggestion)

# train your own: https://github.com/neuspell/neuspell
# https://towardsdatascience.com/spelling-correction-how-to-make-an-accurate-and-fast-corrector-dc6d0bcbba5f
if __name__ == "__main__":
    # main()
    demo_phunspell()
