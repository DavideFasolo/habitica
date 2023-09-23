from pyres.environment import chabitica, gold_symbol, gold_nerd_font, gold_text_font
from pyres.genmonscripting import settxt, setspan, setfont, writeclick
from pyres.habiticafuncs import getmoney

chabitica()
print(settxt(
                setspan(
                            gold_symbol
                          , setfont(*gold_nerd_font)
                )
                +
                setspan(
                            str(round(getmoney()))
                          , setfont(*gold_text_font)
                )
))

writeclick("goldmon_click.py")
