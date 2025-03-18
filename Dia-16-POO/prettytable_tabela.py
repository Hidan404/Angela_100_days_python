from prettytable import PrettyTable

tabela = PrettyTable()


tabela.field_names = ["Nome", "Idade", "Profissão"]
tabela.add_row(["John Doe", 40, "Programador"])
tabela.add_row(["Jane Doe", 35, "Designer"])
tabela.add_row(["John Smith", 50, "Gerente"])
tabela.add_row(["Jane Smith", 45, "Diretora"])

tabela.align = "l"

print(tabela)