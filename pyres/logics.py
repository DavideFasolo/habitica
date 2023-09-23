def int_or_z(val):
    try:
        return int(val)
    except ValueError:
        return 0


def no_z(n):
    """
    verifica se n!=0
    """
    return bool(n)


def is_z(n):
    """
    verifica se n==0
    """
    return not(bool(n))


def is_sn(n):
    """
    verifica se 0 < n < 10
    """
    return bool(no_z(n) * (n < 10))


def is_dn(n):
    """
    verifica se n>=10
    """
    return ( n > 9 )


def add_z(n):
    """
    aggiunge uno zero prima del numero
    """
    return "0" + n


def add_cln(n):
    """
    aggiunge ":" dopo il numero
    """
    return str(n + ":")
