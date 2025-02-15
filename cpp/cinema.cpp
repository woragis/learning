#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

struct chair {
    int id;
    int x;
    int y;
    bool free;
};

int main() {
    int colCount = 4;
    int rowCount = 4;

    vector<chair> cinema = {
    };

    int size = 16;
    // Constructor of Cinema
    for (int i = 0; i < size; i++) {
        int row =  i / rowCount;
        int col =  i % colCount;
        cinema.push_back({i, row, col, true});
    }

    // Visualizer of the Cinema
    for (int i = 0; i < size; i++) {
        string free = (cinema[i].free) ? "yes" : "no";
        cout << "Id: " << cinema[i].id;
        cout << " - Free: " << free;
        cout << " - X: " << cinema[i].x;
        cout << " - Y: " << cinema[i].y;
        cout << endl;
    }

    return 0;
}