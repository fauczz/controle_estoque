import csv
import os

# Caminho do CSV (mesma pasta do script)
ARQUIVO_CSV = os.path.join(os.path.dirname(__file__), "estoque.csv")

# Lista de produtos
produtos = [
    ["P001","Caixa de Som JBL",800.0,100],
    ["P002","Home Theater Sony",2500.0,4],
    ["P003","Amplificador Yamaha",1800.0,3],
    ["P004","Cabo HDMI 2m",50.0,20],
    ["P005","Projetor Epson",3500.0,2],
    ["P006","Caixa de Som Bose",1500.0,4],
    ["P007","Subwoofer Pioneer",1200.0,6],
    ["P008","Receiver Onkyo",2200.0,2],
    ["P009","Soundbar Samsung",1300.0,7],
    ["P010","Controle Universal Logitech",400.0,15],
    ["P011","Caixa Acústica Polk Audio",900.0,8],
    ["P012","Microfone Shure",700.0,12],
    ["P013","Mesa de Som Behringer",1600.0,3],
    ["P014","Cabo Óptico Digital",60.0,25],
    ["P015","Suporte para Projetor",150.0,10],
    ["P016","Tela de Projeção Retrátil",900.0,5],
    ["P017","Headset Gamer HyperX",500.0,18],
    ["P018","Caixa Bluetooth Philips",350.0,20],
    ["P019","Micro System LG",1100.0,6],
    ["P020","Cabo RCA 1,5m",25.0,40],
    ["P021","Equalizador Digital",800.0,4],
    ["P022","Caixa Passiva Attack",1000.0,3],
    ["P023","Mixer Digital Yamaha",3000.0,2],
    ["P024","Cabo P10 Estéreo",30.0,50],
    ["P025","Rack para Equipamentos",600.0,2],
    ["P026","Caixa Portátil Sony",750.0,9],
    ["P027","Suporte de Parede para Caixa",90.0,15],
    ["P028","Microfone Sem Fio AKG",950.0,5],
    ["P029","Cabo XLR Balanceado",45.0,35],
    ["P030","Projetor Portátil LG",2100.0,3],
    ["P100","JBL",130.0,420],
    ["P102","JBL Soundbar",1000.0,0],
    ["P200","Fone de ouvido JBL",87.9,50]
]

# Cria o CSV
with open(ARQUIVO_CSV, "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["codigo","nome","preco","quantidade"])
    escritor.writerows(produtos)

print(f"✅ Arquivo '{ARQUIVO_CSV}' criado com {len(produtos)} produtos!")
