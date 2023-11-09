import datetime

def check_aniversarios_no_mes(birthdate):
    mes_atual = datetime.date.today()
    birthdate = datetime.datetime.strptime(birthdate, "%d/%m/%Y")
    return mes_atual.month == birthdate.month

inicial_file = "consultores_info.txt"
final_file = "aniversariantes_do_mes.txt"

with open(inicial_file, "r") as file:
    lines = file.readlines()

mes_corrente = datetime.date.today().strftime("%m")

with open(final_file, "w") as file:
    for line in lines:
        name, email, birthdate = line.strip().split(" | ")
        if check_aniversarios_no_mes(birthdate):
            file.write(f"{name} | {email} | {birthdate}\n")

print(f"Arquivo {final_file} gerado!")