import csv
import os
from datetime import datetime

ARQUIVO_CSV = os.path.join(os.path.dirname(__file__), "estoque.csv")
ARQUIVO_HISTORICO = os.path.join(os.path.dirname(__file__), "historico.csv")

# ---------------- UTILIDADES ---------------- #
def carregar_estoque():
    estoque = {}
    if os.path.exists(ARQUIVO_CSV):
        with open(ARQUIVO_CSV, newline="", encoding="utf-8") as csvfile:
            leitor = csv.DictReader(csvfile, delimiter=',')
            for linha in leitor:
                if not linha:
                    continue
                try:
                    codigo = linha["codigo"].strip()
                    nome = linha["nome"].strip()
                    preco = float(linha["preco"].replace(",", "."))
                    quantidade = int(linha["quantidade"])
                    estoque[codigo] = {"nome": nome, "preco": preco, "quantidade": quantidade}
                except Exception as e:
                    print(f"⚠️ Linha ignorada devido a erro: {linha} -> {e}")
    return estoque

def salvar_estoque(estoque):
    with open(ARQUIVO_CSV, "w", newline="", encoding="utf-8") as csvfile:
        campos = ["codigo", "nome", "preco", "quantidade"]
        escritor = csv.DictWriter(csvfile, fieldnames=campos)
        escritor.writeheader()
        for codigo, dados in estoque.items():
            escritor.writerow({
                "codigo": codigo,
                "nome": dados["nome"],
                "preco": dados["preco"],
                "quantidade": dados["quantidade"]
            })

def registrar_historico(codigo, tipo, quantidade, nota_fiscal):
    arquivo_existe = os.path.exists(ARQUIVO_HISTORICO)
    with open(ARQUIVO_HISTORICO, "a", newline="", encoding="utf-8") as csvfile:
        campos = ["data_hora", "codigo", "tipo", "quantidade", "nota_fiscal"]
        escritor = csv.DictWriter(csvfile, fieldnames=campos, delimiter=';')
        if not arquivo_existe:
            escritor.writeheader()
        escritor.writerow({
            "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "codigo": codigo,
            "tipo": tipo,
            "quantidade": quantidade,
            "nota_fiscal": nota_fiscal
        })

# ---------------- FUNÇÕES PRINCIPAIS ---------------- #
def cadastrar_produto(estoque):
    while True:
        codigo = input("Código do produto: ").strip()
        if not codigo:
            print("❌ Código não pode ser vazio.")
        elif codigo in estoque:
            print("❌ Produto já cadastrado! Digite outro código.")
        else:
            break

    while True:
        nome = input("Nome do produto: ").strip()
        if nome:
            break
        print("❌ Nome não pode ser vazio.")
        

    while True:
        try:
            preco = float(input("Preço unitário: R$ ").replace(",", ".").strip())
            if preco <= 0:
                print("❌ Preço inválido! Deve ser maior que 0.")
            else:
                break
        except ValueError:
            print("❌ Valor inválido! Digite um número.")

    estoque[codigo] = {"nome": nome, "preco": preco, "quantidade": 0}
    salvar_estoque(estoque)
    print(f"✅ Produto '{nome}' cadastrado com sucesso!")

def entrada(estoque, codigo, quantidade, nota_fiscal):
    if codigo not in estoque:
        print("❌ Produto não encontrado!")
        return
    estoque[codigo]["quantidade"] += quantidade
    salvar_estoque(estoque)
    registrar_historico(codigo, "Entrada", quantidade, nota_fiscal)
    print(f"📦 Entrada registrada: +{quantidade} unid. (NF {nota_fiscal})")
    print(f"🔹 Quantidade atual: {estoque[codigo]['quantidade']} unid.\n")

def saida(estoque, codigo, quantidade, nota_fiscal):
    if codigo not in estoque:
        print("❌ Produto não encontrado!")
        return
    if estoque[codigo]["quantidade"] < quantidade:
        print("⚠️ Estoque insuficiente!")
        return
    estoque[codigo]["quantidade"] -= quantidade
    salvar_estoque(estoque)
    registrar_historico(codigo, "Saída", quantidade, nota_fiscal)
    print(f"🚚 Saída registrada: -{quantidade} unid. (NF {nota_fiscal})")
    print(f"🔹 Quantidade atual: {estoque[codigo]['quantidade']} unid.\n")

def consultar(estoque):
    print("\n===== ESTOQUE ATUAL =====")
    for codigo, dados in estoque.items():
        print(f"{codigo} | {dados['nome']} | {dados['quantidade']} unid. | R$ {dados['preco']:.2f}")
    print("=========================\n")

