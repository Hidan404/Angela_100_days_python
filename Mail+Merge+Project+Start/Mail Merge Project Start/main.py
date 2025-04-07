#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


class MailMerge:
    def __init__(self):
        self.nomes = []
        self.letras = "Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt"
        self.nomes_lista = "Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt"
        self.diretorio = "Mail+Merge+Project+Start/Mail Merge Project Start/Output/ReadyToSend"
        
    def ler_nomes(self):
        with open(self.nomes_lista, "r") as file: 
            for line in file:
                self.nomes.append(line.strip())
        return self.nomes
    
    def ler_letra(self):
        with open(self.letras, "r") as file:
            conteudo = file.read()
        return conteudo
    
    def criar_letras(self):
        for nome in self.nomes:
            conteudo = self.ler_letra()
            conteudo = conteudo.replace("[name]", nome)
            with open(f"{self.diretorio}/{nome}.txt", "w") as file:
                file.write(conteudo)

    def main(self):
        self.ler_nomes()
        self.criar_letras()
        print("Cartas criadas com sucesso!")


if __name__ == "__main__":
    mail_merge = MailMerge()
    mail_merge.main() 