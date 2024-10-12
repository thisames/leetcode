while True:
    try:
        N = int(input())
        words = [input().strip() for _ in range(N)]
        trie = {'children': {}, 'is_end': False}

        for word in words:
            node = trie
            for char in word:
                if char not in node['children']:
                    node['children'][char] = {'children': {}, 'is_end': False}
                node = node['children'][char]
            node['is_end'] = True

        total_key_presses = 0

        for word in words:
            node = trie
            key_presses = 0
            for i, char in enumerate(word):
                if i == 0:
                    key_presses += 1
                else:
                    if node['is_end'] or len(node['children']) > 1:
                        key_presses += 1
                node = node['children'][char]
            total_key_presses += key_presses

        average = total_key_presses / N
        print("{0:.2f}".format(round(average + 1e-8, 2)))
    except EOFError:
        break
