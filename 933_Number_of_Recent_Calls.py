class RecentCounter:
    def __init__(self):
        self.arr = []

    def ping(self, t: int) -> int:
        self.arr.append(t)
        start = t - 3000
        if (t <= 0):
            return len(self.arr)

        # find t which is >= start in arr
        def binSearch(start, arr):
            i = 0
            j = len(arr)
            while (i <= j):
                mid = (i + j) // 2
                if (arr[mid] > start):
                    j = mid - 1
                elif (arr[mid] < start):
                    i = mid + 1
                else:
                    return mid
            return i

        indx = binSearch(start, self.arr)
        return len(self.arr) - indx