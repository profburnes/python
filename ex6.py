import os;
os.system("cls");
print("---------------- Programa Chinês ---------------------");
# funcao para saber o valor as parcelas
def calcularParcela(produto, valor, parcelas):
    valor = float(valor);
    parcelas = int(parcelas);
    valorParcela = valor / parcelas;
    print(f"O valor das parcelas do produto {produto} são de R$ {valorParcela:.2f}");

produto = input("Digite o nome do produto: ");
valor = input("Digite o valor do produto: ");
parcelas = input("Digite as parcelas: ");

# chamar a função calcularParcela
calcularParcela(produto, valor, parcelas);

