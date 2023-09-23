from pyres.environment import intfile, chabitica, time_text_font, timeout_text_font
from pyres.genmonscripting import settxt, setspan, setfont, writeclick
from pyres.timefuncs import writetime, set_time, readint


def writeout_timer():
    chabitica()
    if readint(intfile):
        print(settxt(
                        setspan(
                                    f"Tempo rimanente: {set_time()}"
                                  , setfont(*time_text_font)
                        )
        ))
    else:
        print(settxt(
                        setspan(
                                    "Tempo esaurito"
                                  , setfont(*timeout_text_font)
                        )
        ))
    writetime(readint(intfile))
    writeclick("timerclick.py")
writeout_timer()



