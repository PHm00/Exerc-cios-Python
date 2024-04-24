from Exercicios import Exercicios

class Control:
    def __init__(self):
        self.opcao = -1
        self.exer = Exercicios()


    def coletar(self):
        self.exer.num1 = int(input("informe o primeiro número: "))
        self.exer.num2 = int(input("informe o segundo número: "))

    def coletarUm(self):
        self.exer.num1 = int(input("informe o primeiro número: "))

    def menu(self):
            self.opcao = int(input("----- Menu ----- \n\n" +
                                  "\n0. Sair"               +
                                  "\n1. Somar"              +
                                  "\n2. Subtrair"           +
                                  "\n3. Dividir"            +
                                  "\n4. Multiplicar"        +
                                  "\n5. Imprimir 1 a 10 Números" +
                                  "\n6. Pares um a Vinte" +
                                  "\n7. Somar de 1 a 100" +
                                  "\n8. multiplo de 5" +
                                  "\n9. par e impar" +
                                  "\n10. número positivo ou negativo"    +
                                  "\n11. tabuada do número digitado "    +
                                  "\n12. Contar até Número digitado "    +
                                  "\n13. Somar Até numero digitado"      +
                                  "\n14. Imprimir números primos 1 a 20" +
                                  "\n15. Verificar se é primo "          +
                                  "\n16. Calcular fatorial "             +
                                  "\n17. Sequencia Fibonacci"            +
                                  "\n18. Verificar se é Fibonacci"       +
                                  "\nEscolha uma das opções acima: "))

    def operacao(self):
        while(self.opcao != 0):
            self.menu() #mostrar menu
            if(self.opcao == 0):
                print("Obrigado!")
            elif(self.opcao == 1):
                self.coletar()
                print(self.exer.somar())
            elif (self.opcao == 2):
                self.coletar()
                print(self.exer.subtrair())
            elif (self.opcao == 3):
                self.coletar()
                print(self.exer.dividir())
            elif (self.opcao == 4):
                self.coletar()
                print(self.exer.multiplicar())
            elif (self.opcao ==5):
                print(self.exer.mostrar1a10())
            elif(self.opcao ==6):
                print(self.exer.paresUmAVinte())
            elif(self.opcao ==7):
                print(self.exer.somar1Ate100())
            elif(self.opcao ==8):
                print(self.exer.multiplo5())
            elif(self.opcao ==9):
                print(self.exer.parImpar())
            elif(self.opcao ==10):
                self.coletar()
                print(self.exer.positivoNegativo())
            elif(self.opcao ==11):
                self.coletar()
                print(self.exer.tabuada)
            elif(self.opcao ==12):
                self.coletarUm()
                print(self.exer.contarAteNum())
            elif (self.opcao == 13):
                self.coletarUm()
                print(self.exer.somarAteNum())
            elif (self.opcao == 14):
                print(self.exer.primosAte20())
            elif (self.opcao == 15):
                 self.coletarUm()
                 print(self.exer.verificarPrimo())
            elif(self.opcao == 16):
                self.coletarUm()
                print(self.exer.fatorial())
            elif(self.opcao == 17):
                print(self.exer.sequenciaFibonacci())
            elif(self.opcao == 18):
                self.coletarUm()
                print(self.exer.verificarFibonacci())

            else:
                print("Código escolhido não é válido!")
