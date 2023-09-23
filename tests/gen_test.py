from gnupg import GPG
from unittest import TestCase, main
from unittest.mock import patch, Mock
import tempfile
from os import remove
from pyres.environment import gethomedir
from pyres.gpgfuncs import decifra, decifrafile, is2lines, credenzialiapi, FileDecryptionError
import timer


def get_public_key():
    return 'A0FCB5A27C1ED66B5BC6D030862A9198690C1B67'


class TestDecifra(TestCase):
    def test_decifra(self):
        temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
        temp_file.write("Test linea 1\nTest linea 2")
        temp_file.close()
        recipient_key = get_public_key()
        gpg = GPG()
        encrypted_file = temp_file.name + ".gpg"
        gpg.encrypt_file(temp_file.name, recipients=recipient_key, output=encrypted_file)
        risultato_decifra = decifra(encrypted_file)
        remove(encrypted_file)
        with self.assertRaises(FileNotFoundError, msg=f"Errore nella funzione {decifra.__name__}: File non trovato."):
            decifra("qwertyasdfghzxcvbn")
        with self.assertRaises(FileDecryptionError, msg=f"Avviso dalla funzione {decifra.__name__}: il file non è cifrato"):
            decifra(temp_file.name)
        self.assertTrue(risultato_decifra.ok)

    def test_decifrafile(self):
        temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
        temp_file.write("Test linea 1\nTest linea 2")
        temp_file.close()
        recipient_key = get_public_key()
        gpg = GPG()
        encrypted_file = temp_file.name + ".gpg"
        gpg.encrypt_file(temp_file.name, recipients=recipient_key, output=encrypted_file, always_trust=True)
        risultato_decifrafile = decifrafile(encrypted_file)
        remove(encrypted_file)

        self.assertIsInstance(risultato_decifrafile, list)
        self.assertTrue(len(risultato_decifrafile) == 2)
        self.assertEqual(risultato_decifrafile[0].decode('utf-8'), "Test linea 1")
        self.assertEqual(risultato_decifrafile[1].decode('utf-8'), "Test linea 2")

    def test_datareduce(self):
        self.assertTrue(is2lines([1, 2]))
        self.assertFalse(is2lines([1, 2, 3, 4]))
        self.assertIsInstance(is2lines([1, 2, 3]), bool)

    def test_credenzialiapi(self):
        temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
        temp_file.write("Test linea 1\nTest linea 2")
        temp_file.close()
        recipient_key = get_public_key()
        gpg = GPG()
        encrypted_file = temp_file.name + ".gpg"
        gpg.encrypt_file(temp_file.name, recipients=recipient_key, output=encrypted_file)
        risultato_decifrafile = credenzialiapi(encrypted_file)
        remove(encrypted_file)

        self.assertIsInstance(risultato_decifrafile, tuple)
        self.assertEqual(risultato_decifrafile[0].decode('utf-8'), "Test linea 1")
        self.assertEqual(risultato_decifrafile[1].decode('utf-8'), "Test linea 2")


class TestGetHomeDir(TestCase):

    @patch('pyres.environment.system', new_callable=Mock, return_value='Linux')
    @patch('pyres.environment.getenv', new_callable=Mock, return_value='/home/user')
    def test_gethomedir_linux(self, mock_getenv, mock_system):
        result = gethomedir()
        self.assertEqual(result, '/home/user')

    @patch('pyres.environment.system', new_callable=Mock, return_value='Windows')
    @patch('pyres.environment.getenv', new_callable=Mock, return_value='C:\\Users\\user')
    def test_gethomedir_windows(self, mock_getenv, mock_system):
        result = gethomedir()
        self.assertEqual(result, 'C:\\Users\\user')

    @patch('pyres.environment.system', new_callable=Mock, return_value='Other')
    def test_gethomedir_other(self, mock_system):
        result = gethomedir()
        self.assertEqual(result, '')


class TestWriteoutTimer(TestCase):

    @patch('timer.chabitica')
    @patch('timer.readint')
    @patch('timer.set_time')
    @patch('timer.print')
    def test_writeout_timer_remaining_time(self, mock_print, mock_set_time, mock_readint, mock_chabitica):
        mock_readint.return_value = 1
        timer.writeout_timer()
        # Verifica che la funzione chabitica sia stata chiamata
        mock_chabitica.assert_called()
        # Verifica che la funzione readint sia stata chiamata
        mock_readint.assert_called_with(timer.intfile)
        # Verifica che set_time sia stato chiamato con il valore corretto
        mock_set_time.assert_called_with()
        # Verifica che print sia stato chiamato con il testo corretto
        mock_print.assert_called_with(timer.settxt(timer.setspan(
            f"Tempo rimanente: {mock_set_time()}", timer.setfont(*timer.time_text_font))))

    @patch('timer.chabitica')  # Sostituire 'timer' con il nome effettivo del modulo
    @patch('timer.readint')
    @patch('timer.print')
    def test_writeout_timer_timeout(self, mock_print, mock_readint, mock_chabitica):
        mock_readint.return_value = 0
        timer.writeout_timer()
        # Verifica che la funzione chabitica sia stata chiamata
        mock_chabitica.assert_called()
        # Verifica che la funzione readint sia stata chiamata
        mock_readint.assert_called_with(timer.intfile)
        # Verifica che print sia stato chiamato con il testo corretto
        mock_print.assert_called_with(timer.settxt(timer.setspan(
            "Tempo esaurito", timer.setfont(*timer.timeout_text_font))))


if __name__ == "__main__":
    main()

