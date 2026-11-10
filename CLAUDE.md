# Projeto: carreira em dados

Portfólio de estudos do plano "Projeto de Carreira: do zero a Especialista de Dados" (documento no Claude: https://claude.ai/artifact/GUK2pGGqDdEcUFD8y9jFYe). Meta atual: vaga de Analista de Dados/BI Jr em cerca de 6 meses, estudando 10h por semana.

## Como me ajudar aqui
- Sou iniciante em SQL, Power BI e Python. Explique o porquê das coisas e prefira me guiar com dicas a entregar a resposta pronta dos exercícios, a menos que eu peça.
- Corrija e revise meu código apontando o erro e o conceito por trás.
- Tudo aqui vai virar portfólio público: nada de dados reais de clientes ou empresas, só dados públicos ou fictícios.

## Ambiente
- PostgreSQL 17 local em `localhost:5432`, usuário `postgres`. A senha está em `.env` (no .gitignore, nunca exibir nem commitar).
- Bancos: `northwind` (dados de exemplo, projeto 01) e `estudos` (livre para testes).
- psql: `C:\Program Files\PostgreSQL\17\bin\psql.exe`. Carregue as variáveis do `.env` antes de usar.
- DBeaver, Power BI Desktop, Python 3.12 com pandas, Jupyter, SQLAlchemy e psycopg.

## Estrutura
- `01-sql` … `05-portfolio`: uma pasta por entrega do plano de 6 meses, cada uma com README.
- `dados/`: arquivos de dados. `dados/brutos/` não vai para o Git.
