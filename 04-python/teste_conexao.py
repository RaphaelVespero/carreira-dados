"""Testa a conexão do Python (pandas) com o PostgreSQL local."""
import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

url = (
    f"postgresql+psycopg://{os.environ['PGUSER']}:{os.environ['PGPASSWORD']}"
    f"@{os.environ['PGHOST']}:{os.environ['PGPORT']}/northwind"
)
engine = create_engine(url)

df = pd.read_sql(
    """
    SELECT c.category_name AS categoria,
           ROUND(SUM(od.unit_price * od.quantity * (1 - od.discount))::numeric, 2) AS vendas
    FROM order_details od
    JOIN products p USING (product_id)
    JOIN categories c USING (category_id)
    GROUP BY 1
    ORDER BY 2 DESC
    """,
    engine,
)
print(df.to_string(index=False))
