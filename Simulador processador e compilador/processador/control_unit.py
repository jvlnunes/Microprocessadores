class ControlUnit:
    def __init__(self, cpu, memory, io_devices):
        self.cpu = cpu
        self.memory = memory
        self.io_devices = io_devices

    def start(self):
        """Inicia a simulação."""
        while not self.cpu.halted:
            self.cpu.step()
            # Aqui podemos imprimir o estado ou interagir com o usuário

    def stop(self):
        """Para a simulação."""
        self.cpu.halted = True
