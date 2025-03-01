class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos    = 0     
        self.ast    = []    

    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        
        return None

    def consume(self):
        """Consome o token atual e avança para o próximo."""
        token = self.peek()
        if token:
            self.pos += 1
        return token

    def parse_instruction(self):
        """Analisa uma instrução Assembly e seus operandos."""
        instr = self.consume()
        if instr[0] != 'INSTRUCTION':
            raise SyntaxError(f'Esperado uma instrução, encontrado {instr}')

        operands = []
        while self.peek() and self.peek()[0] in ('REGISTER', 'NUMBER', 'IDENTIFIER'):
            operands.append(self.consume())
            
            if self.peek() and self.peek()[0] == 'SEPARATOR':
                self.consume()  # Ignora a vírgula
        
        self.ast.append(('INSTRUCTION', instr[1], operands))
    
    def parse_label(self):
        """Analisa um rótulo (label)."""
        label = self.consume()
        self.ast.append(('LABEL', label[1]))

    def parse(self):
        """Percorre os tokens e constrói a AST."""
        while self.peek():
            token_type, value = self.peek()
            
            if token_type == 'INSTRUCTION':
                self.parse_instruction()
                
            elif token_type == 'LABEL':
                self.parse_label()
                
            elif token_type == 'COMMENT':
                self.consume()  # Ignora comentários
                
            else:
                raise SyntaxError(f'Token inesperado: {value}')
        
        return self.ast

# Exemplo de uso
if __name__ == "__main__":
    from lexer import tokenize
    
    assembly_code = """
        MOV R1, 10      ; Move 10 para R1
        ADD R2, R1      ; Soma R1 em R2
        loop: SUB R1, 1 ; Decrementa R1
        CMP R1, 0       ; Compara R1 com 0
        JMP loop        ; Salta para loop se R1 não for zero
    """
    tokens = tokenize(assembly_code)
    parser = Parser(tokens)
    ast    = parser.parse()
    
    for node in ast:
        print(node)
