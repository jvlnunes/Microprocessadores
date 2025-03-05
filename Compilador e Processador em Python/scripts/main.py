import sys
import os

# Diretório atual (scripts/)
current_dir = os.path.dirname(os.path.abspath(__file__))
print("Current Directory:", current_dir)

# Diretório raiz do projeto: subindo um nível (de scripts para "Compilador e Processador em Assembly")
project_root = os.path.abspath(os.path.join(current_dir, '..'))
print("Project ROOT:", project_root)

# Verifica se os diretórios 'compilador' e 'processador' existem no projeto raiz
compilador_dir = os.path.join(project_root, 'compilador')
processador_dir = os.path.join(project_root, 'processador')

if not os.path.exists(compilador_dir):
    print("Aviso: Diretório 'compilador' não encontrado em", project_root)
else:
    print("Diretório 'compilador' encontrado.")

if not os.path.exists(processador_dir):
    print("Aviso: Diretório 'processador' não encontrado em", project_root)
else:
    print("Diretório 'processador' encontrado.")

# Adiciona o diretório raiz ao sys.path
sys.path.insert(0, project_root)
print("sys.path atualizado:", sys.path)

# Importa os módulos do compilador e do processador
try:
    from compilador.lexer import tokenize
    from compilador.parser import Parser
    from compilador.semantic_analyzer import SemanticAnalyzer
    from compilador.assembler import Assembler
    from processador.cpu import CPU
except ModuleNotFoundError as e:
    print("Erro ao importar módulos:", e)
    sys.exit(1)

def main():
    assembly_code = """
        MOV R1, 10
        ADD R2, R1
        loop: 
            SUB R1, 1
            CMP R1, 0
            JZ end_loop  ; Salta para end_loop se R1 for 0
            JMP loop
        end_loop:

    """
    # Etapa 1: Tokenização
    tokens = tokenize(assembly_code)
    print("Tokens:", tokens)
    
    # Etapa 2: Parsing – gera a AST
    parser = Parser(tokens)
    ast = parser.parse()
    print("AST:", ast)
    
    # Etapa 3: Análise Semântica
    analyzer = SemanticAnalyzer(ast)
    analyzer.analyze()
    
    assembler = Assembler(ast)
    machine_code = assembler.assemble()
    print("Código de Máquina Gerado:", machine_code)
    
    cpu = CPU()
    cpu.load_program(machine_code)
    cpu.run()

if __name__ == "__main__":
    main()
