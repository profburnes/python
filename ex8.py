import os;
os.system("cls");
print("-------------- Programa de Média --------------------");
def calcularMedia():
    disciplina = input("Disciplina: ");
    nota1 = float(input("Nota 1 Bim: "));
    nota2 = float(input("Nota 2 Bim: "));
    media = ( nota1 + nota2 ) / 2;
    if (media >= 7):
        print(f"Sua média é de {media:.1f} e vc foi APROVADO na disciplina de {disciplina}");
    else:
        print(f"Sua média é de {media:.1f} e vc foi REPROVADO na disciplina de {disciplina}");
    print("--------------------------------------------");
    resposta = input("Você deseja sair do Programa [S e Enter para sair] ou qualquer outra tecla e Entrer para Continuar.");
    if (resposta == "S"):
        print("Tchau!");
    else:
        calcularMedia();

calcularMedia();