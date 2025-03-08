class SemanticAnalyzer:
    INSTRUCTION_OPERANDS = {
        'MOV': ['REGISTER'  , 'NUMBER'    ],
        'ADD': ['REGISTER'  , 'REGISTER'  ],
        'SUB': ['REGISTER'  , 'NUMBER'    ],
        'CMP': ['REGISTER'  , 'NUMBER'    ],
        'JMP': ['IDENTIFIER'              ],
    }
    
    def __init__(self, ast):
        self.ast = ast
        self.labels = set()
    
    def check_labels(self):
        for node in self.ast:
            if node[0] == 'LABEL':
                self.labels.add(node[1][:-1])  # Remove ':'
    
    def analyze(self):
        self.check_labels()
        
        for node in self.ast:
            if node[0] == 'INSTRUCTION':
                instr, operands = node[1], node[2]
                expected_types = self.INSTRUCTION_OPERANDS.get(instr)
                
                if expected_types is None:
                    raise ValueError(f'Instrução desconhecida: {instr}')
                
                if len(operands) != len(expected_types):
                    raise ValueError(f'Erro de operandos em {instr}: esperado {expected_types}, recebido {operands}')
                
                for (expected, received) in zip(expected_types, operands):
                    if received[0] != expected:
                        raise ValueError(f'Tipo de operando inválido em {instr}: esperado {expected}, recebeu {received[0]}')
                
                if instr == 'JMP' and operands[0][1] not in self.labels:
                    raise ValueError(f'Label indefinido: {operands[0][1]}')
        
        print("Análise semântica concluída com sucesso!")
        return True

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
    analyzer = SemanticAnalyzer(ast)
    analyzer.analyze()
