import json
import os
import requests

FILE = "gastos.json"


def carregar_gastos():
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r") as f:
        return json.load(f)


def salvar_gastos(gastos):
    with open(FILE, "w") as f:
        json.dump(gastos, f, indent=4)


def adicionar_gasto(valor, categoria):
    if valor <= 0:
        raise ValueError("Valor deve ser positivo")

    gastos = carregar_gastos()
    gastos.append({
        "valor": valor,
        "categoria": categoria
    })

    salvar_gastos(gastos)


def listar_gastos():
    return carregar_gastos()


def total_gastos():
    return sum(g["valor"] for g in carregar_gastos())


def filtrar_por_categoria(categoria):
    return [
        g for g in carregar_gastos()
        if g["categoria"].lower() == categoria.lower()
    ]


def cotacao_dolar():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

    response = requests.get(url, timeout=10)

    data = response.json()

    return data["USDBRL"]["bid"]


def menu():
    while True:
        print("\n==== CONTROLE DE GASTOS ====")
        print("1 - Adicionar gasto")
        print("2 - Listar gastos")
        print("3 - Total")
        print("4 - Filtrar por categoria")
        print("5 - Cotação do dólar")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            try:
                valor = float(input("Valor: "))
                categoria = input("Categoria: ")

                adicionar_gasto(valor, categoria)

                print("Gasto adicionado!")

            except ValueError as e:
                print("Erro:", e)

        elif op == "2":
            gastos = listar_gastos()

            if not gastos:
                print("Nenhum gasto registrado.")

            for g in gastos:
                print(g)

        elif op == "3":
            print("Total:", total_gastos())

        elif op == "4":
            cat = input("Categoria: ")

            filtrados = filtrar_por_categoria(cat)

            if not filtrados:
                print("Nenhum gasto encontrado.")

            for g in filtrados:
                print(g)

        elif op == "5":
            try:
                dolar = cotacao_dolar()
                print(f"Cotação do dólar: R$ {dolar}")

            except Exception as e:
                print("Erro ao buscar cotação:", e)

        elif op == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()