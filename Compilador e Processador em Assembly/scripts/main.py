# Corrigindo problema com importação de módulos
import sys
import os

current_dir  = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..', 'Compilador e Processador em Assembly'))
sys.path.insert(0, project_root)

# Inicio da pipeline
from compilador.lexer             import tokenize
from compilador.parser            import Parser
from compilador.assembler         import Assembler
from compilador.semantic_analyzer import SemanticAnalyzer
from processador.cpu              import CPU

def main():
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
    
    assembler = Assembler(ast)
    machine_code = assembler.assemble()
    print("Código de Máquina Gerado:", machine_code)
    
    cpu = CPU()
    cpu.load_program(machine_code)
    cpu.run()

if __name__ == "__main__":
    main()
