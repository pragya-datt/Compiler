import compilerLab.lexicalAnalyzer

def main():
    content = ""

    with open('C:\Pragya\Sem5\compilerLab\lexAna.txt', 'r') as file:
        content = file.read()
        lex = compilerLab.lexicalAnalyzer.lexer(content)
        tokens = lex.token()
main()