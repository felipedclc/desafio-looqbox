from classes.reporter import Reporter

SCHEMA = "looqbox_challenge"

report = Reporter(SCHEMA)


class Challenges:
    @classmethod
    def challenge_one(cls):
        return report.count_number_of_products()

    @classmethod
    def challenge_two(cls):
        return report.top_10_most_expensive_products()

    @classmethod
    def challenge_three(cls):
        return report.sections_BEBIDAS_PADARIA()

    @classmethod
    def challenge_four(cls):
        return report.more_sales_products_in_one_day()

    @classmethod
    def challenge_five(cls):
        return report.total_sales_first_quarter()

    @classmethod
    def challenge_six(cls):
        return report.top_10_scify_imdb()
