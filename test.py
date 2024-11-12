# Representação visual da Trie:

#
#            ''
#          /    \
#        'h'     'g'  h - 1
#       /        /
#     'e'      'o'      he - 1
#    /   \        \
#  'l'   'a'      'o'    hell - 2
#  /      |         \
# 'l'    'v'        'd'   hello - 3
#  |      |         /
# 'o'    'e'      'b'
#  |      |       /
#  *      *     'y'
#               |
#              'e'
#               |
#               *
#
# - Os asteriscos ('*') indicam o final de uma palavra.
# - Exemplo de palavras contidas: "hello", "he", "haven", "goodbye"


trie = {
    'h': {

        'e': {'l': {'l': {'o': {'*': True}, '*': True}},

              'a': {'v': {'e': {'n': {'*': True}}}}}
    },

    'g': {'o': {'o': {'d': {'b': {'y': {'e': {'*': True}}}}}}}
}

# heaven
# healen
# hello
# hell, he + 1

string = "goodbye"
index = 1
build = ""

for i in string:
    build += i
    if build == string:
        break
    if len(trie[i]) > 1:
        index += 1
    trie = trie[i]

print(index)
print(build)
