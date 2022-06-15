alfabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя123456789123456789'

def get_message():
    return input('Введите сообщение: ').lower()

def choose_func(message):
    print('''
        Если вам нужно зашифровать сообщение, введите 1')
        Если вам нужно разшифровать сообщение, введите 2
        Если вам нужно взломать сообщение и узнать улюч, введите 3
    ''')
    choosed = int(input('Введите выбраное число: '))
    match choosed:
        case 1:
            encrypt_message(message)
        case 2:
            unencrypt_message(message)
        case 3:
            hack_message(message)
    quit()

def hack_message(message):
    key = 1
    unencrypted_message = ''
    choosed = 0
    while True:
        for char in message:
            position = alfabet.rfind(char)
            new_position = position - key
            if char in alfabet:
                unencrypted_message += alfabet[newPosition]
            else:
                unencrypted_message += char
        print('Расшифровка с ключом ' + str(key) + ': ' + unencrypted_message)
        print('Если это правильная расшифровка, введите 1. Если нет - 2')
        choosed = int(input('Введите выбраное число: '))
        match choosed:
            case 1:
                print('Расшифрованый текст: ' + unencrypted_message)
                break
            case 2:
                key += 1
                unencrypted_message = ''
                continue

def get_key():
    return int(input('Введите ключ: '))

def encrypt_message(message):
    key = get_key()
    encrypted_message = ''
    for char in message:
        position = alfabet.find(char)
        new_position = position + key
        if char in alfabet:
            encrypted_message += alfabet[newPosition]
        else:
            encrypted_message = + char
    print('Зашифрованый текст: ' + encrypted_message)

def unencryptMessage(message):
    key = get_key()
    unencrypted_message = ''
    for char in message:
        position = alfabet.rfind(char)
        new_position = position - key
        if char in alfabet:
            unencrypted_message += alfabet[newPosition]
        else:
            unencrypted_message += char
    print('Расшифрованый текст: ' + unencryptedMessage)

message = get_message()
choose_func(message)
