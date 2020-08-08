import sys

class Bureau():

    def __init__(self,program):
        self.programme = program.split()
        self.fleurs = {}
        self.fruits = {}
        self.eau = {}
        self.pointeur_lecture = 0
        self.fonctions = {}

    def fleuve_interprete(self):

        while bureau.pointeur_lecture < len(bureau.programme):
            word = bureau.programme[bureau.pointeur_lecture]
            print(word)
            self.read_word(word)
            print(word)
            input("je suis ici")
        return

    def read_word(self,word):
        if word in ("rose", "tulipe","tournesol"):
            key = word
            bureau.pointeur_lecture += 1
            value = bureau.programme[bureau.pointeur_lecture]
            if value in ("bleu, jaune, rose") or (int(value) % 2) == 0:
                bureau.fleurs[key] = value
                bureau.pointeur_lecture += 1
                print("la fleur est une " + key + " la fleur est " + value)
            return      

        elif word in ("pomme", "melon", "tomate"):
            key = word
            bureau.pointeur_lecture += 1
            value = bureau.programme[bureau.pointeur_lecture]
            if value in ("amer", "extreme") or (int(value) % 2) == 0:
                bureau.fruits[key] = value
                bureau.pointeur_lecture += 1
                print("le fruit est " + value + " c'est un fruit d'un drôle de genre, c'est une " + key)
            return     

        elif word in ("lac", "etang", "ruisseau"):
            key = word
            bureau.pointeur_lecture += 1
            value = bureau.programme[bureau.pointeur_lecture]
            if value in ("majestueux"):
                print("le " + key + " est majestueux! quel redondance.")
            elif value in ("pourpre","duo","effervescent"):
                print("oui! c'est mieux. le " + key + " est " + value)
                bureau.eau[key] = value
            elif value == 2:
                print("deux c'est bon.")
                bureau.eau[key] = value
            elif int(value) % 2 == 0:
                print("mais non c'est incensé, il ne peut y en avoir autant!")
            bureau.pointeur_lecture += 1
            return        


if __name__ == "__main__":
    # print(sys.argv)
    with open(sys.argv[1], "r") as file:
        program = file.read()
        bureau = Bureau(program)
        bureau.fleuve_interprete()