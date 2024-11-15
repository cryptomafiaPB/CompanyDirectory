#include <iostream> 
#include <vector> 
#include <set> 
#include <algorithm> 
 
using namespace std; 
 
// Directions: Up, Down, Left, Right 
const int dx[] = {-1, 1, 0, 0};  // Row offsets for up/down/left/right 
const int dy[] = {0, 0, -1, 1};  // Column offsets for up/down/left/right 
 
// Function to find the next direction based on mirror type and current direction 
int getNextDirection(char mirror, int currentDirection) { 
    if (mirror == '/') { 
        if (currentDirection == 0) return 3;  // Up -> Right 
        if (currentDirection == 1) return 2;  // Down -> Left 
        if (currentDirection == 2) return 1;  // Left -> Down 
        if (currentDirection == 3) return 0;  // Right -> Up 
    } else if (mirror == '\\') { 
        if (currentDirection == 0) return 2;  // Up -> Left 
        if (currentDirection == 1) return 3;  // Down -> Right 
        if (currentDirection == 2) return 0;  // Left -> Up 
        if (currentDirection == 3) return 1;  // Right -> Down 
    } 
    return currentDirection;  // For '0' (empty space), continue in the same direction 
} 
 
// Function to find the cycle length starting from a given cell and direction 
int findLoop(int startX, int startY, int startDirection, vector<vector<char>>& grid, int M, int N) { 
    set<pair<pair<int, int>, int>> visited;  // (x, y, direction) to track visited cells with directions 
    vector<pair<int, int>> path;  // To track the path for cycle length calculation 
    int x = startX, y = startY, direction = startDirection; 
     
    while (x >= 0 && x < M && y >= 0 && y < N) { 
        if (visited.count({{x, y}, direction})) { 
            // Loop detected, calculate the cycle length 
            auto loopStart = find(path.begin(), path.end(), make_pair(x, y)); 
            return distance(loopStart, path.end());  // Length of the loop 
        } 
        visited.insert({{x, y}, direction}); 
        path.push_back({x, y}); 
         
        // Move to the next cell based on the current direction 
        direction = getNextDirection(grid[x][y], direction); 
        x += dx[direction]; 
        y += dy[direction]; 
    } 
     
    return 0;  // No loop found 
} 
 
int main() { 
    int M, N; 
    cin >> M >> N; 
 
    vector<vector<char>> grid(M, vector<char>(N)); 
     
    // Input the grid structure 
    for (int i = 0; i < M; i++) { 
        for (int j = 0; j < N; j++) { 
            cin >> grid[i][j]; 
        } 
    } 
 
    int maxLoop = 0; 
 
    // Try starting from each cell 
    for (int i = 0; i < M; i++) { 
        for (int j = 0; j < N; j++) { 
            if (grid[i][j] != '0') {  // Only start from a mirror cell 
                for (int dir = 0; dir < 4; dir++) {  // Try all 4 possible directions (Up, Down, Left, Right) 
                    maxLoop = max(maxLoop, findLoop(i, j, dir, grid, M, N)); 
                } 
            } 
        } 
    } 
 
    cout << maxLoop << endl;  // Output the maximum loop length 
 
    return 0; 
}                                                                                                                                          MIRROR GAZE CODE