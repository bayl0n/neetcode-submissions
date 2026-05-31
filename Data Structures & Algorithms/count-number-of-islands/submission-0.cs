public class Solution {
    public int NumIslands(char[][] grid) {
        var directions = new (int dx, int dy)[] {
            (0, 1),
            (0, -1),
            (-1, 0),
            (1, 0)
        };

        var seen = new HashSet<(int, int)>();

        var count = 0;

        bool isInvalidNode((int x, int y) node) {
            return node.x < 0 || node.x > grid.Length - 1 || node.y < 0 || node.y > grid[0].Length - 1 || grid[node.x][node.y] == '0';
        }

        void dfs((int x, int y) node) {
            if (isInvalidNode((node.x, node.y)) || seen.Contains((node.x, node.y))) return;

            seen.Add((node.x, node.y));
            foreach ((var dx, var dy) in directions) {
                dfs((node.x+dx, node.y+dy));
            }
        }

        for (int i = 0; i < grid.Length; i++) {
            for (int j = 0; j < grid[0].Length; j++) {
                if (grid[i][j] == '1' && !seen.Contains((i, j))) {
                    count++;
                    dfs((i,j));
                }
            }
        }

        return count;
    }
}
