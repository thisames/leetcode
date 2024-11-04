# Função para criar um novo nó
def create_node(data):
    return {'data': data, 'next': None}


# Função para verificar se a lista está vazia
def is_empty(head):
    return head is None


# Função para adicionar um novo nó no final da lista
def append(head, data):
    new_node = create_node(data)
    if is_empty(head):
        return new_node  # O novo nó se torna a cabeça da lista
    else:
        current = head
        while current['next']:  # Percorre até o último nó
            current = current['next']
        current['next'] = new_node
    return head


# Função para exibir todos os elementos da lista
def display(head):
    if is_empty(head):
        print("A lista está vazia.")
    else:
        current = head
        while current:
            print(current['data'], end=" -> ")
            current = current['next']
        print("None")


# Função para remover o primeiro nó que contém o valor especificado
def remove(head, data):
    if is_empty(head):
        print("A lista está vazia.")
        return head

    if head['data'] == data:
        return head['next']  # Remover o primeiro nó (cabeça)

    current = head
    previous = None
    while current and current['data'] != data:
        previous = current
        current = current['next']

    if current is None:
        print(f"Valor {data} não encontrado.")
        return head

    previous['next'] = current['next']  # Remover o nó encontrado
    return head


# Exemplo de uso
head = None
head = append(head, 1)
head = append(head, 2)
head = append(head, 3)

print("Conteúdo da lista ligada:")
display(head)

print("Removendo o valor 2:")
head = remove(head, 2)

print("Conteúdo da lista após remoção:")
display(head)
