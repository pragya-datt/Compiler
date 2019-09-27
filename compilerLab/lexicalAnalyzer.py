import re

class lexer():
    def __init__(self, prog):
        self.prog = prog

    def token(self):
        tokens =[]

        prog = self.prog.split()
        index = 0

        while index < len(prog):
            word = prog[index]

            if word == "var" or word == "int" or word == "float" or word == "if" or word == "then" or word == "else" or word == "endif":
                tokens.append(["KEYWORD", word])
            elif re.match('[a-z]', word) or re.match('[A-Z]', word):
                if word[len(word)-1]==";":
                    tokens.append(["IDENTIFIER", word[0:len(word)-1]])
                else:
                    tokens.append(["IDENTIFIER", word])

            elif re.match('[0-9]', word):
                if word[len(word)-1]==";":
                    tokens.append(["IDENTIFIER", word[0:len(word)-1]])
                else:
                    tokens.append(["INTEGER", word])
            elif word in "=/*-+><":
                tokens.append(["OPERATOR", word])

            if word[len(word)-1]==";":
                tokens.append(["STATEMENT_END", ";"])

            index +=1

        print (tokens)

        return tokens






