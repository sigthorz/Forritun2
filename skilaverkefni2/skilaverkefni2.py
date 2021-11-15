import csv
from random import shuffle

def lesa_skra(nafntxt):
    spurningar_svor = []
    with open(nafntxt,'r') as f:
        lines = f.read()
    lines_split = lines.split("\n")
    for x in lines_split:
        splitter = x.split(";")
        dict_question = {"question":splitter[0],"answer":splitter[1]}
        spurningar_svor.append(dict_question)
    return spurningar_svor

def spurning(spurning:str, svar:str) -> bool:
    print(spurning)
    svar_fra_notanda = input("svar:")
    if svar_fra_notanda == svar:
        return True
    return False

def lesa_simaskra(filename):
    simaskra = []
    with open(filename,'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

def skrifaIskra(listi,nafntxt):
    simaskra = lesa_simaskra(nafntxt)
    simaskra.append(listi)
    with open(nafntxt,"w") as f:
        write = csv.writer(f)
        write.writerows(simaskra)

def breytaUppl(simaskra,nafn,nyttGSM):
    new_simaskra = simaskra
    for foo in new_simaskra:
        if nafn in foo:
            foo[1] = nyttGSM
    return new_simaskra

def eyda(simaskra,nafn):
    new_simaskra = simaskra
    for foo in new_simaskra:
        print(foo)
        if nafn in foo:
            new_simaskra.remove(foo)
    return new_simaskra


while True:
    print("-----Valmynd-----\n")
    print("Liður 1: Spurningaleikur")
    print("Liður 2: simaskrá")
    print("Liður 3: Hætta í Valmynd")
    choice = int(input("Veldu lið: "))

    if choice == 1:
        print("choice1")

        print("---- SPURNINGALEIKUR ----\n")
        question_count = 0
        allar_spurningar = lesa_skra("einkunnir.csv")
        points = 0
        shuffle(allar_spurningar)
        for _spurning in allar_spurningar:
            falsecounter = 0
            for _ in range(2):
                sp = spurning(_spurning["question"],_spurning["answer"])
                if sp == True:
                    points+=1
                    print("Rétt!!\n")
                    break
                if sp == False:
                    print("Rangt!!")
                    falsecounter += 1
                if falsecounter == 2:
                    print(f"Rétt svar er: {_spurning['answer']}\n")
            question_count+=1
        print(f"Stigafjöldi þinn er: {points}")

    innihald_simaskra = lesa_simaskra("simaskra.csv") #Öll gögn í simaskra.csv skránni
    if choice == 2: # Ef valkostur er 2
        while True:
            val = int(input("veldu 1 skrifa í skrá,2 breyta símanúmeri, eða 3 eyða aðila:"))

            if val == 1:
                listi_inputs = []
                listi_inputs.append(input("skrifaðu inn nafn: "))
                listi_inputs.append(input("skrifaðu inn Símanúmer: "))
                listi_inputs.append(input("Skrifaðu inn kennitölu: "))
                skrifaIskra(listi_inputs, "simaskra.csv")
                print(lesa_simaskra("simaskra.csv"))

            if val == 2:
                print(breytaUppl(innihald_simaskra, input("Vinsamlegast stimplaðu inn nafn aðila: "), input("Vinsamlegast stimplaðu inn símanúmer aðila: ")))

            if val == 3:
                print(eyda(innihald_simaskra, input("Sláðu inn nafn aðila sem þú vilt eyða: ")))

    else:
        break
