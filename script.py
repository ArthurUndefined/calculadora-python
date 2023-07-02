def main():
    expressão = input("Digite a expressão matematica:").split(" ")
    
    def operacoes():
        if "*" in expressão:
            index = expressão.index("*")
            resultado = int(expressão[index-1]) * int(expressão[index+1])
            for x in range(3):
                expressão.pop(index-1)
            expressão.insert(index-1, resultado)
            operacoes()

        if "/" in expressão:
            index = expressão.index("/")
            resultado = int(expressão[index-1]) / int(expressão[index+1])
            for x in range(3):
                expressão.pop(index-1)
            expressão.insert(index-1, resultado)
            operacoes()

        if "+" in expressão:
            index = expressão.index("+")
            resultado = int(expressão[index-1]) + int(expressão[index+1])
            for x in range(3):
                expressão.pop(index-1)
            expressão.insert(index-1, resultado)
            operacoes()

        if "-" in expressão:
            index = expressão.index("-")
            resultado = int(expressão[index-1]) - int(expressão[index+1])
            for x in range(3):
                expressão.pop(index-1)
            expressão.insert(index-1, resultado)
            operacoes()

    operacoes()
    
    print(expressão)

main()