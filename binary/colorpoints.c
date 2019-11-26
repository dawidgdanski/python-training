#include <stdio.h>

struct Vector {
    float x;
    float y;
    float z;
};

struct Color {
    unsigned short int red;
    unsigned short int green;
    unsigned short int blue;
};

struct Vertex {
    struct Vector position;
    struct Color color;
};

int main(int argc, char** argv) {
    struct Vertex vertices[] = {
        {
            .position = {243.34, 2394.43, 324.343},
            .color = {232, 943, 1}
        },
        {
            .position = {244.34, 234.43, 65.343},
            .color = {233, 944, 2}
        },
        {
            .position = {43.34, 987.43, 876.343},
            .color = {234, 945, 3}
        },
        {
            .position = {1230.2, 1230.123, 549.43},
            .color = {235, 946, 4}
        },
    };

    FILE* file = fopen("colors.bin", "wb");

    if(file == NULL) {
        return -1;
    }

    fwrite(vertices, sizeof(struct Vertex), 4, file);
    fclose(file);
    
    return 0;
}