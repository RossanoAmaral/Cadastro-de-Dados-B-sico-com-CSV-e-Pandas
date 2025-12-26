def linha(tam=42): # apenas funções de linhas -----------
    lin = print(('-'*tam))
    return lin


def texto(txt): #titulo bonitinho
    linha()
    print(txt.center(42))
    linha()
    return


def ler_nome(msg):
    while True:
        try:
            n = input(msg).strip()

            if not n:
                raise ValueError
            
            if not n.replace(' ', '').isalpha():
                raise TypeError
            
            return n.upper()
        except(ValueError, TypeError):
            texto('ALGO DEU ERRADO, DIGITE NOVAMENTE')


def ler_idade(msg):
    while True:
        try:
            n = int(input(msg))

            if n < 17:
                texto('MENOR DE IDADE')
            return n  # idade válida → sai da função

        except ValueError:
            texto('ERRO AO LER IDADE, DIGITE APENAS NÚMEROS POR FAVOR')


def ler_sexo(msg):
    while True:
        try:
            s = input(msg).strip().upper()[0]

            if s not in 'MF':
                texto('ERRO AO LER SEXO, DIGITE APENAS [M] OU [F]')
                continue

            return s

        except IndexError:
            texto('ERRO AO LER SEXO, DIGITE APENAS [M] OU [F]')


def ler_email(msg):
    while True:
        email = input(msg).strip()

        if ' ' in email:
            texto('ESTRUTURA DE EMAIL INVÁLIDA')
            continue

        if email.count('@') != 1:
            texto('ESTRUTURA DE EMAIL INVÁLIDA')
            continue

        usuario, dominio = email.split('@')

        if not usuario or not dominio:
            texto('ESTRUTURA DE EMAIL INVÁLIDA')
            continue

        if '.' not in dominio:
            texto('ESTRUTURA DE EMAIL INVÁLIDA')
            continue

        return email
    

def ler_senha(num):
    while True:
        try:
            senha = int(input(num))
        except (ValueError,TypeError, IndexError, InterruptedError):
            texto('ALGO DEU ERRADO DIGITE NOVAMENTE')
            continue
        return senha


def opcao_parada(msg):
    while True:
        try:
            opcao = int(input(msg))
            return opcao
        except ValueError:
            texto('OPÇÃO INVÁLIDA, DIGITE UMA OPÇÃO VÁLIDA')