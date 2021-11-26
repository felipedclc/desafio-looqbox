from db.connection_and_query import ConnectionAndQuery

connection_query = ConnectionAndQuery()


class Reporter:
    def __init__(self, schema):
        self.schema = schema

    def count_number_of_products(self):
        query = f"SELECT COUNT(PRODUCT_NAME) FROM {self.schema}.data_product"
        connection_query.count_number_of_products(self.schema, query, "quantity")

    def top_10_most_expensive_products(self):
        query = f"SELECT PRODUCT_NAME, PRODUCT_VAL FROM {self.schema}.data_product ORDER BY PRODUCT_VAL DESC LIMIT 10"
        connection_query.top_10_most_expensive_products(self.schema, query)

    def sections_BEBIDAS_PADARIA(self):
        query = f"SELECT distinct DEP_NAME, SECTION_NAME FROM {self.schema}.data_product WHERE DEP_NAME='BEBIDAS' OR DEP_NAME='PADARIA'"
        connection_query.sections_BEBIDAS_PADARIA(self.schema, query)

    def more_sales_products_in_one_day(self):
        query = f"SELECT DATE, STORE_NAME, SALES_QTY FROM {self.schema}.data_product_sales as ps INNER JOIN {self.schema}.data_store_cad as sc ON ps.STORE_CODE = sc.STORE_CODE ORDER BY SALES_QTY DESC LIMIT 1"
        connection_query.more_sales_products_in_one_day(self.schema, query)

    def total_sales_first_quarter(self):
        query = f"SELECT dp.DEP_NAME, SUM(ps.SALES_VALUE * ps.SALES_QTY) AS TOTAL_PRICE FROM {self.schema}.data_product_sales as ps INNER JOIN {self.schema}.data_product as dp ON dp.PRODUCT_COD = ps.PRODUCT_CODE WHERE ps.DATE >= '01-01-2019'  AND ps.DATE <= '31-03-2019' GROUP BY DEP_NAME ORDER BY TOTAL_PRICE DESC"
        connection_query.total_sales_first_quarter(self.schema, query)

    def top_10_scify_imdb(self):
        query = f"SELECT Title, Year FROM {self.schema}.IMDB_movies WHERE Genre LIKE '%Sci-Fi%' AND Rating > 7 ORDER BY Rating DESC LIMIT 20"
        connection_query.top_10_scify_imdb(self.schema, query)
