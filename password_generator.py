import random
import string

def gerar_senha(tamanho=12):
    """Gera uma senha segura com letras, números e caracteres especiais."""
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

if __name__ == "__main__":
    print("🔐 Gerador de Senhas Seguras")
    try:
        tamanho = int(input("Digite o tamanho da senha desejada: "))
        if tamanho < 4:
            print("A senha deve ter pelo menos 4 caracteres.")
        else:
            senha = gerar_senha(tamanho)
            print(f"🔑 Sua senha gerada: {senha}")
    except ValueError:
        print("Erro: Digite um número válido para o tamanho da senha.")
