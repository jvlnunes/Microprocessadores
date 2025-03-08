class Display:
    def update(self, cpu, memory, io_devices):
        """
        Exibe o estado atual da simulação (por exemplo, PC, registradores e saída de I/O).
        """
        print("\n========== Estado da Simulação ==========")
        # Exibe o contador de programa
        print("PC:", cpu.pc)
        # Exibe os registradores (supondo que cpu.registers seja um dicionário ou forneça um método de dump)
        print("Registradores:")
        try:
            # Se cpu.registers for um objeto com atributo 'registers'
            for reg, val in cpu.registers.registers.items():
                print(f"  {reg}: {val}")
        except AttributeError:
            # Caso seja um dicionário diretamente
            for reg, val in cpu.registers.items():
                print(f"  {reg}: {val}")
        # Exibe a saída de I/O (simulação de monitor)
        print("I/O Output:")
        for line in io_devices.output_buffer:
            print("  ", line)
        print("==========================================\n")

# Exemplo de uso:
if __name__ == "__main__":
    # Exemplo dummy para teste
    class DummyCPU:
        def __init__(self):
            self.pc = 42
            self.registers = {'R1': 10, 'R2': 20, 'R3': 0}
    class DummyIO:
        def __init__(self):
            self.output_buffer = ["Hello, World!", "Simulação em andamento..."]
    
    display = Display()
    dummy_cpu = DummyCPU()
    dummy_io = DummyIO()
    display.update(dummy_cpu, None, dummy_io)
