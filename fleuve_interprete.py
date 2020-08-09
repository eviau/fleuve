import sys

class Bureau():

    def _reserved_words(self):
        return ["fleurs", "fruits", "eau","rose","tulipe","tournesol","pomme","melon","tournesol","lac", "etang", "ruisseau"]

    def __init__(self,program):
        self.programme = program.split()
        self.fleurs = {}
        self.fruits = {}
        self.eau = {}
        self.pointeur_lecture = 0
        self.fonctions = {}

    def _next_pointeur(self):
        self.pointeur_lecture += 1
        if self.pointeur_lecture >= len(self.programme):
            print("fin du poème (encore). bonne nuit.")
            exit()
    
    def _get_next(self):
        self._next_pointeur()
        value = bureau.programme[bureau.pointeur_lecture]
        return value
    
    def _save_fleur(self,typ):
        name = self._get_next()
        value = self._get_next()
        if not(value in self._reserved_words()) and not(name in self._reserved_words()):
            bureau.fleurs[name] = {typ: value}
            self._next_pointeur()
            return name
        else:
            print("la valeur " + value + " est un mot réservé! recommencez.")

    def fleuve_interprete(self):
        while bureau.pointeur_lecture < len(bureau.programme):
            word = bureau.programme[bureau.pointeur_lecture]
            # print(word)
            self.read_word(word)
            # print(word)
            input("je suis ici")
            print(len(bureau.programme))
            print(bureau.pointeur_lecture)
        return

    def read_word(self,word):
        if word in ("rose", "tulipe","tournesol"):
            key = word
            self._next_pointeur()
            typ = bureau.programme[bureau.pointeur_lecture]
            if typ in ("bleu, jaune, rouge") or (type(typ) is int and (int(typ) % 2) == 0):
                name = self._save_fleur(typ)
                print("je confirme ! la fleur est une " + key + " la fleur est " + typ + " son nom est " + name + " et sa valeur est " + bureau.fleurs[name][typ] + ".")
            else:
                print("ceci n'est une fleur. continuons.")
                self._next_pointeur()
            return      

        elif word in ("pomme", "melon", "tomate"):
            key = word
            self._next_pointeur()
            name = bureau.programme[bureau.pointeur_lecture]
            if name in ("amer", "extreme") or (int(name) % 2) == 0:
                bureau.fruits[key] = name
                self._next_pointeur()
                print("le fruit est " + name + " c'est un fruit d'un drôle de genre, c'est une " + key)
            return     

        elif word in ("lac", "etang", "ruisseau"):
            key = word
            self._next_pointeur()
            name = bureau.programme[bureau.pointeur_lecture]
            if name in ("majestueux"):
                print("le " + key + " est majestueux! quelle redondance.")
            elif name in ("pourpre","duo","effervescent"):
                print("oui! c'est mieux. le " + key + " est " + name)
                bureau.eau[key] = name
            elif name == 2:
                print("deux c'est bon.")
                bureau.eau[key] = name
            elif int(name) % 2 == 0:
                print("mais non c'est insensé, il ne peut y en avoir autant!")
            self._next_pointeur()
            return    
        else:
            print("c'est la fin de ce poème. bonsoir.")
            self._next_pointeur()

            return    


if __name__ == "__main__":
    # print(sys.argv)
    with open(sys.argv[1], "r") as file:
        program = file.read()
        bureau = Bureau(program)
        bureau.fleuve_interprete()