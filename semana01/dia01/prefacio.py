"""Eis o plano: quando uma pessoa usar uma funcionalidade que você não
entende, simplesmente atire nela. Isso é mais fácil que aprender algo
novo e, em pouco tempo, os únicos programadores vivos estarão codando
em um minúsculo subconjunto facilmente compreensível do Python
- Tim Peters"""


class Day01:
    day = "dia01"
    table_of_contents_title = "Prefácio"
    topics = (
        "Aquém este livro se destina",
        "A quem este livro não se destina",
        "Como este livro está organizado",
        "Uma abordagem 'mão na massa'",
        "Hardware usado para medições de tempo",
        "Meu ponto de vista",
        "Jargão do Python",
        "Versão do Python discutida",
        "Convenções usadas neste livro",
        "Uso dos exemplos de código",
        "Como entrar em contato conosco",
        "Agradecimentos",
    )

    @classmethod
    def show(cls):
        for t in cls.topics:
            print(t)

    pass


if __name__ == "__main__":
    Day01.show()
    print(Day01)
