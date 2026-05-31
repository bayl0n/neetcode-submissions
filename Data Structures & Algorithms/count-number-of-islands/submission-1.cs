public class Solution {
    public int NumIslands(char[][] grid) {
        var seen = new HashSet<(int, int)>();
        var islandCount = 0;

        var directions = new (int, int)[] {
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        };

        bool isWater(int x, int y) {
            return x < 0 || x > grid.Length-1 || y < 0 || y > grid[0].Length-1 || grid[x][y] == '0';
        }

        void dfs(int x, int y) {
            if (isWater(x, y) || seen.Contains((x,y))) return;

            seen.Add((x,y));

            foreach ((var dx, var dy) in directions) {
                dfs(x+dx, y+dy);
            }
        }

        for (var i = 0; i < grid.Length; i++) {
            for (var j = 0; j < grid[0].Length; j++) {
                if (!seen.Contains((i,j)) && grid[i][j] == '1') {
                    islandCount++;
                    dfs(i,j);
                }
            }
        }

        return islandCount;
    }
}
