# Compilador/assembler.py

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
    
    # Tamanho (em células) que cada instrução ocupa na memória
    INSTRUCTION_LENGTHS = {
        'MOV': 3,
        'ADD': 3,
        'SUB': 3,
        'MUL': 3,
        'DIV': 3,
        'CMP': 3,
        'JMP': 2,
    }
    
    def __init__(self, ast):
        self.ast = ast
        self.labels = {}       # Armazena os endereços (índices) dos labels
        self.machine_code = [] # Lista que conterá o código de máquina
    
    def first_pass(self):
        address = 0
        for node in self.ast:
            if node[0] == 'LABEL':
                # Remove ':' do rótulo e armazena o endereço real
                label = node[1][:-1]
                self.labels[label] = address
                print(f"Label '{label}' definido em endereço {address}")
            else:
                instr = node[1].upper()  # Normaliza para maiúsculas
                length = self.INSTRUCTION_LENGTHS.get(instr, 1)
                print(f"Instrução {instr} com tamanho {length} encontrada em endereço {address}")
                address += length  
    
    def second_pass(self):
        for node in self.ast:
            if node[0] == 'INSTRUCTION':
                instr, operands = node[1], node[2]
                opcode = self.OPCODE_TABLE.get(instr.upper(), None)
                if opcode is None:
                    raise ValueError(f'Instrução desconhecida: {instr}')
                
                binary_instr = [opcode]
                for operand in operands:
                    if operand[0] == 'REGISTER':
                        # Converte "R1" para (1, 'R'), "R2" para (2, 'R'), etc.
                        binary_instr.append((int(operand[1][1:]), 'R'))
                    elif operand[0] == 'NUMBER':
                        binary_instr.append((int(operand[1]), 'I'))
                    elif operand[0] == 'IDENTIFIER':  # Label usada em JMP
                        label = operand[1]
                        if label in self.labels:
                            binary_instr.append((self.labels[label], 'I'))
                        else:
                            raise ValueError(f'Label não definido: {label}')
                self.machine_code.extend(binary_instr)
    
    def assemble(self):
        self.first_pass()   # Calcula os endereços dos labels com base nos tamanhos reais
        self.second_pass()  # Converte a AST em código de máquina
        return self.machine_code

# Exemplo de uso (para testes isolados):
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
    assembler = Assembler(ast)
    machine_code = assembler.assemble()
    print("Código de Máquina Gerado:", machine_code)
