class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def calculateAreas(y):
            area_above = 0
            area_below = 0
            for xi, yi, li in squares:
                if y <= yi:
                    area_above += li * li
                elif y >= yi + li:
                    area_below += li * li
                else:
                    above_height = yi + li - y
                    below_height = y - yi
                    area_above += above_height * li
                    area_below += below_height * li
            return area_above, area_below

        # Determine the search space
        min_y = float('inf')
        max_y = float('-inf')
        for xi, yi, li in squares:
            min_y = min(min_y, yi)
            max_y = max(max_y, yi + li)

        # Binary search
        precision = 1e-5
        while max_y - min_y > precision:
            mid_y = (min_y + max_y) / 2
            area_above, area_below = calculateAreas(mid_y)
            if area_above > area_below:
                min_y = mid_y
            else:
                max_y = mid_y

        return (min_y + max_y) / 2