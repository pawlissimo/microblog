def read_file():
    res = []
    with open('words.txt', 'r') as f:
        lines = f.readlines()
        words = [l.split(' ') for l in lines]
        res.extend(words[0])

    # print(res)
    return res

def parse_words(words, size=3):
    res = [] # list of sets
    if words:
        for idx in range(words.__len__()):
            res.append(set(words[idx:idx+size]))
    # print(res)
    return res

def analyze_words(words):
    max_qty = 0
    max_set = None

    if words:
        max_set = words[0]
        curr_qty = 1
        for i1 in range(words.__len__()):
            curr_qty = 1
            for i2 in range(i1+1, words.__len__()):
                if words[i1] == words[i2]:
                    curr_qty += 1

            if curr_qty > max_qty:
                max_qty = curr_qty
                max_set = words[i1]

    print('Max qty: {} for set: {}'.format(max_qty, max_set))
    return max_set, max_qty


def main():
    words = read_file()
    res = parse_words(words)
    analyze_words(res)


if __name__ == '__main__':
    main()