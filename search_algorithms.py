def naive_search(text, pattern):
    n, m = len(text), len(pattern)
    matches, comparisons = [], 0

    for i in range(n - m + 1):
        j = 0
        while j < m:
            comparisons += 1
            if text[i + j] != pattern[j]:
                break
            j += 1

        if j == m:
            matches.append(i)

    return matches, comparisons


def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    lps = compute_lps(pattern)

    matches, comparisons = [], 0
    i = j = 0

    while i < n:
        comparisons += 1

        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            matches.append(i - j)
            j = lps[j - 1]

        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches, comparisons


def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)

    if m > n:
        return [], 0

    base = 256
    prime = 101

    pattern_hash = 0
    text_hash = 0

    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        text_hash = (base * text_hash + ord(text[i])) % prime

    matches, comparisons = [], 0

    for i in range(n - m + 1):
        comparisons += 1

        if pattern_hash == text_hash:
            if text[i:i+m] == pattern:
                matches.append(i)

        if i < n - m:
            text_hash = (
                base * (text_hash - ord(text[i]) * pow(base, m-1, prime))
                + ord(text[i + m])
            ) % prime

            if text_hash < 0:
                text_hash += prime

    return matches, comparisons
