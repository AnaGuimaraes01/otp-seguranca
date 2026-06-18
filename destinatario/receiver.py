def repetir_chave(chave, tamanho):
    return (chave * ((tamanho // len(chave)) + 1))[:tamanho]

with open("/dados/criptografado.txt", encoding="latin1") as f:
    criptografado = f.read()

with open("/dados/chave.txt") as f:
    chave = f.read()

chave_expandida = repetir_chave(chave, len(criptografado))

mensagem = ""

for c, k in zip(criptografado, chave_expandida):
    mensagem += chr(ord(c) ^ ord(k))

print("Mensagem recuperada:")
print(mensagem)