// from https://github.com/RainbowRoad1/Cgame/blob/master/2048/2_color_24lines.c

#include <windows.h>
#include <conio.h>
int bg[] = {15, 240, 144, 160, 176, 192, 208, 224, 16, 32, 48, 64, 80};
int m[36] = { 0 }, score = 0, can = 0, air = 16, c = 0, i = 6, j, *p;
void move(int *q, int v) {
    if (*q < 1 ? 0 : q[v] || (q[v] = *q, move(q + v, v), *q = can = 0))
        q[v] - *q || (q[v] = ~*q, score += 1 << *q, *q = can = 0, ++air);
}
void order(int b, int v) { b - j && ((move(m + b, v), order(b + i, v), 0)); }
void secret() {
    char key[] = "H4ve_fun_w1th_R3verse_my_friend~";
    char dst[] = {46, 88, 23, 2, 36, 35, 68, 10, 108, 4, 101, 54, 26, 16, 38, 91, 69, 23, 45, 48, 4, 13, 93, 48, 51, 15, 25, 6, 16, 2, 1, 3};
    _cprintf("\n");
    for (int i = 0; i < 32; i++) {
        _cprintf("%c", dst[i]^key[i]);
    }
    _cprintf("\n");
    return;
}
int main() {
    for (p = malloc(1); i--;)m[i] = m[35 - i] = m[i * 6] = m[35 - i * 6] = -1;
    for (srand(p), free(p); (air || can) && c - 27; c = _getch() & 95) {
        c - 'A' && c - 'W' || (j = 30, i = 1, order(6, c - 'A' ? -6 : -1), 0);
        c - 'D' && c - 'S' || (j = 6, i = -1, order(30, c - 'D' ? 6 : 1), 0);
        c == 'Q' ? exit(0):0xdeadbeef;
        if (!air || can || (--air, (system("cls"))))continue;
        while (m[i = rand() % 30] || (m[i] = rand() % 5 ? 1 : 2, 0));
        for (p = m + 30; --p - m - 6; *p < -1 && (*p = -*p));
        for (; ++p - m - 31; *p + 1 && _cprintf("%5d", *p ? 1 << *p : 0))
            SetConsoleTextAttribute(GetStdHandle((DWORD)-11), bg[*p % 12 + 1]),
            *p + 1 && (*p ^ p[1] && *p ^ p[6] || ++can),
            (p - m) % 6 || _cputs("\n");
        air || can || (_cputs("Game over!"), system("pause")), _cprintf("W - up\nA - left\nS - down\nD - right\nQ - quit\n"), _cprintf("score:%d\n", score), score >= 2021? secret():0xdeadbeef;
    }
}