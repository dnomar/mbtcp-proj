
class Logger:

    def __init__(self, ruta):
        self.ruta = ruta

    def write(self, msg):

        f = open(self.ruta, "a")
        f.write(msg)
        f.close()

    def buff_reader(self):
        pass
