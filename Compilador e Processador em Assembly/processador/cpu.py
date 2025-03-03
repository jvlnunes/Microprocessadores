# Processador/cpu.py

from processador.registers import Registers
from processador.instruction_set import InstructionSet
from processador.memory import Memory

class CPU:
    def __init__(self):
        self.registers = Registers()       # Instância dos registradores
        self.memory = Memory(256)          # Memória com 256 posições
        self.instruction_set = InstructionSet(self.registers)
        self.pc = 0                        # Program Counter
        self.running = True
        # Mapeamento de opcode para (nome da instrução, número de operandos)
        self.instruction_format = {
            1: ("MOV", 2),
            2: ("ADD", 2),
            3: ("SUB", 2),
            4: ("MUL", 2),
            5: ("DIV", 2),
            6: ("CMP", 2),
            7: ("JMP", 1),
        }
    
    def load_program(self, machine_code):
        # Carrega o código de máquina na memória
        for i, code in enumerate(machine_code):
            self.memory.write(i, code)
        print("Memória carregada:", self.memory.dump())
    
    def fetch(self):
        # Busca o próximo valor da memória e incrementa o PC
        value = self.memory.read(self.pc)
        self.pc += 1
        return value
    
    def run(self):
        print("\nIniciando execução no processador...")
        while self.running and self.pc < len(self.memory.memory):
            opcode = self.fetch()
            if opcode == 0:
                break  # Fim do programa (opcode 0)
            if opcode not in self.instruction_format:
                raise ValueError("Opcode desconhecido: " + str(opcode))
            instr_name, num_operands = self.instruction_format[opcode]
            # Busca os operandos conforme o número esperado
            raw_operands = [self.fetch() for _ in range(num_operands)]
            
            # Função para converter operandos usando a informação de tipo:
            def convert_operand(op, instr, pos):
                # Se o operando for uma tupla, usamos a flag:
                if isinstance(op, tuple):
                    val, typ = op
                    if typ == 'R':
                        return "R" + str(val)
                    elif typ == 'I':
                        return val
                # Caso contrário, fallback (não esperado)
                else:
                    if instr in ["MOV", "ADD", "SUB", "CMP"]:
                        if pos == 0:
                            return "R" + str(op)
                        else:
                            return op
                    elif instr == "JMP":
                        return op
                    else:
                        return op
            
            converted_operands = [convert_operand(op, instr_name, i) for i, op in enumerate(raw_operands)]
            print(f"Decodificado: {instr_name} {converted_operands}")
            
            method = getattr(self.instruction_set, instr_name.lower(), None)
            if method is None:
                raise ValueError("Instrução não implementada: " + instr_name)
            method(converted_operands)
            
            # Se a instrução for JMP, ajusta o PC para o destino do salto
            if instr_name == "JMP":
                self.pc = converted_operands[0]
            
            if self.pc >= len(self.memory.memory):
                self.running = False

if __name__ == "__main__":
    # Para teste isolado:
    # Código de máquina esperado (gerado pelo assembler):
    # [1, (1,'R'), (10,'I'), 2, (2,'R'), (1,'R'), 3, (1,'R'), (1,'I'), 6, (1,'R'), (0,'I'), 7, (6,'I')]
    machine_code = [1, (1,'R'), (10,'I'), 2, (2,'R'), (1,'R'),
                    3, (1,'R'), (1,'I'), 6, (1,'R'), (0,'I'),
                    7, (6,'I')]
    cpu = CPU()
    cpu.load_program(machine_code)
    cpu.run()
