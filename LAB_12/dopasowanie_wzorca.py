import time


def naive(S, W):
    m = 0
    indexes = []
    counter = 0

    while m < len(S) - len(W) + 1:
        i = 0
        while i < len(W):
            counter += 1
            if S[m + i] == W[i]:
                i += 1
                if i == len(W):
                    indexes.append(m)
            else:
                break
        m += 1

    return indexes, counter

def hash(word, d = 256, q = 101):
    hw = 0
    for i in range(len(word)):
        hw = (hw*d + ord(word[i])) % q
    return hw

def rabin_karp(S, W, d = 256, q = 101):
    m = 0
    indexes = []
    counter = 0
    counter_colisions = 0
    w_len = len(W)
    hW = hash(W, d, q)

    while m < len(S):
        if len(S[m:m+w_len]) < w_len:
            break
        hS = hash(S[m:m+w_len], d, q)
        counter += 1
        if hS == hW:
            if S[m:m+w_len] == W:
                indexes.append(m)
            else:
                counter_colisions += 1
        m += 1

    return indexes, counter, counter_colisions

def rabin_karp_rolling_hash(S, W, d = 256, q = 101):
    m = 0
    indexes = []
    counter = 0
    counter_colisions = 0
    w_len = len(W)
    hW = hash(W, d, q)

    h = 1
    for i in range(w_len - 1):
        h = (h * d) % q
    hs = 0
    while m < len(S) - w_len + 1:
        if m == 0:
            hS = hash(S[m:m + w_len], d, q)
        else:
            hS = (d * (hS - ord(S[m - 1]) * h) + ord(S[m + w_len - 1])) % q
        if hs < 0:
            hs += q
        counter += 1
        if hS == hW:
            if S[m:m + w_len] == W:
                indexes.append(m)
            else:
                counter_colisions += 1
        m += 1

    return indexes, counter, counter_colisions

def kmp_search(S, W):
    m = 0
    i = 0
    indexes = []
    counter = 0
    T = kmp_table(W)
    while m < len(S):
        counter += 1
        if S[m] == W[i]:
            m += 1
            i += 1
            if i == len(W):
                indexes.append(m - i)
                i = T[i - 1]
        else:
            i = T[i]
            if i<0:
                m += 1
                i += 1

    return indexes, counter, T

def kmp_table(W):
    pos = 1
    cnd = 0
    T = [0 for x in range(len(W))]

    T[0] = -1
    while pos < len(W):
        if W[pos] == W[cnd]:
            T[pos] = T[cnd]
        else:
            T[pos] = cnd
            while cnd >= 0 and W[pos] != W[cnd]:
                cnd = T[cnd]
        pos += 1
        cnd += 1

    return T


def main():
    with open("lotr.txt", encoding='utf-8') as f:
        text = f.readlines()

    text = ' '.join(text).lower()
    wzor = 'time.'.lower()
    #text = 'ABC ABCDAB ABCDABCDABDE'
    #wzor = 'ABCDABD'

    t_start = time.perf_counter()
    idxs, porow = naive(text, wzor)
    t_stop = time.perf_counter()
    print(f"{len(idxs)} {porow} {t_stop - t_start:.7f}")

    t_start = time.perf_counter()
    idxs, porow, colisions = rabin_karp(text, wzor)
    t_stop = time.perf_counter()
    print(f"{len(idxs)} {porow} {colisions} {t_stop - t_start:.7f}")

    t_start = time.perf_counter()
    idxs, porow, colisions = rabin_karp_rolling_hash(text, wzor)
    t_stop = time.perf_counter()
    print(f"{len(idxs)} {porow} {colisions} {t_stop - t_start:.7f}")

    t_start = time.perf_counter()
    idxs, porow, T = kmp_search(text, wzor)
    t_stop = time.perf_counter()
    print(f"{len(idxs)} {porow} {T}")

if __name__ == "__main__":
    main()