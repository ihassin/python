from markov import Markov, get_table

m = Markov('i will try to use this buggy program to predict what the next letter is')
b = m.predict('b')

print('<' + b + '>')
