class Assembler:
    OPCODE_TABLE = {
        'MOV': 0x01,
        'ADD': 0x02,
        'SUB': 0x03,
        'MUL': 0x04,
        'DIV': 0x05,
        'CMP': 0x06,
        'JMP': 0x07,
    }
    
    def __init__(self, ast):
        self.ast          = ast
        self.labels       = {}  # Armazena os endereços dos rótulos
        self.machine_code = []
    
    def first_pass(self):
        address = 0
        for node in self.ast:
            if node[0] == 'LABEL':
                self.labels[node[1][:-1]] = address  # Remove ':' do rótulo
                
            else:
                address += 1  
    
    def second_pass(self):
        for node in self.ast:
            if node[0] == 'INSTRUCTION':
                instr, operands = node[1], node[2]
                opcode = self.OPCODE_TABLE.get(instr, None)
                
                if opcode is None:
                    raise ValueError(f'Instrução desconhecida: {instr}')
                
                binary_instr = [opcode]
                for operand in operands:
                    if operand[0] == 'REGISTER':
                        binary_instr.append(int(operand[1][1:]))  # R1 -> 1
                        
                    elif operand[0] == 'NUMBER':
                        binary_instr.append(int(operand[1]))
                        
                    elif operand[0] == 'IDENTIFIER':  # Label usada em JMP
                        if operand[1] in self.labels:
                            binary_instr.append(self.labels[operand[1]])
                            
                        else:
                            raise ValueError(f'Label não definido: {operand[1]}')
                
                self.machine_code.extend(binary_instr)
    
    def assemble(self):
        self.first_pass()  # Identifica labels
        self.second_pass()  # Converte para código binário
        
        return self.machine_code

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
    tokens       = tokenize(assembly_code)
    parser       = Parser(tokens)
    ast          = parser.parse()
    assembler    = Assembler(ast)
    machine_code = assembler.assemble()
    
    print(machine_code)
