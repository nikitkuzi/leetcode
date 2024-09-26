class MyCalendar:

    def __init__(self):
        self.books = []

    def book(self, start: int, end: int) -> bool:
        pos_left = bisect_left(self.books, [start,end])
        # print(pos_left)
        l = -inf
        r = inf
        if pos_left > 0:
            l = self.books[pos_left-1][1]
        if pos_left < (len(self.books)):
            r = self.books[pos_left][0]
        if start < l or end > r:
            return False
        self.books.insert(pos_left, [start, end])
        # print(self.books)
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)