#include <stdio.h>

char map[285] = {2, 1, 1, 0, 1, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 2, 0, 1, 0, 0, 1, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 3, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
char path[51] = {0};
int start[6][2] = {{0, 0}, {2, 1}, {1, 0}, {1, 6}, {1, 2}, {-1, -1}};
int n = 3, m = 0;
int x = 0, y = 0;

int move(char op) {
    switch (op) {
        case 'h':
            y--;
            break;
        case 'j':
            x++;
            break;
        case 'k':
            x--;
            break;
        case 'l':
            y++;
            break;
        default:
            return 0;
    }
    if (map[m + x*n + y] == 0 || x >= n || y >= n || x < 0 || y < 0) return 0;
    if (map[m + x*n + y] == 3) {
        m += n*n;
        x = start[n/2][0];
        y = start[n/2][1];
        n += 2;
    }
    return 1;
}

int check() {
    for (int i = 0; i < 51; i++) {
        if(path[i] == 0) return 0;
        if(move(path[i]) == 0) return 0;
    }
    if (x == -1 && y == -1) return 1;
    return 0;
}

int main() {
    printf("Give me the shortest path and I will give you flag. (Only read the first 51 chars!)\n");
    scanf("%51s", path);
    if (check() == 1) {
        printf("R1ght! Your flag is flag{md5(your input, 51 chars)}!\n");
    } else {
        printf("Wr0ng! Maybe try again?\n");
    }
    return 0;
}