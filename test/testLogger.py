import sys
import unittest
from os import path
from os import remove

sys.path.append(r'''C:\Users\vlonc_000\Envs\mbtcp-proj\src\mbtcp-proj''')
import logger


class MyTestCase(unittest.TestCase):
    def test_if_the_file_is_created(self):
        #given
        msg = "El archivo ha sido creado con Exito"
        ruta = r'''C:\Users\vlonc_000\Documents'''
        archivo = "mdbtcp-log1.txt"
        ruta_completa=ruta+"\\"+archivo

        logfile = logger.Logger(ruta_completa)
        logfile.write(msg)
        self.assertTrue(path.exists(ruta_completa))
        remove(ruta_completa)

    def test_if_can_read_a_buffer(self):
        self.assertTrue(False)
    

if __name__ == '__main__':
    unittest.main()
