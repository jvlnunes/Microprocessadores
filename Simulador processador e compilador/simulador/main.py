from processador.cpu import CPU
from processador.memory import Memory
from processador.io_devices import IODevices
from processador.control_unit import ControlUnit  
from simulador.logger import setup_logger
from simulador.display import Display
from simulador.controls import Controls

def main():
    logger = setup_logger()
    display = Display()
    controls = Controls()
    
    
    machine_code = [1, (1, 'R'), (10, 'I'), 2, (2, 'R'), (1, 'R'),
                    3, (1, 'R'), (1, 'I'), 6, (1, 'R'), (0, 'I'),
                    7, (6, 'I')]   
    
    memory = Memory(256)
    memory.load(machine_code)
    io_devices = IODevices()
    cpu = CPU(memory, io_devices)
    logger.info("Iniciando simulação.")
    while not cpu.halted and cpu.pc < len(memory.memory):
        cpu.step()  
        display.update(cpu, memory, io_devices)
        controls.wait_for_step()  

if __name__ == "__main__":
    main()
