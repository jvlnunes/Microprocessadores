# Sistema Operacional Simples

## 📌 Visão Geral
Este projeto consiste na criação de um sistema operacional simples, incluindo um **bootloader**, um **nano kernel** e um **editor de texto básico** como aplicação de teste. O sistema suporta:

✅ Bootloader próprio
✅ Sistema de arquivos com alocação contínua
✅ Kernel em Assembly e C
✅ Editor de texto básico
✅ Capacidade de reiniciar o computador e carregar arquivos do disco

---

## 🛠️ Estrutura do Projeto
O projeto contém os seguintes arquivos:

```
/
│── boot.asm       # Código do bootloader
│── kernel.asm     # Código do kernel
│── editor.c       # Código do editor de texto
│── editor.asm     # Alternativa do editor em Assembly
│── disk.img       # Imagem do disco com o SO
│── README.md      # Documentação do projeto
```

---

## 🚀 Compilação e Geração do Disco
Para compilar e gerar a imagem do disco, siga os passos abaixo.

### **1. Compilar o Bootloader**
```sh
nasm -f bin boot.asm -o boot.bin
```

### **2. Compilar o Kernel**
```sh
nasm -f bin kernel.asm -o kernel.bin
```

### **3. Compilar o Editor de Texto**
Caso use a versão em C:
```sh
i686-elf-gcc -ffreestanding -m32 -nostdlib -o editor.elf editor.c
objcopy -O binary editor.elf editor.bin
```
Se usar a versão em Assembly:
```sh
nasm -f bin editor.asm -o editor.bin
```

### **4. Criar a Imagem do Disco**
```sh
dd if=/dev/zero of=disk.img bs=512 count=2880
dd if=boot.bin of=disk.img bs=512 seek=0 conv=notrunc
dd if=kernel.bin of=disk.img bs=512 seek=1 conv=notrunc
dd if=editor.bin of=disk.img bs=512 seek=4 conv=notrunc
```

---

## 💻 Execução no QEMU
Após gerar `disk.img`, podemos rodá-lo no **QEMU**:
```sh
qemu-system-x86_64 -drive format=raw,file=disk.img
```

No terminal do sistema, digite:
```
editor
```
para abrir o editor de texto!

---

## 📅 Próximos Passos
🔹 Melhorar o sistema de arquivos para suportar múltiplos arquivos
🔹 Adicionar funcionalidade de salvar e carregar no editor de texto
🔹 Criar um shell básico para comandos no kernel

---

## 📜 Licença
Este projeto é de código aberto e pode ser usado para aprendizado e experimentação!

---

**Contribuições são bem-vindas! 🚀**

