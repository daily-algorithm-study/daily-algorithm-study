#include <string>
#include <vector>
#include <queue>
#include <set>
#include <iostream>
using namespace std;

bool checkRange(int x, int y, int X1, int X2, int Y1, int Y2) {
    if ((x == X1 || x == X2) && (y >= Y1 && y <= Y2)) {
        return true;
    }
    if ((y == Y1 || y == Y2) && (x >= X1 && x <= X2)) {
        return true;
    }
    return false;
}

int solution(vector<vector<int>> rectangle, int characterX, int characterY, int itemX, int itemY) {
    int answer = 0;

    queue<pair<int, int>> q;
    q.push(make_pair(characterX, characterY));

    bool visited[60][60] = { false };
    visited[characterX][characterY] = true;

    int count = -1;
    pair<int, int> rotates[] = { make_pair(0,1),make_pair(1,0),make_pair(-1,0),make_pair(0,-1) };
    while (!q.empty()) {
        count += 1;
        int length = q.size();
        for (int k = 0; k < length; k++) {
            pair<int, int> current = q.front();
            if (current.first == itemX && current.second == itemY) return count;
            q.pop();
            for (int i = 0; i < size(rotates); i++) {
                float moveLess = 0.5;
                pair<int, int> rotate = rotates[i];
                int newX = current.first + rotate.first;
                int newY = current.second + rotate.second;

                if (visited[newX][newY] || newX < 0 || newY < 0) continue;

                bool innerFlag = false;
                bool borderFlag = false;

                float xLess = rotate.first * moveLess;
                float yLess = rotate.second * moveLess;

                for (vector<int> rec : rectangle) {
                    int leftDownX = rec[0];
                    int leftDownY = rec[1];
                    int rightUpX = rec[2];
                    int rightUpY = rec[3];
                    if (newX - xLess > leftDownX && newX - xLess <rightUpX && newY - yLess > leftDownY && newY - yLess < rightUpY) {
                        innerFlag = true;
                        break;
                    }
                    if (checkRange(current.first, current.second, leftDownX, rightUpX, leftDownY, rightUpY)
                        && checkRange(newX, newY, leftDownX, rightUpX, leftDownY, rightUpY)) {
                        borderFlag = true;
                    }
                }

                if (!innerFlag && borderFlag && !visited[newX][newY]) {
                    q.push(make_pair(newX, newY));
                    visited[newX][newY] = true;
                }

            }

        }

    }
    return answer;
}