import os

def nuovaPartita():
    dati=dict()

    while True:
        dati["nomeFile"]=input("nome file: (senza .pgn) ")

        if not os.path.exists(dati["nomeFile"]+".pgn"):
            break
        else:
            print("il nome del file è già occupato")

    dati["evento"]=input("evento: ")
    dati["luogo"]=input("luogo: ")
    dati["data"]=input("data: ")
    dati["ora"]=input("ora: ")

    dati["round"]=input("round: ")
    dati["scacchiera"]=input("scacchiera: ")
    dati["risultato"]=input("risultato: ")
    dati["terminazione"]=input("terminazione: ")
    dati["tempo"]=input("tempo: ")

    dati["nomeBianco"]=input("nome bianco: ")
    dati["eloBianco"]=input("elo bianco: ")
    dati["titoloBianco"]=input("titolo bianco: ")

    dati["nomeNero"]=input("nome nero: ")
    dati["eloNero"]=input("elo nero: ")
    dati["titoloNero"]=input("titolo nero: ")

    dati["mosse"]=input("mosse: ")

    f=open(dati["nomeFile"]+".pgn","w")

    for x in dati:
        if x!="mosse":
            f.write('[' + x + ' "' + dati[x] + '"]\n')
        else:
            f.write("\n"+dati[x])

    f.close()



def modificaPartita():
    while True:
        dati["nomeFile"]=input("nome file: (senza .pgn) ")

        if os.path.exists(dati["nomeFile"]+".pgn"):
            break
        else:
            print("il file non esiste")

    indici=["nomeFile", "evento", "luogo", "data", "ora", "round", "scacchiera", "risultato", "terminazione", "tempo", "nomeBianco", "eloBianco", "titoloBianco", "nomeNero", "eloNero", "titoloNero", "mosse"]
    while True:
        indice=input("che cosa vuoi modificare? ")

        if indice in indici:
            break

    elemento=input("con cosa vuoi modificarlo? ")

    f.open(nomeFile+".pgn","r")

    i=0
    for linea in f.readlines():
        copia[i]=linea
        i+=1

    f.close()

    os.remove(nomeFile+".pgn")

    f.open(nomeFile+".pgn","w")

    for x in copia:
        if indice in x:
            f.wite('[' + indice + ' "' + elemento + '"]')
        else:
            f.write(x)

    f.close()



def eliminaPartita():
    while True:
        dati["nomeFile"]=input("nome file: (senza .pgn) ")

        if os.path.exists(dati["nomeFile"]+".pgn"):
            break
        else:
            print("il file non esiste")

    os.remove(nomeFile+".pgn")

nuovaPartita()
