public class Solution {
    public int MaxAreaOfIsland(int[][] grid) {
        var seen = new HashSet<(int, int)>();
        var maxArea = 0;

        var directions = new (int, int)[] {
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        };

        bool IsInvalidNode(int x, int y) {
            return x < 0 || x > grid.Length - 1 || y < 0 || y > grid[0].Length - 1;
        }

        int dfs(int x, int y) {
            if (IsInvalidNode(x, y) || grid[x][y] == 0 || seen.Contains((x,y))) return 0;

            var count = 1;
            seen.Add((x,y));

            foreach ((var dx, var dy) in directions) {
                count += dfs(x + dx, y + dy);
            }

            maxArea = Math.Max(maxArea, count);

            return count;
        }

        for (int i = 0; i < grid.Length; i++) {
            for (int j = 0; j < grid[0].Length; j++) {
                if (!seen.Contains((i,j))) {
                    dfs(i, j);
                }
            }
        }

        return maxArea;
    }
}
