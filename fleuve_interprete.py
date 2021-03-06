import sys

class Bureau():

    def _reserved_words(self):
        return ["fleurs", "fruits", "eau","rose","tulipe","tournesol","pomme","melon","tournesol","lac", "etang", "ruisseau"]

    def _user_reserved_words(self):
        return self.user_defined
    
    def _user_defined_fcts(self):
        return self.fonctions.keys

    def __init__(self,program):
        self.programme = program.split()
        self.fleurs = {}
        self.fruits = {}
        self.eau = {}
        self.pointeur_lecture = 0
        self.fonctions = {}
        self.user_defined = []

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
        self.user_defined.append(name)
        value = self._get_next()
        print("vérifions... si cette fleur existe dans notre univers! ")
        while value in self._reserved_words():
            value = input("la valeur " + value + " est un mot réservé! recommencez en direct (j'attends) : ")
        while name in self._reserved_words():
            name = input("le nom " + name + " est un mot réservé! recommencez en direct (j'attends) : ")
            
        bureau.fleurs[name] = {typ: value}            
        return name        

    def _save_fruit(self,typ):
        name = self._get_next()
        self.user_defined.append(name)
        value = self._get_next()
        print("ce fruit, existe-t-il ?")
        while value in self._reserved_words():
            value = input("non, cette valeur, " + value + " est un mot réservé! recommencez en direct (j'attends): ")
        while name in self._reserved_words():
            name = input("désolée, ce nom: " + name + " est un mot réservé. recommencez en direct (j'attends): ")
        bureau.fruits[name] = {typ: value}
        return name

    def _save_eau(self,typ):
        name = self._get_next()
        self.user_defined.append(name)
        value = self._get_next()
        while value in self._reserved_words():
            value = input("non, cette valeur, " + value + " est un mot réservé! recommencez en direct (j'attends): ")
        while name in self._reserved_words():
            name = input("désolé, ce nom: " + name + " est un mot réservé. recommencez en direct (j'attends): ")
        bureau.eau[name] = {typ: value}
        return name
    
    def _define_fct(self,fct):
        print("alors, définissons cette fonction...")
        char = self._get_next()
        print("nous en sommes à " + char )
        signature = ""
        
        while char != ';':
            signature = signature + char
            char = self._get_next()
            print(char)

        body = ""

        while char != ")":
            body = body + char
            char = self._get_next()


        self.fonctions[fct] = {"sign" : signature, "body" : body}

        print(self.fonctions)

            


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
            print("le mot est: " + word)
            key = word
            self._next_pointeur()
            typ = bureau.programme[bureau.pointeur_lecture]
            if typ in ("bleu, jaune, rouge") or (int(typ) % 2) == 0:
                name = self._save_fleur(typ)
                print("je confirme ! la fleur est une " + key + " la fleur est " + typ + " son nom est " + name + " et sa valeur est " + bureau.fleurs[name][typ] + ".")
            else:
                print("ceci n'est une fleur. continuons.")
            self._next_pointeur()
            return      

        elif word in ("pomme", "melon", "tomate"):
            key = word
            self._next_pointeur()
            typ = bureau.programme[bureau.pointeur_lecture]
            if typ in ("amer", "extreme") or (int(typ) % 2) == 0:
                name = self._save_fruit(typ)
                print("le fruit est " + name + " c'est un fruit d'un drôle de genre, c'est une " + bureau.fruits[name][typ])
            else:
                print("est-ce un fruit ? bien non. suivant !")
            self._next_pointeur()
            return     

        elif word in ("lac", "etang", "ruisseau"):
            key = word
            self._next_pointeur()
            typ = bureau.programme[bureau.pointeur_lecture]
            if typ in ("majestueux"):
                print("le " + key + " est majestueux! quelle redondance.")
            elif typ in ("pourpre","duo","effervescent"):
                print("oui! c'est mieux. " + key + " est " + typ)
                name = self._save_eau(typ)
            elif typ == 2:
                print("deux c'est bon.")
                name = self._save_eau(typ)
            elif int(typ) % 2 == 0:
                print("mais non c'est insensé, il ne peut y en avoir autant!")
                self._next_pointeur()
            self._next_pointeur()
            return  
        elif word == "propos":
            print("c'est une fonction!")
            fct = self._get_next()
            print(fct)
            self._next_pointeur()
            use_or_def = bureau.programme[bureau.pointeur_lecture]
            if use_or_def == "(":
                print("voici une autre façon de dire nos propos.")
                self._define_fct(fct)
        elif word in self.fonctions.keys():
                print("vous avez oublié une parenthèse. la voici: ( " + use_or_def )
                print("maintenant, examinons vos propos...")
                self._use_fct(fct)
                print("... et ceci conclut nos propos, parenthèse fermante incluse: )")
        else:
            print("ce mot... ne me dit rien. bonsoir.")
        self._next_pointeur()
        return   

    def redire(word):
        return print(word) 


if __name__ == "__main__":
    # print(sys.argv)
    with open(sys.argv[1], "r") as file:
        program = file.read()
        bureau = Bureau(program)
        bureau.fleuve_interprete()