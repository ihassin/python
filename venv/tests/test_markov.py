from markov import Markov


def test_markov_prediction():
    markov = Markov("Some text to test")
    predict = markov.predict('t')
    assert predict in [' ', 'e', 'o']
