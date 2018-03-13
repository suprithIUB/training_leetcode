from functools import total_ordering
class WordFrequency:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def _is_valid_operand(self, other):
        return (hasattr(other, "word") and hasattr(other, "freq"))

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return ((self.freq, self.word) == (other.freq, other.word))

    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return ((self.freq, self.word) < (other.freq, other.word))

if __name__ == "__main__":
    import heapq
    l = []
    one = WordFrequency('suprith', -10)
    l.append(one)
    d = {}
    d['suprith'] = one
    two = WordFrequency('bashi', -5)
    l.append(two)
    d['bashi'] = two
    heapq.heapify(l)
    for i in l:
        print(i.freq)
    d['bashi'].freq += -5

    heapq.heapify(l)
    for i in l:
        print(i.freq)
        print(i.word)
