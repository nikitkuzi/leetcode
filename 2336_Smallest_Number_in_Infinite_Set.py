class SmallestInfiniteSet:
    def __init__(self):
        self.cur = 1
        self.s = set()

    def popSmallest(self):
        if self.s:
            res = min(self.s)
            self.s.remove(res)
            return res
        else:
            self.cur += 1
            return self.cur - 1

    def addBack(self, num):
        if self.cur > num:
            self.s.add(num)


class SmallestInfiniteSet:
    def __init__(self):
        self.cur_integer = 1
        self.added = []
        self.present = set()

    def popSmallest(self) -> int:
        if self.added:
            answer = heapq.heappop(self.added)
            self.present.remove(answer)
        else:
            answer = self.cur_integer
            self.cur_integer += 1
        return answer

    def addBack(self, num: int) -> None:
        if num >= self.cur_integer or num in self.present:
            return
        heapq.heappush(self.added, num)
        self.present.add(num)