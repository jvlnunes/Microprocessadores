class Controls:
    def __init__(self):
        self.paused = False

    def pause(self):
        """
        Pausa a simulação.
        """
        self.paused = True
        print("Simulação pausada.")

    def resume(self):
        """
        Retoma a simulação.
        """
        self.paused = False
        print("Simulação retomada.")

    def wait_for_step(self):
        """
        Aguarda o usuário pressionar Enter para avançar um passo na simulação.
        """
        input("Pressione Enter para executar o próximo passo...")

# Exemplo de uso:
if __name__ == "__main__":
    controls = Controls()
    print("Simulação iniciada.")
    controls.wait_for_step()
    print("Avançando um passo...")
    controls.pause()
