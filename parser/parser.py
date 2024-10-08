import nltk
import sys

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> NP VP Conj NP VP | NP P NP | NP P NP P NP | NP VP | S Conj S | S P S | NP VP Conj VP 
NP -> N | Det N | Det AdjP N | Det N PP | Det AdjP N PP
VP -> V | V NP | V NP PP | V PP | Adv VP | VP Adv
PP -> P NP
AdjP -> Adj | Adj AdjP
"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    sentence = str(sentence).lower()
    alpha = "abcdefghiklmnopqrstuvwxyz"
    a = nltk.casual_tokenize(sentence)
    for i in a:
        count = 0
        for j in alpha:
            if j in i:
                count += 1
        if count <1:
            a.remove(i)
    return a
        

def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    chunks = []
    
    def check(sub):
        if sub.label() != "NP":
            return False
        for i in sub:
            if isinstance(i,nltk.Tree):
               if i.label == "VP":
                    for a in i.subtrees:
                        if a.label == "PP" or a.label == "NP":
                            return False
               elif i.label() == "NP" or i.label() == "PP":
                    return False
        return True

    for sub in tree.subtrees():
        if check(sub):
            chunks.append(sub)
    return chunks

    


if __name__ == "__main__":
    main()


