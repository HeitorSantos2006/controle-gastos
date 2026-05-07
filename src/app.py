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
    if valor < 0:
        raise ValueError("Valor inválido")

    gastos = carregar_gastos()

    gastos.append({
        "valor": valor,
        "categoria": categoria
    })

    salvar_gastos(gastos)


def total_gastos():
    gastos = carregar_gastos()

    return sum(g["valor"] for g in gastos)


def cotacao_dolar():
    response = requests.get(
        "https://economia.awesomeapi.com.br/json/last/USD-BRL",
        timeout=10
    )

    data = response.json()

    return data["USDBRL"]["bid"]


if __name__ == "__main__":

    while True:

        print("\n--- CONTROLE DE GASTOS ---")
        print("1 - Adicionar gasto")
        print("2 - Ver total")
        print("3 - Ver cotação do dólar")
        print("4 - Sair")

        op = input("Escolha: ")

        if op == "1":

            valor = float(input("Valor: "))
            categoria = input("Categoria: ")

            adicionar_gasto(valor, categoria)

            print("Gasto adicionado!")

        elif op == "2":

            print(f"Total: R$ {total_gastos()}")

        elif op == "3":

            valor = cotacao_dolar()

            print(f"Dólar atual: R$ {valor}")

        elif op == "4":

            break

        else:

            print("Opção inválida!")