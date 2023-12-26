""""""


class Day01:
    day = "dia01"
    table_of_contents_title = "Prefácio"
    topics = (
        "Novidades na segunda edição",
        "Convenções usadas neste livro",
        "Uso de exemplos de código de acordo com a política da O'Reilly",
        "Como entrar em contato conosco",
        "Agradecimentos",
        "ln memoriam: John D. Hunter (1968-2012)",
        "Agradecimentos para a segunda edição (2017) ",
        "Agradecimentos para a primeira edição (2012) ",
    )

    @classmethod
    def show(cls):
        for t in cls.topics:
            print(t)

    pass


if __name__ == "__main__":
    Day01.show()
