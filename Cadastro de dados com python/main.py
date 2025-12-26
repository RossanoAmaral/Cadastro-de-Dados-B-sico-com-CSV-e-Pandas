import funcoes as fun
import pandas as pd

listas_dados = list()
cont = 0
while True:
    cont += 1
    fun.texto(f'CADASTRADO {cont}')
    dicionario_dados = dict()

    dicionario_dados['nomes'] = fun.ler_nome('>>> Digite seu nome: ')
    dicionario_dados['idade'] = fun.ler_idade('>>> Digite sua idade: ')
    dicionario_dados['sexo'] = fun.ler_sexo('>>> Digite seu sexo: ')
    fun.texto('DADOS DE ACESSO')
    dicionario_dados['senha'] = fun.ler_senha('>>> Digite sua senha: ')
    dicionario_dados['email'] = fun.ler_email('>>> Digite seu email: ')

    listas_dados.append(dicionario_dados.copy())
    fun.linha()
    print("""    [ 0 ] Continuar cadastrando
    [ 1 ] Encerrar o programa""")
    fun.linha()
    parada = fun.opcao_parada('>>> Digite um número: ')
    
    if parada == 1:
        break

# Pandas 
df = pd.DataFrame(listas_dados)
df.to_csv('lista_dados.csv', index=False) # Salve todo o conteudo no formado e na pasta CSV
fun.texto('TODOS FORAM CADASTRADOS')