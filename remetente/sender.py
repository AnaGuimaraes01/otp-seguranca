def repetir_chave(chave, tamanho):
    return (chave * ((tamanho // len(chave)) + 1))[:tamanho]

with open("/dados/mensagem.txt") as f:
    mensagem = f.read()

with open("/dados/chave.txt") as f:
    chave = f.read()

chave_expandida = repetir_chave(chave, len(mensagem))

criptografado = ""

for m, k in zip(mensagem, chave_expandida):
    criptografado += chr(ord(m) ^ ord(k))

with open("/dados/criptografado.txt", "w", encoding="latin1") as f:
    f.write(criptografado)

print("Mensagem criptografada com sucesso!")