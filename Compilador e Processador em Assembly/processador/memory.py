class Memory:
    def __init__(self, size=256):
        self.size = size
        self.memory = [0] * size 

    def write(self, address, value):
        if 0 <= address < self.size:
            self.memory[address] = value  # Removendo a operação bitwise
        else:
            raise ValueError(f"Endereço {address} fora dos limites da memória.")


    def read(self, address):
        if 0 <= address < self.size:
            return self.memory[address]
        else:
            raise ValueError(f"Endereço {address} fora dos limites da memória.")

    def dump(self, start=0, end=None):
        end = end if end else self.size
        return self.memory[start:end]

# Teste básico
if __name__ == "__main__":
    mem = Memory(256)
    mem.write(10, 42)
    print("Endereço 10:", mem.read(10)) 
    print("Dump de memória:", mem.dump(0, 16)) 
