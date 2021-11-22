#include <stdio.h>

char dst[32] = {94, 27, 10, 9, 35, 52, 101, 0, 8, 34, 52, 54, 44, 53, 38, 51, 79, 10, 37, 124, 41, 63, 11, 35, 53, 16, 3, 107, 13, 22, 80, 24};

int foo3(char s[]) {
    char arr3[33] = "!workHardAndYouWillBeSuccessful!";
    for (int i = 0; i < 32; i++) {
        s[i] ^= arr3[i];
    }
    for (int i = 0; i < 32; i++) {
        if (s[i] != dst[i]) {
            return 0;
        }
    }
    return 1;
}

int foo2(char s[]) {
    char arr2[33] = "keep_going_and_you_will_get_it~!";
    for (int i = 0; i < 32; i++) {
        s[i] ^= arr2[i];
    }
    return foo3(s);
}

int foo1(char s[]) {
    char arr1[33] = "really_really_ezzzzzzzzz_reverse";
    for (int i = 0; i < 32; i++) {
        s[i] ^= arr1[i];
    }
    return foo2(s);
}

int main() {
    char flag[33] = {0};
    printf("baigei? baigei!\n客官来个baigei的flag吧~\n");
    scanf("%32s", flag);
    if (foo1(flag) == 1) {
        printf("Yes! Gogogo!\n");
    } else {
        printf("Nooooooooo\n");
    }
    return 0;
}