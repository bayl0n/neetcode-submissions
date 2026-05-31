class Solution:
    def trap(self, height: List[int]) -> int:
        """
        elevation:
            it is the min height for i and j

        so for each elevation, we want to scan between i and j

        we know water can be trapped if for a given height, it is less than the elevation
        between i and j

        in order to track elevations, we want to ensure that i and j are non-decreasing

        - we want to track the max elevation between and i j
        - when a new max elevation is found, we want to count between i and j for heights
            that are less than our current elevation
        - when deciding to move i or j, since we want to find a new max elevation, we want to
            move whichever side is smallest
        """

        max_elevation = 0
        left = 0
        water = 0
        right = len(height) - 1

        while left < right:
            current_elevation = min(height[left], height[right])
            max_elevation = max(max_elevation, current_elevation)

            if height[left] > height[right]:
                scan = right-1
                while height[scan] < max_elevation and scan > left:
                    water += (max_elevation - height[scan])
                    scan -= 1

                right = scan
            else:
                scan = left+1
                while height[scan] < max_elevation and scan < right:
                    water += (max_elevation - height[scan])
                    scan += 1

                left = scan

        return water