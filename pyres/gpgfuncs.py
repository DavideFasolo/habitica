from functools import reduce
from gnupg import GPG
from os import path


class FileDecryptionError(Exception):
    pass


def decifra(file_cifrato):
    """
    Decifra un file usando GPG.

    Args:
        file_cifrato (str): Il percorso del file cifrato.

    Returns:
        decifrato (GPG): Il file decifrato come oggetto Decrypt.

    Raises:
        FileNotFoundError: Se il file cifrato non viene trovato.
        FileDecryptionError: Se si verificano errori durante la decifratura.
    """
    if not path.isfile(file_cifrato):
        raise FileNotFoundError(f"Errore nella funzione {decifra.__name__}: File non trovato.")
    decifrato = GPG().decrypt_file(file_cifrato)
    if decifrato.status == 'no data was found':
        raise FileDecryptionError(f"Avviso dalla funzione {decifra.__name__}: il file non è cifrato")
    if decifrato.status =='decryption failed':
        raise FileDecryptionError(f"Avviso dalla funzione {decifra.__name__}: frase chiave errata")
    if not decifrato.ok:
        raise FileDecryptionError(f"Avviso dalla funzione {decifra.__name__}: errore sconosciuto")
    return decifrato


def decifrafile(file_cifrato):
    try:
        decifrato = decifra(file_cifrato).data.splitlines()
        return decifrato
    except AttributeError:
        raise ValueError(
            f"Avviso dalla funzione {decifrafile.__name__}: impossibile eseguire 'splitlines()' sul contenuto del file"
        )


def is2lines(data):
    return not reduce(
        lambda a, b: (a[0] + [b], a[1] + 1), data, ([], 0)
    )[1] - 2


def credenzialiapi(file_credenziali):
    lines = decifrafile(file_credenziali)
    return is2lines(lines) * tuple(lines)
