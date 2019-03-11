from markov import Markov, get_table

m = Markov('a lot of added additions text in this sentence')
b = m.predict('a')

print('<' + b + '>')
