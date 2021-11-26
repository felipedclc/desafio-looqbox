from db.connection import connect
from mysql.connector import Error
from classes.writer import Writer

# SCHEMA = "looqbox_challenge"
writer = Writer()


class ConnectionAndQuery:
    @classmethod
    def count_number_of_products(cls, schema, query, line_name):
        try:
            cursor = connect.cursor()
            cursor.execute(query)
            row = cursor.fetchone()
            writer.products_quantity_report(schema, {line_name: row[0]})
        except Error as e:
            print(f"Erro ao acessar tabela MySQL {e}")
        finally:
            if connect.is_connected():
                cursor.close()
                connect.close()
                print("Conexão ao MySQL foi encerrada")

    @classmethod
    def top_10_most_expensive_products(cls, schema, query):
        try:
            print("iniciando conexão")
            cursor = connect.cursor()
            cursor.execute(query)
            lines = cursor.fetchall()
            doc = [{line[0]: float(line[1])} for line in lines]
            writer.top_10_most_expensive_report(schema, doc)
        except Error as e:
            print(f"Erro ao acessar tabela MySQL {e}")
        finally:
            if connect.is_connected():
                cursor.close()
                connect.close()
                print("Conexão ao MySQL foi encerrada")

    @classmethod
    def sections_BEBIDAS_PADARIA(cls, schema, query):
        try:
            print("iniciando conexão")
            cursor = connect.cursor()
            cursor.execute(query)
            lines = cursor.fetchall()
            bebidas = []
            padaria = []
            for line in lines:
                if line[0] == "BEBIDAS":
                    bebidas.append(line[1])
                if line[0] == "PADARIA":
                    padaria.append(line[1])
            writer.sections_BEBIDAS_PADARIA_report(
                schema, [{"BEBIDAS": bebidas, "PADARIA": padaria}]
            )
        except Error as e:
            print(f"Erro ao acessar tabela MySQL {e}")
        finally:
            if connect.is_connected():
                cursor.close()
                connect.close()
                print("Conexão ao MySQL foi encerrada")

    @classmethod
    def more_sales_products_in_one_day(cls, schema, query):
        try:
            print("iniciando conexão")
            cursor = connect.cursor()
            cursor.execute(query)
            row = cursor.fetchone()
            writer.more_sales_products_in_one_day_report(
                schema,
                [
                    {"date": str(row[0])},
                    {"store": row[1]},
                    {"sale": float(row[2])},
                ],
            )
        except Error as e:
            print(f"Erro ao acessar tabela MySQL {e}")
        finally:
            if connect.is_connected():
                cursor.close()
                connect.close()
                print("Conexão ao MySQL foi encerrada")

    @classmethod
    def total_sales_first_quarter(cls, schema, query):
        try:
            print("iniciando conexão")
            cursor = connect.cursor()
            cursor.execute(query)
            lines = cursor.fetchall()
            doc = [{line[0]: float(line[1])} for line in lines]
            writer.total_sales_first_quarter_report(schema, doc)
        except Error as e:
            print(f"Erro ao acessar tabela MySQL {e}")
        finally:
            if connect.is_connected():
                cursor.close()
                connect.close()
                print("Conexão ao MySQL foi encerrada")

    @classmethod
    def top_10_scify_imdb(cls, schema, query):
        try:
            print("iniciando conexão")
            cursor = connect.cursor()
            cursor.execute(query)
            lines = cursor.fetchall()
            doc = [{line[0]: line[1]} for line in lines]
            writer.top_10_scify_imdb_report(schema, doc)
        except Error as e:
            print(f"Erro ao acessar tabela MySQL {e}")
        finally:
            if connect.is_connected():
                cursor.close()
                connect.close()
                print("Conexão ao MySQL foi encerrada")
