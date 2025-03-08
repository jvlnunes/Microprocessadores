# Simulador de Compilador e Processador em Assembly

Este projeto implementa um simulador de um microprocessador e seu compilador em Assembly. Ele integra as etapas de lexação, parsing, análise semântica e montagem (assembler) para converter código Assembly em código de máquina, que é então executado por um processador simulado. O sistema é modular e inclui também uma simulação de memória, dispositivos de entrada/saída, unidade de controle, logging e uma interface de controle e exibição do estado da simulação.

## Visão Geral

O simulador foi desenvolvido para atender aos seguintes requisitos:
- **Compilador:** Implementa um lexer, parser, analisador semântico, e um assembler (ou gerador de código) para converter Assembly em código de máquina.
- **Processador:** Simula a execução do código de máquina através de uma CPU com registradores, memória, e dispositivos de I/O.
- **Simulador:** Um pacote que integra o compilador e o processador, fornecendo ferramentas de logging, display do estado e controles (pause, resume, passo a passo).
- **Modularidade:** Cada parte do sistema (compilador, processador, simulador) está organizada em módulos, facilitando a expansão e a manutenção do projeto.

## Estrutura do Projeto


## Requisitos

- Python 3.6 ou superior
- Bibliotecas padrão do Python (não há dependências externas obrigatórias, mas você pode expandir com GUI ou outros módulos conforme necessário)

## Instalação e Execução

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/seu-projeto.git
   cd seu-projeto
