from pyres.environment import intfile
from pyres.logics import no_z, is_sn, add_cln, add_z, is_dn, is_z
from pyres.miscfuncs import readint


def writetime(t=0):
    with open(intfile, 'w') as file:
        file.write(str(max(t,1) - 1))


def calcore():
    return readint(intfile) // 3600


def texore():
    return str(calcore())


def calcmin():
    return readint(intfile) % 3600 // 60


def texmin():
    return str(calcmin())


def calcsec():
    return readint(intfile) % 60


def texsec():
    return str(calcsec())


def dep_ore():
    return no_z(calcore()) * (texore() + ":")


def set_ore():
    return dep_ore()


def set_min():
    return (
            (is_sn(calcmin()) * no_z(calcore())) * add_cln(add_z(texmin()))
           ) + (
                bool(is_dn(calcmin()) + (is_z(calcore()) * no_z(calcmin()))) * add_cln(texmin())
               ) + (
                    (no_z(calcore()) * is_z(calcmin())) * "00:"
                   ) + (
                        is_z(calcore()) * is_z(calcmin()) * ""
                       ) + ""


def set_sec():
    # noinspection PyTypeChecker
    return (
            (bool(no_z(calcmin()) + no_z(calcore())) * is_sn(calcsec())) * add_z(texsec())
           ) + (
                bool(is_dn(calcsec()) + (is_z(calcore()) * is_z(calcmin()))) * texsec()
               ) + (
                    no_z(calcmin()+calcore()) * is_z(calcsec()) * "00"
                   ) + (
                        (is_z(calcore()) * is_z(calcmin()+calcsec())) * "0"
                       ) + ""


def set_time():
    return set_ore() + set_min() + set_sec()


def formattime(colore, testo, f_time):
    return (
            "<txt>"
                f"<span fgcolor='{colore}' size='14pt' style='italic' weight='bold'>"
                    f"{testo}{f_time()}  "
                "</span>"
            "</txt>"
           )
