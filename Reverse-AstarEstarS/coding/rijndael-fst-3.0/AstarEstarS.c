#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "rijndael-api-fst.h"

typedef struct {
    int len;
    char text[64];
} textInstance;

void printBytes(textInstance *text) {
    for (int i = 0; i < text->len; i++) {
        printf("%02x", text->text[i]);
    }
    printf("\n");
    return;
}

BYTE unhex_sub(char x) {
    if (x >= '0' && x <= '9') {
        return x - '0';
    } else if (x >= 'a' && x <= 'f') {
        return x - 'a' + 10;
    } else if (x >= 'A' && x <= 'F') {
        return x - 'A' + 10;
    } else {
        return 0xff;
    }
}

int unhex(char *hex, BYTE *bin, int hexLen) {
    for (int i = 0; i < hexLen; i += 2) {
        bin[i/2] = 0;
        for (int j = 0; j < 2; j++) {
            BYTE tmp = unhex_sub(hex[i+j]);
            if (tmp == 0xff) {
                return FALSE;
            }
            bin[i/2] <<= 4;
            bin[i/2] |= tmp;
        }
    }
    return TRUE;
}

void printMenu() {
    printf("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n");
    printf("      Welcome to HSCTF ~ !\n");
    printf("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n");
    printf("\n");
    return;
}

size_t getSomething(char key[]) {
    char secret[6] = "Tover";
    int arr[16] = {32, 7, 71, 22, 45, 61, 28, 41, 4, 45, 63, 10, 15, 58, 43, 27};
    for (int i = 0; i < 16; i++) {
        key[i] = arr[i] ^ secret[i%5];
    }
    return strlen(key);
}

int check(char res[48]) {
    char dst[48] = {211, 93, 222, 166, 164, 157, 25, 242, 217, 199, 50, 240, 62, 64, 120, 233, 16, 140, 140, 180, 83, 119, 49, 193, 191, 63, 108, 93, 127, 129, 140, 205, 85, 147, 50, 53, 34, 172, 61, 55, 115, 44, 74, 69, 210, 197, 108, 175};

    if (!memcmp(dst, res, 48)) return TRUE;
    else return FALSE;
}

int foo(keyInstance *key, cipherInstance *cipher, textInstance *input, textInstance *output) {
    char _keyMaterial[MAX_KEY_SIZE+1] = {0};
    size_t  _keyLen = getSomething(_keyMaterial) * 8;
    int _direction = DIR_ENCRYPT, _mode = MODE_ECB;
    char * _IV = NULL;

    makeKey(key, _direction, _keyLen, _keyMaterial);
    cipherInit(cipher, _mode, _IV);

    memset(input->text, 0, 64);
    printf("\nGive me a flag?\n");
    if (!scanf("%63s", input->text)) {
        return FALSE;
    }
    input->len = strlen(input->text);
    output->len = ((input->len-1)/16+1)*16;
    if (input->len != 38) {
        return FALSE;
    }
    if (padEncrypt(cipher, key, (BYTE *)input->text, input->len, (BYTE *)output->text) <= 0) {
        return FALSE;
    }

    return check(output->text);
}

int main() {
    keyInstance keyInst;
    cipherInstance cipherInst;
    textInstance inputInst, outputInst;
    printMenu();
    if (foo(&keyInst, &cipherInst, &inputInst, &outputInst) != TRUE) {
        printf("Soooooooorry~ \n");
    } else {
        printf("Gogogo! You get it!\n");
    }
    return 0;
}