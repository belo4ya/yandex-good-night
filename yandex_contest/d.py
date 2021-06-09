import sys


def gen_bracket_sequences(n):

    def _generate(seq, opened, closed):
        if opened == n and closed == n:
            print(seq)
        else:
            if opened < n:
                _generate(seq + '(', opened + 1, closed)
            if closed < opened:
                _generate(seq + ')', opened, closed + 1)

    _generate('', 0, 0)


n = int(sys.stdin.readline().strip())
gen_bracket_sequences(n)
