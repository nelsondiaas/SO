def main():

    lista = [{'felipe': [{'dvd': 2}, {'impressora': 8}]}]

    for item in range(len(lista)):
        key = lista[item].copy().popitem()[0]
        #recurso = lista[item][key][0].copy().popitem()[0]
        print(lista[item][key][0]['dvd'])
        #print(lista[item][key][0])
        #lista[item][key][0][recurso] = 1


    print(lista)


if __name__ == '__main__':
    main()