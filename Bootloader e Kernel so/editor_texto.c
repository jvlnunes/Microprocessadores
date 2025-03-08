#define VIDEO_MEMORY 0xB8000
#define SCREEN_WIDTH 80
#define MAX_TEXT_LENGTH 1024

char text_buffer[MAX_TEXT_LENGTH];
int cursor_pos = 0;

void clear_screen() {
    char *video = (char*) VIDEO_MEMORY;
    for (int i = 0; i < SCREEN_WIDTH * 25 * 2; i += 2) {
        video[i] = ' ';
        video[i+1] = 0x07; 
    }
}

void print_char(char c) {
    char *video = (char*) VIDEO_MEMORY;
    if (c == '\n') {
        cursor_pos += SCREEN_WIDTH - (cursor_pos % SCREEN_WIDTH);
    } else {
        video[cursor_pos * 2] = c;
        video[cursor_pos * 2 + 1] = 0x07;
        cursor_pos++;
    }
}

void print_text() {
    clear_screen();
    for (int i = 0; i < cursor_pos; i++) {
        print_char(text_buffer[i]);
    }
}

char get_key() {
    char c;
    __asm__ volatile (
        "mov $0, %%ah\n"
        "int $0x16\n"
        "movb %%al, %0\n"
        : "=r"(c)
        :
        : "ax"
    );
    return c;
}

void editor() {
    clear_screen();
    while (1) {
        char c = get_key();
        if (c == 27) break; 
        if (cursor_pos < MAX_TEXT_LENGTH - 1) {
            text_buffer[cursor_pos] = c;
            cursor_pos++;
            print_text();
        }
    }
}

void main() {
    editor();
}
