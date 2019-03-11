import random

class Markov:
    def __init__(self, data):
        self.table = get_table(data)

    def predict(self, data_in):
        options = self.table.get(data_in, {})
        if not options:
            raise KeyError(f'{data_in} not found')

        possibles = []
        for key in options:
            count = options[key]
            for i in range(count):
                possibles.append(key)

        return random.choice(possibles)


def get_table(data):
    """
    call get_table('ab')
    { 'a' : {'b' : 1} }
    """
    results = {}
    for i in range(len(data)-1):
        char = data[i]
        out = data[i+1]
        char_dict = results.get(char, {})
        char_dict.setdefault(out, 0)
        char_dict[out] += 1
        results[char] = char_dict

    return results
