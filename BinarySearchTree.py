# Trabalho 3 - Estrutura de Dados - Matheus Mendonca Lopes
# Árvore Binária de Busca - Busca, Inserção e Remoção de Dois Elementos

import pandas as pd
import numpy as np

arquivoResultados = open("resultados.txt", "w")

class Node: # Classe para criar os nós da árvore, através de OO, em que cada nó passa a ser um objeto, com valores atribuídos aos seus lados esquerdo (menor) e direito (maior)
    
    def __init__(self, val):
        self.valor = val
        self.esquerda = None
        self.direita = None

def converteArrayParaABB(array): # Função recursiva para converter um Array obtido dos dados para uma ABB 

    if array.size == 0:
        return
    
    meio = (len(array))//2 # O meio será a raiz da árvore, e é obtido a partir de uma divisão simples
    raiz = Node(array[meio])
    
    raiz.esquerda = converteArrayParaABB(array[:meio]) # O lado esquerdo da raiz terá todos os valores à esquerda do meio da Array List

    raiz.direita = converteArrayParaABB(array[meio+1:]) # O lado direito da raiz terá todos os valores à direita do meio da Array List
    return raiz

def buscarValor(raiz, valor): 
    
    # Casos base: Raíz é null ou o valor está presente na raíz
    if raiz is None or raiz.valor == valor:
        return raiz
    
    # Valor a ser procurado é menor que o valor na raiz: deve se percorrer a sub-árvore da esquerda
    elif (valor < raiz.valor):
        return buscarValor(raiz.esquerda, valor)
    
    # Valor a ser procurado é maior que o valor na raiz: deve se percorrer a sub-árvore da direita
    elif (valor):
        return buscarValor(raiz.direita, valor)

def insereValor(raiz, valor):
    
    if raiz is None:
        return Node(valor)
    else:
        if valor == raiz.valor:
            return raiz
        elif valor < raiz.valor:
            raiz.esquerda = insereValor(raiz.esquerda, valor)
        else:
            raiz.direita = insereValor(raiz.direita, valor)
    return raiz

def nodeMenorValor(node):
    
    atual = node

    while(atual.esquerda is not None):
        atual = atual.esquerda
    
    return atual

def deletaValor(raiz, valor):
    
    if raiz is None:
        return raiz
    
    if(valor < raiz.valor):
        raiz.esquerda = deletaValor(raiz.esquerda, valor)
    
    elif (valor > raiz.valor):
        raiz.direita = deletaValor(raiz.direita, valor)
    
    else:
        if raiz.esquerda is None:
            temp = raiz.direita
            raiz = None
            return temp
        
        elif raiz.direita is None:
            temp = raiz.esquerda
            raiz = None
            return temp
        
        temp = nodeMenorValor(raiz.direita)

        raiz.valor = temp.valor

        raiz.direita = deletaValor(raiz.direita, temp.valor)
    
    return raiz
    
def percursoEmOrdem(node): # Função recursiva para percorrer a ABB Em-Ordem
    
    if not node:
        return
    
    percursoEmOrdem(node.esquerda)
    arquivoResultados.write(str(node.valor) + " ")
    percursoEmOrdem(node.direita)

# Estrutura para obter valores ordenados de coluna do Excel
df = pd.read_excel('valores.xlsx')
valores = df['Entrada'].to_numpy(np.int64) # A árvore terá apenas valores inteiros
arvore = converteArrayParaABB(valores)

arquivoResultados.write("Percurso em-ordem da arvore pre-operacoes: \n")
percursoEmOrdem(arvore)
arquivoResultados.write("\n")

arquivoResultados.write("Busca na arvore por valor nao presente: \n")
arquivoResultados.write(str(buscarValor(arvore, 3)))
arquivoResultados.write("\n")

arquivoResultados.write("Busca na arvore por valor presente: \n")
arquivoResultados.write(str(buscarValor(arvore, 5).valor))
arquivoResultados.write("\n")

arquivoResultados.write("Arvore apos insercao do valor 15, remocao de uma folha (2) e de um elemento interno (8): \n")
arvore = insereValor(arvore, 15)
arvore = deletaValor(arvore, 2)
arvore = deletaValor(arvore, 8)
percursoEmOrdem(arvore)
arquivoResultados.write("\n")

arquivoResultados.close()