from pynput.mouse import Controller
from screeninfo import get_monitors

from pyres.environment import intfile
from pyres.habiticafuncs import setmoney, getmoney
from pyres.logics import int_or_z
from tkinter import Button, Tk, Toplevel, Label
from tkinter import FLAT as TkFLAT


def readint(intfile):
    try:
        with open(intfile, 'r') as file:
            return int_or_z(file.read())
    except FileNotFoundError:
        return 0


def setmenuvoice(nome, durata, prezzo):
    return {
        "nome": nome,
        "durata": durata,
        "prezzo": prezzo
    }


def create_button(
                    finestra
                  , root
                  , voce
                  , dimfont
                  , fg
                  , bg
                  , fga
                  , bga
                 ):
    if voce["nome"] == "lascia perdere":
        testo  = "lascia perdere"
        prezzo = 0
        tempo  = 0
    else:
        testo = f"{voce['nome']} per {voce['durata']}min: {voce['prezzo']}"
        prezzo = voce["prezzo"]
        tempo = voce["durata"]
    oro = getmoney()
    return Button(
                  finestra
                , text=testo
                , command=lambda l_oro      = oro
                               , l_prezzo   = prezzo
                               , l_tempo    = tempo
                               , l_finestra = finestra
                               , l_root     = root
                               : fun_a(l_oro, l_prezzo, l_tempo, l_finestra, l_root)
                , relief=TkFLAT
                , font="OperatorMonoLig " + str(dimfont) + " italic"
                , borderwidth=0
                , bg=bg
                , fg=fg
                , highlightthickness=0
                , activebackground=bga
                , activeforeground=fga
                , anchor="e"
                , justify="right"
    )


def fun_a(gold, prezzo, tempo, fin, root):
    with open(intfile, 'r') as file:
        time_c = file.read()
    if prezzo <= gold:
        setmoney(gold - prezzo)
        time_c = str((int(time_c) // 60 + tempo) * 60)
        with open(intfile, 'w') as file:
            file.write(str(time_c))
    closeall(fin, root)


def closeall(win, root):
    win.destroy()
    root.quit()


def getscreen(xy):
    schermo = get_monitors()[0]
    return xy and schermo.height or schermo.width


def getmouse(xy):
    return Controller().position[xy]


def crea_finestra_fantasma():
    finestra = Tk()
    finestra.geometry("1x1")
    finestra.overrideredirect(True)
    finestra.configure(
        bg="#141414"
    )
    finestra.withdraw()
    return finestra


def creapopupmenu(genitore):
    popup = Toplevel(genitore)
    popup.attributes("-topmost", True)
    popup.overrideredirect(True)
    popup.configure(
        bg="#141414"
    )
    return popup


def set_titolo(testo, genitore):
    titolo = Label(
        genitore
        , text=testo
        , font="OperatorMonoLig " + "12" + " italic"
        , borderwidth=0
        , bg="#141414"
        , fg="#AA3933"
        , highlightthickness=0
    )
    titolo.pack()
    return titolo



