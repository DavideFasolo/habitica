from tkinter import X as TkX
from pyres.habiticafuncs import getmoney
from pyres.miscfuncs import create_button, getscreen, getmouse, crea_finestra_fantasma, creapopupmenu, set_titolo, setmenuvoice
from pyres.environment import X, Y, chabitica

chabitica()
gold = getmoney()

m_x = min(getmouse(X), getscreen(X) - 200)
m_y = max(getmouse(Y), 300)


root = crea_finestra_fantasma()
popup_menu = creapopupmenu(root)


voices = [
    setmenuvoice("Cazzeggio", 60, 5),
    setmenuvoice("Cazzeggio utile", 60, 0.5),
    setmenuvoice("Gaming", 60, 4),
    setmenuvoice("serie o film", 60, 4),
    setmenuvoice("Film", 240, 5)
]


set_titolo("Acquista tempo:", popup_menu)


for i in voices:
    btn_x = create_button(
                            popup_menu
                          , root
                          , i
                          , "12"
                          , "#ADADAD"
                          , "#141414"
                          , "#5B9631"
                          , "#141414"
    )
    btn_x.pack(fill=TkX)


btn_z = create_button(
                        popup_menu
                      , root
                      , { "nome": "lascia perdere" }
                      , "12"
                      , "#4E8392"
                      , "#141414"
                      , "#5B9631"
                      , "#141414"
                     )


btn_z.pack(fill=TkX)


popup_menu.geometry(
                    f"+{m_x}+{m_y - round((len(voices) * (16)) * 2.7)}"
                   )


popup_menu.mainloop()
