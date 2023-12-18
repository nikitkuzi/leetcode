class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix[0])
        n = len(matrix)
        l_row = 0
        r_row = n-1
        f = False
        while l_row <= r_row:
            mid = (l_row+r_row) // 2
            # print(matrix[mid][0],matrix[mid][-1])
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                f = True
                l_row = mid
                break
            elif matrix[mid][0] > target:
                r_row = mid-1
                # continue
            elif matrix[mid][-1] < target:
                l_row = mid+1

        if not f: #and (l_row >= n or not(matrix[l_row][0] <= target <= matrix[l_row][-1])):
            # print(l_row,"here")
            return False
        l = 0
        r = m-1
        # print("l,r", l,r,l_row)
        while l<=r:
            mid = (l+r)//2
            if matrix[l_row][mid] == target:
                return True
            elif matrix[l_row][mid] < target:
                l = mid+1
            else:
                r = mid -1
        # print(l)
        # if l >= m:
        return False
        # return matrix[l_row][l] == target
        # return False
