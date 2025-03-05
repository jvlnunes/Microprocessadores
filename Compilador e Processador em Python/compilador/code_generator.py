class CodeGenerator:
    OPCODES = {
        'MOV': '0001',
        'ADD': '0010',
        'SUB': '0011',
        'CMP': '0100',
        'JMP': '0101',
    }
    
    REGISTER_MAP = {
        'R1': '0001',
        'R2': '0010',
        'R3': '0011',
    }
    
    def __init__(self, ast):
        self.ast = ast
        self.labels = {}
        self.output = []
    
    def first_pass(self):
        """Mapeia os labels para endereços de memória."""
        address = 0
        for node in self.ast:
            if node[0] == 'LABEL':
                self.labels[node[1][:-1]] = address  # Remove ':'
            else:
                address += 1
    
    def second_pass(self):
        """Gera código binário/máquina para cada instrução."""
        for node in self.ast:
            if node[0] == 'INSTRUCTION':
                instr, operands = node[1], node[2]
                opcode = self.OPCODES.get(instr, '0000')
                operand_bits = []
                
                for operand in operands:
                    if operand[0] == 'REGISTER':
                        operand_bits.append(self.REGISTER_MAP.get(operand[1], '0000'))
                    elif operand[0] == 'NUMBER':
                        operand_bits.append(format(int(operand[1]), '04b'))  # Converte número para binário (4 bits)
                    elif operand[0] == 'IDENTIFIER':
                        operand_bits.append(format(self.labels.get(operand[1], 0), '04b'))  # Endereço do label
                
                machine_code = opcode + ''.join(operand_bits)
                self.output.append(machine_code)
        
        return self.output
    
    def generate(self):
        self.first_pass()
        return self.second_pass()

# Exemplo de uso
if __name__ == "__main__":
    from parser import Parser
    from lexer import tokenize
    
    assembly_code = """
        MOV R1, 10
        ADD R2, R1
        loop: SUB R1, 1
        CMP R1, 0
        JMP loop
    """
    tokens = tokenize(assembly_code)
    parser = Parser(tokens)
    ast = parser.parse()
    generator = CodeGenerator(ast)
    machine_code = generator.generate()
    
    print("Código gerado:")
    for line in machine_code:
        print(line)
