[BITS 32]
[ORG 0x1000]

start:
    cli                     
    lgdt [gdt_descriptor]    

    mov eax, cr0            
    or eax, 1
    mov cr0, eax

    jmp CODE_SEG:init32      

[BITS 32]
init32:
    mov ax, DATA_SEG    
    mov ds, ax          
    mov ss, ax
    mov esp, 0x90000    

    call init_pic           
    call enable_keyboard    

    mov esi, msg_ready      
    call print_string       

main_loop:
    hlt                     
    jmp main_loop

; --------- Função de Leitura de Disco ---------
disk_read:
    pusha

    mov ah, 0x02        
    mov al, dh          
    mov ch, 0          
    mov cl, dl          
    mov dh, 0          
    mov dl, 0x80       
    int 0x13           

    popa
    ret

; --------- Carregar Arquivo ---------
load_file:
    pusha

    mov si, buffer
    mov di, file_table
.loop:
    mov cx, 8
    repe cmpsb
    jz .found
    add di, 12
    cmp di, file_table + 64
    jl .loop

    mov esi, msg_file_not_found
    call print_string
    popa
    ret

.found:
    mov dl, [di]
    mov dh, [di+2]
    mov bx, 0x9000
    call disk_read

    mov esi, msg_file_loaded
    call print_string
    popa
    ret

msg_ready db 'Kernel pronto! Digite um comando: ', 0
msg_file_not_found db 'Arquivo nao encontrado.', 0
msg_file_loaded db 'Arquivo carregado com sucesso.', 0

buffer times 256 db 0

file_table:
    db 'editor  ', 4, 1, 0, 0, 0, 0, 0, 0  ; Arquivo "editor" no setor 4
    times 64-12 db 0

; --------- GDT ---------
gdt:
    dq 0x0000000000000000 
    dq 0x00CF9A000000FFFF 
    dq 0x00CF92000000FFFF 

gdt_descriptor:
    dw gdt_descriptor - gdt - 1
    dd gdt

CODE_SEG equ 0x08  
DATA_SEG equ 0x10  
