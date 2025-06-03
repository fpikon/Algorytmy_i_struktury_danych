import time

def hash(word, d = 256, q = 101):
    hw = 0
    for i in range(len(word)):
        hw = (hw*d + ord(word[i])) % q
    return hw

def rabin_karp(S, W_list, d = 256, q = 101):
    indexes = {W: [] for W in W_list}
    counter_colisions = 0
    hW_set = set()
    w_len_set = {len(W) for W in W_list}

    for W in W_list:
        hW = hash(W, d, q)
        hW_set.add(hW)

    for w_len in w_len_set:
        h = 1
        for i in range(w_len - 1):
            h = (h * d) % q
        hs = 0
        m = 0
        while m < len(S) - w_len + 1:
            a = S[m:m + w_len]
            if m == 0:
                hS = hash(S[m:m + w_len], d, q)
            else:
                hS = (d * (hS - ord(S[m - 1]) * h) + ord(S[m + w_len - 1])) % q
            if hs < 0:
                hs += q
            if hS in hW_set:
                if S[m:m + w_len] in W_list:
                    indexes[S[m:m + w_len]].append(m)
                else:
                    counter_colisions += 1
            m += 1

    return indexes, counter_colisions

def main():
    with open("lotr.txt", encoding='utf-8') as f:
        text = f.readlines()

    text = ' '.join(text).lower()
    wzory = ['gandalf', 'looking', 'blocked', 'comment', 'pouring', 'finally', 'hundred', 'hobbits', 'however', 'popular',
     'nothing', 'enjoyed', 'stuffed', 'relaxed', 'himself', 'present', 'deliver', 'welcome', 'baggins', 'further']

    nr_testu = input()

    if nr_testu == '1':
        test_1(text, wzory)
    elif nr_testu == '2':
        test_2(text, wzory)

def test_1(text, wzory):
    t_start = time.perf_counter()
    rabin_karp(text, [wzory[0]])
    t_stop = time.perf_counter()
    print(f"{t_stop - t_start:.7f}")

    t_start = time.perf_counter()
    rabin_karp(text, wzory)
    t_stop = time.perf_counter()
    print(f"{t_stop - t_start:.7f}")

def test_2(text, wzory):
    found, colisions = rabin_karp(text, wzory)

    found_sum = 0
    for w, idx in found.items():
        print(w, len(idx))
        found_sum += len(idx)
    print(found_sum)
    print(colisions)


if __name__ == "__main__":
    main()