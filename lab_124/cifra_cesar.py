# Duplica o alfabeto para evitar estouro de índice durante o deslocamento.
# Sem isso, letras como X, Y, Z com chave alta gerariam índices inválidos.
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

# Coleta a mensagem que o usuário deseja cifrar.
# Aceita qualquer string; letras minúsculas serão convertidas internamente.
def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt

# Coleta a chave de cifra: um inteiro entre 1 e 25 que define o deslocamento.
# Valores maiores que 25 funcionam, mas são equivalentes ao seu módulo por 26.
def getCipherKey():
    shiftAmount = input("Please enter a key (whole number from 1-25): ")
    return shiftAmount

# Cifra uma mensagem pelo método de substituição de César.
# Parâmetros:
#   message   — texto original (maiúsculas ou minúsculas)
#   cipherKey — número inteiro de posições a deslocar no alfabeto
#   alphabet  — alfabeto de referência (deve ser o alfabeto duplicado)
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""

    # Converte para maiúsculas para garantir consistência com o alfabeto de referência
    uppercaseMessage = message.upper()

    for currentCharacter in uppercaseMessage:
        # Localiza a posição atual da letra no alfabeto (retorna -1 se não encontrada)
        position = alphabet.find(currentCharacter)

        # Aplica o deslocamento da chave para obter a nova posição
        newPosition = position + int(cipherKey)

        if currentCharacter in alphabet:
            # Substitui a letra pela letra na nova posição (cifra de César)
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            # Preserva caracteres não-alfabéticos (espaços, números, pontuação)
            encryptedMessage = encryptedMessage + currentCharacter

    return encryptedMessage

# Descriptografa uma mensagem cifrada pela cifra de César.
# Reutiliza encryptMessage() com a chave negada — deslocar para trás
# pelo mesmo valor desfaz exatamente o processo de cifragem.
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)

# Função principal: orquestra todo o fluxo do programa.
def runCaesarCipherProgram():
    # Define o alfabeto base em maiúsculas
    myAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')

    # Gera o alfabeto duplicado para suportar deslocamentos sem estouro de índice
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')

    # Coleta mensagem e chave do usuário
    myMessage = getMessage()
    print(f'Original message: {myMessage}')

    myCipherKey = getCipherKey()
    print(f'Cipher key: {myCipherKey}')

    # Cifra a mensagem e exibe o resultado
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted message: {myEncryptedMessage}')

    # Descriptografa a mensagem cifrada para verificar a reversibilidade do processo
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decrypted message: {myDecryptedMessage}')

runCaesarCipherProgram()