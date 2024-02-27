import random



def build_markov_chain(text, chain={}):
    words = text.split()
    index = 1
    for word in words[index:]:
        key = words[index - 1]
        if key in chain:
            chain[key].append(word)
        else: 
            chain[key] = [word]
        index += 1

    return chain