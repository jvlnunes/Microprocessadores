# processador/instruction_set.py
class InstructionSet:
    def __init__(self, registers):
        self.registers = registers  # Passa a instância de Registers

    def mov(self, operands):
        dest, src = operands

        if dest not in self.registers.registers:
            raise ValueError(f"Registrador {dest} não existe.")

        if isinstance(src, int):
            value = src
        elif isinstance(src, str):
            if src in self.registers.registers:
                value = self.registers.get_register(src)
            elif src.isdigit():
                value = int(src)
            else:
                raise ValueError(f"Operação MOV inválida: {src} não é um registrador nem um número.")
        else:
            raise ValueError(f"Tipo de operando inválido: {src}")

        self.registers.set_register(dest, value)

    def add(self, operands):
        dest, src = operands
        value = self.registers.get_register(src) if isinstance(src, str) and src in self.registers.registers else src
        self.registers.set_register(dest, self.registers.get_register(dest) + value)

    def sub(self, operands):
        dest, src = operands
        value = self.registers.get_register(src) if isinstance(src, str) and src in self.registers.registers else src
        self.registers.set_register(dest, self.registers.get_register(dest) - value)

    def cmp(self, operands):
        op1, op2 = operands
        value1 = self.registers.get_register(op1)
        if isinstance(op2, int):
            value2 = op2
        elif isinstance(op2, str):
            if op2.isdigit():
                value2 = int(op2)
            else:
                value2 = self.registers.get_register(op2)
        else:
            raise ValueError(f"Tipo de operando inválido em CMP: {op2}")
        
        result = value1 - value2
        self.registers.set_flag("ZF", result == 0)
        self.registers.set_flag("SF", result < 0)

    def out(self, operands):
        reg = operands[0]
        print(f"Valor de {reg}: {self.registers.get_register(reg)}")

    def jmp(self, operands):
        # Como o CPU ajusta o PC para saltos,
        # este método pode ser um no-op.
        pass

# Teste básico (se necessário)
if __name__ == "__main__":
    from registers import Registers
    regs = Registers()
    instr_set = InstructionSet(regs)
    # Exemplo: teste do JMP (não faz nada, mas deve ser encontrado)
    instr_set.jmp([2])
    print("Método JMP chamado com sucesso!")
