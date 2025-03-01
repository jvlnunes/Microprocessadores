class Registers:
    def __init__(self):
        self.registers = {
            "R1": 0,
            "R2": 0,
            "R3": 0
        }
        
        self.flags = {
            "ZF": 0, 
            "CF": 0, 
            "SF": 0, 
            "PF": 0, 
            "IF": 0, 
            "DF": 0, 
            "OF": 0  
        }

    def set_register(self, reg, value):
        if reg in self.registers:
            self.registers[reg] = value
        else:
            raise ValueError(f"Registrador {reg} não existe.")

    def get_register(self, reg):
        if reg in self.registers:
            return self.registers[reg]
        else:
            raise ValueError(f"Registrador {reg} não existe.")

    def set_flag(self, flag, value):
        if flag in self.flags:
            self.flags[flag] = 1 if value else 0
        else:
            raise ValueError(f"Flag {flag} não existe.")

    def get_flag(self, flag):
        if flag in self.flags:
            return self.flags[flag]
        else:
            raise ValueError(f"Flag {flag} não existe.")

    def reset(self):
        for reg in self.registers:
            self.registers[reg] = 0
        for flag in self.flags:
            self.flags[flag] = 0

# Teste básico
if __name__ == "__main__":
    regs = Registers()
    regs.set_register("R1", 10)
    print("R1:", regs.get_register("R1"))   
    regs.set_flag("ZF", True)
    print("Zero Flag:", regs.get_flag("ZF")) 
    print("Valor de R1:", regs.get_register("R1"))
