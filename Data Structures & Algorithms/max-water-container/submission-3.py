class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0
        while left < right:
            height = min(heights[left], heights[right])
            length = right - left
            area = height * length
            if area > max_area:
                max_area = area
            if min(heights[left+1], heights[right]) > height or heights[left] < heights[right]:
                left += 1
            elif min(heights[left], heights[right-1]) > height or heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
                right -= 1
        return max_area
        
        # middle = len(heights)//2
        # adjusted = [height - i for i, height in enumerate(heights) if i < middle]
        # if len(heights) % 2 == 1:
        #     adjusted += [heights[middle] - middle]
        # adjusted += [heights[len(heights)-1-i] - i for i in range(middle-1, -1, -1)]
        # first = second = 0
        # print(adjusted)
        # for i, num in enumerate(adjusted):
        #     if num > adjusted[first]:
        #         first = i
        # print(first)
        # for i, num in enumerate(adjusted):
        #     if num >= adjusted[second] and i != first:
        #         second = i
        # print(second)
        # return min(heights[first], heights[second])*abs(first-second)

        

        