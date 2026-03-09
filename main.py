from linked_list import ListaLigada

def main():
    minha_lista = ListaLigada()

    print("--- Inserindo Elementos ---")
    minha_lista.insert_start(10)
    minha_lista.insert_end(20)
    minha_lista.insert_end(30)
    minha_lista.insert_start(5)
    minha_lista.insert_end(40)

    print("Estado atual da lista:")
    minha_lista.display()

    print("\nRemovendo o valor 20")
    minha_lista.remove(20)
    minha_lista.display()

    print("\nBuscando valor")
    print(minha_lista.search(30))

    print(minha_lista.search(100))

main()