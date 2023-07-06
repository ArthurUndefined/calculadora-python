def main():
    expressão = input("Digite a expressão matematica:").split(" ")
    
    def inserirResultado(index, resultado):
            for x in range(3):
                expressão.pop(index-1)
            expressão.insert(index-1, resultado)
            operacoes()

    def operacoes():
        if "*" in expressão:
            index = expressão.index("*")
            resultado = int(expressão[index-1]) * int(expressão[index+1])
            inserirResultado(index, resultado)

        if "/" in expressão:
            index = expressão.index("/")
            resultado = int(expressão[index-1]) / int(expressão[index+1])
            inserirResultado(index, resultado)

        if "+" in expressão:
            index = expressão.index("+")
            resultado = int(expressão[index-1]) + int(expressão[index+1])
            inserirResultado(index, resultado)

        if "-" in expressão:
            index = expressão.index("-")
            resultado = int(expressão[index-1]) - int(expressão[index+1])
            inserirResultado(index, resultado)

    operacoes()
    
    print(expressão)

main()