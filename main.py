alfabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя123456789123456789'

def getMessage():
    return input('Введите сообщение: ').lower()

def chooseFunc(message):
    print('Если вам нужно зашифровать сообщение, введите 1')
    print('Если вам нужно разшифровать сообщение, введите 2')
    print('Если вам нужно взломать сообщение и узнать улюч, введите 3')
    choosed = int(input('Введите выбраное число: '))
    match choosed:
        case 1:
            encryptMessage(message)
        case 2:
            unencryptMessage(message)
        case 3:
            hackMessage(message)
    quit()

def hackMessage(message):
    key = 1
    unencryptedMessage = ''
    choosed = 0
    while True:
        for char in message:
            position = alfabet.rfind(char)
            newPosition = position - key
            if char in alfabet:
                unencryptedMessage += alfabet[newPosition]
            else:
                unencryptedMessage += char
        print('Расшифровка с ключом ' + str(key) + ': ' + unencryptedMessage)
        print('Если это правильная расшифровка, введите 1. Если нет - 2')
        choosed = int(input('Введите выбраное число: '))
        match choosed:
            case 1:
                print('Расшифрованый текст: ' + unencryptedMessage)
                break
            case 2:
                key += 1
                unencryptedMessage = ''
                continue

def getKey():
    return int(input('Введите ключ: '))

def encryptMessage(message):
    key = getKey()
    encryptedMessage = ''
    for char in message:
        position = alfabet.find(char)
        newPosition = position + key
        if char in alfabet:
            encryptedMessage += alfabet[newPosition]
        else:
            encryptedMessage = + char
    print('Зашифрованый текст: ' + encryptedMessage)

def unencryptMessage(message):
    key = getKey()
    unencryptedMessage = ''
    for char in message:
        position = alfabet.rfind(char)
        newPosition = position - key
        if char in alfabet:
            unencryptedMessage += alfabet[newPosition]
        else:
            unencryptedMessage += char
    print('Расшифрованый текст: ' + unencryptedMessage)

message = getMessage()
chooseFunc(message)