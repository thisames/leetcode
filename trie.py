# Função para criar uma nova trie
def create_trie():
    return {}


# Função para inserir uma palavra na trie
def insert(trie, word):
    node = trie
    for char in word:
        if char not in node:
            node[char] = {}
        node = node[char]
    # Usamos um marcador especial para indicar o final de uma palavra
    node['*'] = True


# Função para buscar uma palavra na trie
def search(trie, word):
    node = trie
    for char in word:
        if char not in node:
            return False
        node = node[char]
    # Verifica se chegamos ao final da palavra
    return '*' in node


# Função para verificar se existe algum prefixo na trie
def starts_with(trie, prefix):
    node = trie
    for char in prefix:
        if char not in node:
            return False
        node = node[char]
    return True


# Cria a trie
trie = create_trie()

# Insere palavras
insert(trie, "hello")
insert(trie, "hell")
insert(trie, "heaven")

print(trie)
