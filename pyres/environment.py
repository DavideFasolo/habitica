from os import path, getenv, chdir
from platform import system
from pyres.gpgfuncs import credenzialiapi


def gethomedir():
    if system() == "Linux":
        return getenv("HOME")
    elif system() == "Windows":
        return getenv("USERPROFILE")
    else:
        return ""


habiticadir = path.join(gethomedir(), "scripts", "habitica")
cachedir = path.join(gethomedir(), "scripts", "habitica", "cache")

X = 0
Y = 1


api_user, api_key = credenzialiapi(
                                    path.join(
                                                habiticadir
                                              , "credenzialihabitica"
                                             )
)



userdata_url = "https://habitica.com/export/userdata.json"
user_url = "https://habitica.com/api/v3/user"

headers = {
              "x-api-user": api_user
            , "x-api-key": api_key
            , "x-client": api_user
            , "Content-Type": "application/json"
            ,
          }


intfile = path.join(  cachedir
                    , "timec"
                   )


def chabitica():
    chdir(habiticadir)


gold_symbol = chr(0xe26b)
gold_nerd_font = ["18pt", "italic", "bold", "#B3831D", "VictorMono Nerd Font Propo"]
gold_text_font = ["18pt", "italic", "", "#B3831D", "Operator Mono Light Italic"]
time_text_font = ["16pt", "italic", "", "#4C752F", "Operator Mono Italic"]
timeout_text_font = ["16pt", "italic", "", "#AA2217", "Operator Mono Italic"]
