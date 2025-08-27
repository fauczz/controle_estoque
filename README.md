# controle_estoque
Controle de Estoque em Python
Descrição

Este é um sistema de controle de estoque desenvolvido em Python, que permite gerenciar produtos, registrar entradas e saídas, consultar informações do estoque, gerar relatórios e manter um histórico de movimentações em arquivos CSV. Ele é ideal para pequenas empresas ou para estudo de manipulação de arquivos e interfaces em Python.

O sistema possui uma interface amigável e menu interativo para facilitar a operação.

Funcionalidades

O programa conta com as seguintes funcionalidades:

Cadastrar produto
Permite adicionar novos produtos ao estoque com código, nome, quantidade e preço.

Registrar entrada (compra)
Atualiza o estoque adicionando unidades de produtos já cadastrados.

Registrar saída (venda)
Atualiza o estoque removendo unidades de produtos, controlando a disponibilidade.

Consultar estoque
Exibe todos os produtos cadastrados, suas quantidades e preços.

Alterar preço
Permite modificar o preço de qualquer produto existente no estoque.

Relatórios
Gera relatórios detalhados do estoque e histórico de movimentações.

Pesquisa rápida
Localiza rapidamente produtos pelo código ou nome.

Filtrar / Ordenar estoque
Permite organizar o estoque por código, nome, quantidade ou preço.

Sair
Encerra o programa de forma segura, salvando todas as alterações no arquivo CSV.

Estrutura de Arquivos

estoque.csv – Armazena os produtos e suas quantidades.

historico.csv – Mantém o histórico de entradas e saídas.

controle_estoque.py – Arquivo principal do programa.

Tecnologias Utilizadas

Python 3.x

Módulos padrão: csv, os
