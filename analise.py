import os
import matplotlib.pyplot as plt
import pandas as pd

# 1. Carregar os dados
df = pd.read_csv("dados_vendas.csv")

# 2. Criar a coluna de Faturamento Total por linha
df["Faturamento"] = df["Quantidade"] * df["Preco_Unitario"]

# 3. Exibir insights no terminal
print("--- INSIGHTS DE VENDAS ---")
faturamento_total = df["Faturamento"].sum()
print(f"Faturamento Total: R$ {faturamento_total:,.2f}")

produto_mais_vendido = (
    df.groupby("Produto")["Quantidade"].sum().idxmax()
)
print(f"Produto mais vendido (em quantidade): {produto_mais_vendido}")

regiao_maior_faturamento = (
    df.groupby("Regiao")["Faturamento"].sum().idxmax()
)
print(f"Região com maior faturamento: {regiao_maior_faturamento}\n")

# 4. Gerar e salvar um gráfico de Faturamento por Categoria
df_categoria = df.groupby("Categoria")["Faturamento"].sum().reset_index()

plt.figure(figsize=(8, 5))
plt.bar(
    df_categoria["Categoria"], df_categoria["Faturamento"], color="skyblue"
)
plt.title("Faturamento Total por Categoria de Produto")
plt.xlabel("Categoria")
plt.ylabel("Faturamento (R$)")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Salvar o gráfico na pasta
plt.savefig("faturamento_por_categoria.png")
print("Gráfico 'faturamento_por_categoria.png' gerado com sucesso!")
