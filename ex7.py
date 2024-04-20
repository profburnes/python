import os;
os.system("cls");
print("--------- Programa Chinês ---------");
# funcao para calular parcelas
def calcularParcelas():
    produto = input("Produto: ");
    valor = float(input("Valor: "));
    parcelas = int(input("Número de Parcelas: "));
    juros = float(input("Juros Mensal: "));
    # calcular as parcelas
    valorParcela = valor / parcelas;
    total = 0;
    for i in range(1, parcelas + 1):
        if (i > 1):
            valorParcela = valorParcela + ( valorParcela * juros / 100 );
        total = total + valorParcela;
        print(f"Parcela {i}: R$ {valorParcela:.2f}");
    print(f"O valor total é de R$ {total:.2f}");
    print("----------------------------------------------");
    resposta = input("Você deseja sair[S + Enter] ou continuar[Qualquer Tecla + Enter]?");
    if (resposta == "S"):
        print("Tchauzinho fofinho(a)");
    else:
        calcularParcelas();

calcularParcelas();