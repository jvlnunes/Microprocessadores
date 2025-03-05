class Keyboard:
    def __init__(self):
        self.buffer = []  

    def input_char(self, char):    
        self.buffer.append(char)

    def read_char(self):    
        if self.buffer:
            return self.buffer.pop(0)
        
        return None  

    def is_empty(self):
        return len(self.buffer) == 0


class Monitor:
    def __init__(self):
        self.output = []  

    def display_char(self, char):    
        self.output.append(char)
        print(char, end='', flush=True)  

    def clear_screen(self):    
        self.output = []
        print("\n" * 50)  


if __name__ == "__main__":
    keyboard = Keyboard()
    monitor  = Monitor()

    keyboard.input_char('H')
    keyboard.input_char('i')

    while not keyboard.is_empty():
        char = keyboard.read_char()
        if char:
            monitor.display_char(char)