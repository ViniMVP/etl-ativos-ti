import pandas as pd
import sqlite3
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")


def extract(caminho_csv: str) -> pd.DataFrame:
    logging.info("Extraindo dados do CSV...")
    df = pd.read_csv(caminho_csv)
    logging.info(f"{len(df)} linhas extraídas.")
    return df


def transform(df: pd.DataFrame) -> pd.DataFrame:
    logging.info("Transformando dados...")

    df = df.drop_duplicates(subset = ["equipamento", "setor", "status", "data_aquisicao"])
    df["setor"] = df["setor"].fillna("Não informado")
    df["data_aquisicao"] = pd.to_datetime(df["data_aquisicao"])
    df["dias_desde_aquisicao"] = (pd.Timestamp.now() - df["data_aquisicao"]).dt.days

    logging.info(f"{len(df)} linhas após transformação.")
    return df


def load(df: pd.DataFrame, banco: str, tabela: str):
    logging.info("Carregando dados no banco SQLite...")
    conn = sqlite3.connect(banco)
    df.to_sql(tabela, conn, if_exists="replace", index=False)
    conn.close()
    logging.info("Dados carregados com sucesso.")