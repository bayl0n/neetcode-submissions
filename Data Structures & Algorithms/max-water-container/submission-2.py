class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        i,j

        height = min(i,j)
        width = abs(j - i)

        area = height * width

        We want to find i and j such that it maximises area

        [8, 7, 2, 9, 20]
         i           j

         when deciding to move i and j, we want to move the pointer with the smallest height to maximise height
         we also want to keep track of the maximum area as we are moving our pointers through the list
        """

        maxarea = 0
        i = 0
        j = len(heights) - 1

        while i < j:
            height = min(heights[i], heights[j])
            width = j - i
            area = height * width
            
            maxarea = max(maxarea, area)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1 

            print(heights[i], heights[j])

        return maxarea