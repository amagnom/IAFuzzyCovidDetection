import itertools
l = ["nao","sim"]
lista = [list(i) for i in itertools.product(l, repeat=10)]
print()
i = 0
arquivo = ""
chance = "nao"
for a in lista:
    if a.count("sim") >= a.count("nao"):
        chance = "sim"
    atual = "r{} = ctrl.Rule(tosse['{}'] & febre['{}'] & coriza['{}'] & dorGarganta['{}']" \
            " & dificuldadeRespirar['{}'] " \
            "& anosmia['{}'] & disturbiosGastrointestinais['{}']" \
            " & astenia['{}'] & hiporexia['{}'] & dispneia['{}']," \
            "chanceEstarContaminado['{}'])".format(str(i), a[0], a[1], a[2], a[3], a[4],
                                                   a[5], a[6], a[7], a[8], a[9], chance)
    arquivo += atual + "\n"
    # print(atual)
    i += 1
f = open("Regras.py", "w")
f.write(arquivo)
