import json


class Writer:
    @classmethod
    def products_quantity_report(cls, company, content):
        path = f"data/quantity_products_{company}.json"
        with open(path, mode="w") as file:
            json.dump(content, file)

    @classmethod
    def top_10_most_expensive_report(cls, company, content):
        path = f"data/top_10_most_expensive_products_{company}.json"
        with open(path, mode="w") as file:
            json.dump(content, file)

    @classmethod
    def sections_BEBIDAS_PADARIA_report(cls, company, content):
        path = f"data/sections_BEBIDAS_PADARIA_{company}.json"
        with open(path, mode="w") as file:
            json.dump(content, file)

    @classmethod
    def more_sales_products_in_one_day_report(cls, company, content):
        path = f"data/store_more_sales_products_in_one_day_{company}.json"
        with open(path, mode="w") as file:
            json.dump(content, file)

    @classmethod
    def total_sales_first_quarter_report(cls, company, content):
        path = f"data/total_sales_first_quarter_{company}.json"
        with open(path, mode="w") as file:
            json.dump(content, file)

    @classmethod
    def top_10_scify_imdb_report(cls, company, content):
        path = f"data/top_20_scify_imdb_report{company}.json"
        with open(path, mode="w") as file:
            json.dump(content, file)
