import requests as r
import time
import re

def esperarAte(hora, minuto):
    h = int(time.strftime("%H"))
    m = int(time.strftime("%M"))

    if (h > hora):
        horas = (24 - h) + hora
    else:
        horas = (hora - h)

    if (m > minuto):
        minutos = 60 - m + minuto
    else:
        minutos = minuto - m

    segundos = horas * 60 * 60 + minutos * 60 - int(time.strftime("%S"))
    print "Esperando: ", horas, ":", minutos, " ou ", segundos, " segundos"
    time.sleep(segundos)

def limpar():
    import os
    os.system("cls")


limpar()

tropas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
nomes = ["Lanceiros", "Espadachins", "Barbaros", "Exploradores", "Cavalaria leve", "Cavalaria pesada", "Ariates", "Catapultas", "Paladinos", "Nobres"]


def atacar(arq):
    with r.Session() as c:
        r.get("https://tribalwars.com.br", )
        info = dict(user="user", password="pass", sso="0")
        page = c.post("https://www.tribalwars.com.br/index.php?action=login&server_br78", data=info)
        time.sleep(1)

        arq = open(arq)

        for line in arq:
            l = line.split("|", 2)
            x = l[0]
            y = l[1]

            h = 'teste'
            for line in page.content.split("\n"):
                if "var csrf_token = " in line:
                    h = line

            h = re.search(r".+csrf_token = \'(.+)\'", h).groups(0)
            h = h[0]

            print "Token h: " + h

            info3 = dict(  # x089b503b8e6f830ca1c2b3a='37389c1589b503',
                template_id='',
                source_village='1411',
                spear=str(tropas[0]) if tropas[0] != 0 else '',
                sword=str(tropas[1]) if tropas[1] != 0 else '',
                axe=str(tropas[2]) if tropas[2] != 0 else '',
                spy=str(tropas[3]) if tropas[3] != 0 else '',
                light=str(tropas[4]) if tropas[4] != 0 else '',
                heavy=str(tropas[5]) if tropas[5] != 0 else '',
                ram=str(tropas[6]) if tropas[6] != 0 else '',
                catapult=str(tropas[7]) if tropas[7] != 0 else '',
                knight=str(tropas[8]) if tropas[8] != 0 else '',
                snob=str(tropas[9]) if tropas[9] != 0 else '',
                x=x,
                y=y,
                target_type='coord',
                input='',
                attack='Ataque')

            page3 = c.post("https://br78.tribalwars.com.br/game.php?village=1411&screen=place&try=confirm", data=info3)

            action_id = 'teste'
            ch = "teste"
            for line in page3.content.split("\n"):
                if 'name="action_id"' in line:
                    action_id = line
                if 'name="ch" value="' in line:
                    ch = line

            action_id = re.search(r".+name=\"action_id\" value=\"(.+)\"", action_id).groups(0)
            action_id = action_id[0]

            ch = re.search(r".+name=\"ch\" value=\"(.+)\"", ch).groups(0)
            ch = ch[0]
            print "action_id: " + action_id
            print "token ch: " + ch

            info2 = dict(attack="true", ch=ch,
                         x=x, y=y, source_village="1411", action_id=action_id,
                         spear=str(tropas[0]),
                         sword=str(tropas[1]),
                         axe=str(tropas[2]),
                         spy=str(tropas[3]),
                         light=str(tropas[4]),
                         heavy=str(tropas[5]),
                         ram=str(tropas[6]),
                         catapult=str(tropas[7]),
                         knight=str(tropas[8]),
                         snob=str(tropas[9]),
                         building="main",
                         )

            page2 = c.post("https://br78.tribalwars.com.br/game.php?village=1411&screen=place&action=command&h=" + h,
                           data=info2,
                           headers={
                               "Referer": 'https://br78.tribalwars.com.br/game.php?village=1411&screen=place&try=confirm'})
            print("Mandando ataque em " + x + "|" + y),
            time.sleep(1),


while(1):
    linha = str(raw_input("rqt# "))

    if "atk " in linha:
        coor = re.search(r"\-c ([0-9a-zA-Z\.]+)", linha).groups()
        arq = coor[0]

        tr = re.findall(r"(\-[0-9] [0-9]+)", linha)

        for l in tr:
            li = l.split(" ")
            li[0] = re.search(r"([0-9]+)", li[0]).groups()[0]
            tropas[int(li[0])] = li[1]

        print "Voce ira mandar:"
        cont = 0
        for l in tropas:
            if tropas[cont] != 0:
                print str(tropas[cont]) + " " + nomes[cont]
            cont+=1

        op = raw_input("[S/N]")
        if op != 's' and op !=  'S':
            continue

        if("-t" in linha):
            tempo = re.search(r"\-t ([0-9]+)\:([0-9]+)", linha).groups()
            print "achou"
            esperarAte(int(tempo[0]), int(tempo[1]))


        atacar(arq)
        print("\n"),
        tropas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    elif "lista" in linha:
        print("Lanceiro: -0")
        print("Espadachin: -1")
        print("Barbaro: -2")
        print("Explorador: -3")
        print("Cavalaria leve: -4")
        print("Cavalaria pesada: -5")
        print("Ariate: -6")
        print("Catapulta: -7")
        print("Paladino: -8")
        print("Nobre: -9")
    elif "cls" in linha:
        limpar()
    elif "exit" in linha:
        exit(0)





