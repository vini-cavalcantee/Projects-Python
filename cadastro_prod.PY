#Algoritmo para Adicionar/Excluir/Visualizar produtos em um arquivo JSON.

import json
import os

file = "json_test.json"

def carrega_produtos():
    if os.path.exists(file):
        with open(file, 'r', encoding='utf8') as json_file:
            return json.load(json_file)
    else:
        return []


def salva_produto(produtos):
    with open(file, 'w', encoding='utf8') as file_prod:
        json.dump(produtos, file_prod, ensure_ascii=False, indent=4) 


def clean():
    return os.system('cls')

def line(txt):
    return print(f'{"-" * 15}{txt}{"-" * 15}')

def menu():
    line('MENU')
    print(
        '[1] - Cadastrar um produto',
        '\n[2] - Ver produtos cadastrados',
        '\n[3] - Excluir um produto',
        '\n[4] - Sair')
    line('-')



def cadastra_produto(produto):
    nome = str(input('Nome: '))
    valor = float(input('Valor do produto: R$'))
    calc_icms = lambda valor, porc: valor * porc
    icms = calc_icms(valor, 0.18)

    produto.append({
        'Nome': nome,
        'Valor': valor,
        'ICMS': icms
    })

    salva_produto(produto)
    
def visualiza_produtos(produtos):
    line('PRODUTOS CADASTRADOS')
    if not produtos:
        print('Não há produtos cadastrados para serem visualizados!')
    else:
        for i, produto in enumerate(produtos):
            line(f'Produto {i+1}°')
            print(f'Produto: {produto["Nome"]}',
                  f'\nValor: {produto["Valor"]}',
                  f'\nICMS (18%): {produto["ICMS"]}')
            
def excluir_produto(produtos):
    if not produtos:
        print('Não existe produtos cadastrados a serem excluidos!')
    else:
        visualiza_produtos(produtos)
        try:
            indice = int(input('Selecione qual o índice do produto que deseja excluir')) - 1
            if 0 <= indice < len(produtos):
                produtos.pop(indice)
                salva_produto(produtos)
            else:
                print('ERRO! Selecione um índice válido')
        except ValueError:
            print('ERRO! Selecione um Índice Válido.')
        except IndexError:
            print(f'ERRO! Não existe produto com o índice {indice}')
        
        

while True:
    menu()
    produto = carrega_produtos()
    try:
        opc = int(input('Sua opção: '))
        if opc == 1:
            clean()
            cadastra_produto(produto)

        elif opc == 2:
            clean()
            visualiza_produtos(produto)
        
        elif opc == 3:
            clean()
            excluir_produto(produto)

        elif opc == 4:
            clean
            line('SISTEMA FECHADO')
            break
        else:
            print('ERRO! Selecione uma opção válida')

    except ValueError:
        print('ERRO! Digite uma opção válida!')
    except Exception as error:
        print('ERRO: ', error)
