import logging

def setup_logger(name='simulador', level=logging.DEBUG, log_file='simulador.log'):
    """
    Configura e retorna um logger para o simulador.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    if not logger.handlers:
        # Handler para exibir no console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
        # Handler para gravar em arquivo
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger

# Exemplo de uso:
if __name__ == "__main__":
    logger = setup_logger()
    logger.debug("Logger configurado com sucesso!")
