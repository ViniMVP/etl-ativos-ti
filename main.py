from etl import extract, transform, load

CAMINHO_CSV = "data/ativos.csv"
BANCO = "ativos.db"
TABELA = "ativos_ti"


def main():
    df = extract(CAMINHO_CSV)
    df_transformado = transform(df)
    load(df_transformado, BANCO, TABELA)


if __name__ == "__main__":
    main()