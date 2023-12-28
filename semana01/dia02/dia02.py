""" O senso estético de Guido no design da linguagem é incrível. Conheci
muitos bons designers de linguagem que poderíam ter criado belas linguagens
em teoria, mas que ninguém jamais usaria, porém Guido é uma dessas raras
pessoas capazes de criar uma linguagem apenas um pouco menos bela teoricamente,
mas com a qual é um prazer escrever programas —Jim Hugunin"""


class Day02:
    day = "dia02"
    table_of_contents_title = "CAPÍTUL01 Modelo de dados do Python"
    topics = ("CAPÍTUL01 Modelo de dados do Python",)

    @classmethod
    def show(cls):
        for t in cls.topics:
            print(t)

    pass


if __name__ == "__main__":
    Day02.show()
