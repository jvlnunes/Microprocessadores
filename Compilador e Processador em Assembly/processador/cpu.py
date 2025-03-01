# Em processador/cpu.py
from processador.registers import Registers
from processador.instruction_set import InstructionSet
from processador.memory import Memory
from processador.io_devices import Keyboard, Monitor

class CPU:
    def __init__(self):
        self.registers = Registers()       # Instância dos registradores
        self.memory = Memory(256)          # Memória com 256 posições
        self.instruction_set = InstructionSet(self.registers)
        self.pc = 0                        # Contador de programa
        self.running = True

    def load_program(self, machine_code):
        # Carrega o código de máquina na memória
        for i, code in enumerate(machine_code):
            self.memory.write(i, code)

    def fetch(self):
        instr = self.memory.read(self.pc)
        self.pc += 1
        return instr

    def run(self):
        print("\nIniciando execução no processador...")
        while self.running and self.pc < len(self.memory.memory):
            instr = self.fetch()
            print("Executando instrução:", instr)
            if instr == 0:
                self.running = False

if __name__ == "__main__":
    cpu = CPU()
    cpu.load_program([0x01, 10, 0x02, 0x00])
    cpu.run()
