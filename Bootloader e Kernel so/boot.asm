[BITS 16]
[ORG 0x7C00]

start:
    mov ax, 0x07C0
    mov ds, ax
    mov es, ax

    mov si, msg_loading
    call print_string

    mov bx, 0x1000    
    mov dh, 2         
    call disk_load    

    jmp 0x1000        

disk_load:
    mov ah, 0x02      
    mov al, dh        
    mov ch, 0         
    mov cl, 2         
    mov dh, 0         
    mov dl, 0x80      
    int 0x13         
    ret

print_string:
    mov ah, 0x0E
.loop:
    lodsb
    test al, al
    jz .done
    int 0x10
    jmp .loop
.done:
    ret

msg_loading db 'Carregando o kernel...', 0

times 510-($-$$) db 0
dw 0xAA55
