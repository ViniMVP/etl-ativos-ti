# ETL - Controle de Ativos de TI

Pipeline simples de ETL (Extract, Transform, Load) que lê dados de materiais de TI
de um arquivo CSV, realiza limpeza e enriquecimento dos dados, e carrega o
resultado em um banco SQLite.

## Tecnologias
- Python 3
- Pandas
- SQLite

## Como rodar

\`\`\`bash
python -m venv venv
venv\Scripts\activate no Windows
pip install -r requirements.txt
python main.py
\`\`\`

## O que o pipeline faz
1. **Extract**: lê o CSV de ativos
2. **Transform**: remove duplicatas (ignorando o campo id), trata valores nulos no setor, converte datas e calcula dias desde a aquisição
3. **Load**: grava os dados tratados em um banco SQLite

## Aprendizados
Durante o desenvolvimento, identifiquei que o `drop_duplicates()` padrão não
detectava registros duplicados porque a coluna `id` estava sendo
considerada na comparação. A correção foi especificar as colunas relevantes
via `subset`, ignorando o `id`.