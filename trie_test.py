while True:
    try:
        N = int(input())
        string = [input().strip() for _ in range(N)]
    except EOFError:
        break

    real_trie = {}

    for word in string:
        node = real_trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['*'] = True

    index = 1
    build = ""
    media = 0
    trie = real_trie
    for word in string:
        for char in word:
            build += char
            if build == word:
                break
            if len(trie[char]) > 1:
                index += 1
            trie = trie[char]
        media = media + index
        index = 1
        build = ""
        trie = real_trie

    print(f"{media / len(string):.2f}")
