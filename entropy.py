import math, sys, os.path

# https://rosettacode.org/wiki/Entropy#Python
def entropy(string):
        "Calculates the Shannon entropy of a string"
        
        # get probability of chars in string
        prob = [ float(string.count(c)) / len(string) for c in set(list(string)) ]

        # calculate the entropy
        entropy = - sum([ p * math.log(p, 2) for p in prob ])
        
        return entropy

arg = sys.argv[1]
if os.path.isfile(arg):
        arg = open(arg, 'r').read()

print(entropy(arg))
