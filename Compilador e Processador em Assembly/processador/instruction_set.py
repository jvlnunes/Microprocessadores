class InstructionSet:
    def __init__(self, registers):
        self.registers = registers  # Passa a instância de Registers

    def mov(self, operands):
        dest, src = operands

        if dest not in self.registers.registers:
            raise ValueError(f"Registrador {dest} não existe.")

        if src in self.registers.registers:
            value = self.registers.get_register(src)
        elif src.isdigit():
            value = int(src)
        else:
            raise ValueError(f"Operação MOV inválida: {src} não é um registrador nem um número.")

        self.registers.set_register(dest, value)

    def add(self, operands):
        dest, src = operands
        value = self.registers.get_register(src)
        self.registers.set_register(dest, self.registers.get_register(dest) + value)

    def sub(self, operands):
        dest, src = operands
        value = self.registers.get_register(src)
        self.registers.set_register(dest, self.registers.get_register(dest) - value)

    def cmp(self, operands):
        op1, op2 = operands
        value1 = self.registers.get_register(op1)
        # Se op2 for um número (string composta apenas por dígitos), converte para int
        if op2.isdigit():
            value2 = int(op2)
        else:
            value2 = self.registers.get_register(op2)
        result = value1 - value2
        self.registers.set_flag("ZF", result == 0)
        self.registers.set_flag("SF", result < 0)

    def out(self, operands):
        reg = operands[0]
        print(f"Valor de {reg}: {self.registers.get_register(reg)}")

# Teste básico
if __name__ == "__main__":
    from registers import Registers

    regs = Registers()
    instruction_set = InstructionSet(regs)

    # Teste de MOV
    instruction_set.mov(['R1', '5'])
    print("Valor de R1 após MOV:", regs.get_register("R1"))

    # Teste de ADD
    instruction_set.add(['R1', 'R1'])
    print("Valor de R1 após ADD:", regs.get_register("R1"))

    # Teste de CMP (com número literal "10")
    instruction_set.cmp(['R1', '10'])
    print("Zero Flag após CMP:", regs.get_flag("ZF"))
    print("Sign Flag após CMP:", regs.get_flag("SF"))

    # Teste de OUT
    instruction_set.out(['R1'])
