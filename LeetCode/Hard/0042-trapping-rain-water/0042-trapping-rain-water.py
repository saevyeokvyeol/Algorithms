class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        max_left, max_right = height[0], height[-1]
        left, right = 0, len(height) - 1

        while left < right:
            if max_left < max_right:
                left += 1
                if max_left < height[left]:
                    max_left = height[left]
                else:
                    water += max_left - height[left]
            else:
                right -= 1
                if max_right < height[right]:
                    max_right = height[right]
                else:
                    water += max_right - height[right]
        return water
