from os import path
from pyres.environment import habiticadir


def setclick(content):
    return "<txtclick>{}</txtclick>".format(content)


def settxt(content):
    return "<txt>{}</txt>".format(content)


def setspan(content, tagopts=""):
    return "<span{}>{}</span>".format(tagopts, content)


def setopt(name, value):
    return bool(value) * "{}='{}'".format(name, value) + ""


def setfont(
                 size   = ""
               , style  = ""
               , weight = ""
               , color  = ""
               , face   = ""
              ):
    return " " + str(" ").join([
                                  setopt( "size"    , size   )
                                , setopt( "style"   , style  )
                                , setopt( "weight"  , weight )
                                , setopt( "fgcolor" , color  )
                                , setopt( "font"    , face   )
                               ])


def writeclick(eseguibile):
    print(setclick(
        "python '{}'".format(
            path.join(
                habiticadir
                , eseguibile
            )
        )
    )
    )
