def repetir_chave(chave, tamanho):
    resultado = ""

    while len(resultado) < tamanho:
        resultado += chave

    return resultado[:tamanho]


with open("/dados/chave.txt") as f:
    chave = f.read().strip()

with open("/dados/mensagem.txt") as f:
    mensagem_original = f.read().strip()

with open("/dados/criptografado.txt", encoding="latin1") as f:
    criptografado = f.read()


tamanho_chave = len(chave)
possibilidades = 26 ** tamanho_chave

print("      ANÁLISE DO ATACANTE")
print("ESTIMATIVA DE FORÇA BRUTA")
print(f"Tamanho da chave: {tamanho_chave}")
print(f"Possibilidades: {possibilidades:,}\n")


print("FRAGILIDADES IDENTIFICADAS\n")

if len(chave) < len(mensagem_original):
    print("1. Chave menor que a mensagem")
    print("   -> A chave precisa ser repetida.\n")

print("2. Chave reutilizada")
print("   -> Um verdadeiro One-Time Pad utiliza a chave apenas uma vez.\n")

print("3. Chave armazenada em texto puro")
print("   -> O arquivo chave.txt pode ser acessado por terceiros.\n")

print("4. Redução da segurança")
print("   -> Chaves curtas diminuem o espaço de busca.\n")


print("SIMULAÇÃO DO ATAQUE\n")
print("Mensagem criptografada interceptada: ")
print(criptografado)
print()

print("O atacante encontrou o arquivo chave.txt.")
print(f"Chave obtida: {chave}\n")

chave_repetida = repetir_chave(chave, len(criptografado))

mensagem_recuperada = ""

for c, k in zip(criptografado, chave_repetida):
    mensagem_recuperada += chr(ord(c) ^ ord(k))

print("MENSAGEM RECUPERADA PELO ATACANTE")
print(mensagem_recuperada)
print()

if mensagem_recuperada == mensagem_original:
    print("RESULTADO DO ATAQUE")
    print("A criptografia foi quebrada com sucesso.")
    print("O atacante recuperou exatamente a mensagem original.")
else:
    print("Falha ao recuperar a mensagem.")

print("\nCONCLUSÃO: A implementação utilizada não segue os requisitos de um OTP perfeito. Por isso, tornou-se vulnerável e permitiu a recuperação da mensagem.")
