import re

# Definição de padrões para os tokens
token_patterns = [
    (r'\bMOV\b|\bADD\b|\bSUB\b|\bMUL\b|\bDIV\b|\bJMP\b|\bCMP\b' , 'INSTRUCTION' ),  # Instruções básicas
    (r'\bR[0-9]+\b'                                             , 'REGISTER'    ),  # Registradores (exemplo: R1, R2, R3...)
    (r'\b[0-9]+\b'                                              , 'NUMBER'      ),  # Números inteiros
    (r'\b[A-Za-z_][A-Za-z0-9_]*:'                               , 'LABEL'       ),  # Rótulos (exemplo: loop:)
    (r'\b[A-Za-z_][A-Za-z0-9_]*\b'                              , 'IDENTIFIER'  ),  # Identificadores genéricos (exemplo: loop sem dois-pontos)
    (r';.*'                                                     , 'COMMENT'     ),  # Comentários
    (r'[\,]'                                                    , 'SEPARATOR'   ),  # Separadores como vírgula
    (r'[\n\t ]+'                                                , None          ),  # Espaços e quebras de linha (ignorados)
]

def tokenize(code):
    tokens = []
    
    while code:
        match = None
        
        for pattern, token_type in token_patterns:
            regex = re.compile(pattern)
            match = regex.match(code)
            
            if match:
                if token_type:  # Ignorar tokens do tipo None (espaços, quebras de linha...)
                    tokens.append((token_type, match.group(0)))
                    
                code = code[match.end():]  # Avançar no código
                break
            
        if not match:
            raise SyntaxError(f"Token desconhecido: {code[:10]}")  # Erro se não reconhecer o token
        
    return tokens

if __name__ == "__main__":
    assembly_code = """
        MOV R1, 10      ; Move 10 para R1
        ADD R2, R1      ; Soma R1 em R2
        loop: SUB R1, 1 ; Decrementa R1
        CMP R1, 0       ; Compara R1 com 0
        JMP loop        ; Salta para loop se R1 não for zero
    """
    tokens = tokenize(assembly_code)
    for token in tokens:
        print(token)