def alterar_preco(estoque):
    codigo = input("Digite o código do produto: ").strip()
    if codigo not in estoque:
        print("❌ Produto não encontrado!")
        return
    print(f"Produto: {estoque[codigo]['nome']} | Preço atual: R$ {estoque[codigo]['preco']:.2f}")
    while True:
        try:
            novo_preco = float(input("Digite o novo preço: R$ ").replace(",", ".").strip())
            if novo_preco <= 0:
                print("❌ Preço inválido! Deve ser maior que 0.")
            else:
                break
        except ValueError:
            print("❌ Valor inválido! Digite um número.")
    estoque[codigo]['preco'] = novo_preco
    salvar_estoque(estoque)
    print(f"✅ Preço atualizado! Novo preço: R$ {novo_preco:.2f}")

def relatorios(estoque):
    print("\n===== RELATÓRIOS =====")
    valor_total = sum(dados["preco"] * dados["quantidade"] for dados in estoque.values())
    print(f"💰 Valor total do estoque: R$ {valor_total:.2f}")
    print("\n⚠️ Produtos com estoque baixo (<=5 unid.):")
    baixo = False
    for codigo, dados in estoque.items():
        if dados["quantidade"] <= 5:
            print(f"{codigo} | {dados['nome']} | {dados['quantidade']} unid.")
            baixo = True
    if not baixo:
        print("Nenhum produto com estoque baixo.")
    print("======================\n")

def pesquisar_produto(estoque):
    termo = input("Digite nome ou código do produto: ").strip().lower()
    resultados = []
    for codigo, dados in estoque.items():
        if termo in codigo.lower() or termo in dados['nome'].lower():
            resultados.append((codigo, dados['nome'], dados['quantidade'], dados['preco']))
    if resultados:
        print("\n🔎 Resultados encontrados:")
        for r in resultados:
            print(f"{r[0]} | {r[1]} | {r[2]} unid. | R$ {r[3]:.2f}")
    else:
        print("❌ Nenhum produto encontrado.")
    print()

def filtrar_estoque(estoque):
    try:
        estoque_min = int(input("Mostrar produtos com estoque menor ou igual a: "))
    except ValueError:
        print("❌ Valor inválido! Usando 0 como padrão.")
        estoque_min = 0
    ordenar = input("Ordenar por (codigo/nome/quantidade/preco): ").strip().lower()
    lista = [(c, d['nome'], d['quantidade'], d['preco']) 
             for c, d in estoque.items() if d['quantidade'] <= estoque_min]
    if ordenar == "nome":
        lista.sort(key=lambda x: x[1].lower())
    elif ordenar == "quantidade":
        lista.sort(key=lambda x: x[2])
    elif ordenar == "preco":
        lista.sort(key=lambda x: x[3])
    elif ordenar == "codigo":
        lista.sort(key=lambda x: x[0])  
    if lista:
        print("\n⚙️ Produtos filtrados:")
        for f in lista:
            print(f"{f[0]} | {f[1]} | {f[2]} unid. | R$ {f[3]:.2f}")
    else:
        print("❌ Nenhum produto corresponde aos filtros.")
    print()


# ---------------- MENU ---------------- #
def menu():
    estoque = carregar_estoque()
    print(f"✅ Estoque carregado! {len(estoque)} produtos disponíveis.\n")
    while True:
        print("""
===== MENU ESTOQUE =====
1 - Cadastrar produto
2 - Registrar entrada (compra)
3 - Registrar saída (venda)
4 - Consultar estoque
5 - Alterar preço
6 - Relatórios
7 - Pesquisa rápida
8 - Filtrar / Ordenar estoque
9 - Sair
""")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            cadastrar_produto(estoque)
        elif opcao == "2":
            codigo = input("Código do produto: ")
            quantidade = int(input("Quantidade entrada: "))
            nf = input("Número da Nota Fiscal: ")
            entrada(estoque, codigo, quantidade, nf)
        elif opcao == "3":
            codigo = input("Código do produto: ")
            quantidade = int(input("Quantidade saída: "))
            nf = input("Número da Nota Fiscal: ")
            saida(estoque, codigo, quantidade, nf)
        elif opcao == "4":
            consultar(estoque)
        elif opcao == "5":
            alterar_preco(estoque)
        elif opcao == "6":
            relatorios(estoque)
        elif opcao == "7":
            pesquisar_produto(estoque)
        elif opcao == "8":
            filtrar_estoque(estoque)
        elif opcao == "9":
            salvar_estoque(estoque)
            print("💾 Estoque salvo. Saindo...")
            break
        else:
            print("❌ Opção inválida!")

# ---------------- EXECUÇÃO ---------------- #
if __name__ == "__main__":
    menu()
