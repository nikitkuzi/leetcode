class ListNode:
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.least_recently_used = ListNode()
        self.last_added = ListNode()


    def get(self, key: int) -> int:
        if key in self.dict:
            return self.dict[key]
        return -1

    def put(self, key: int, value: int) -> None:
        print(self.least_recently_used)
        if key not in self.dict and len(self.dict) >= self.capacity :
            del dict[self.least_recently_used.val]
            self.least_recently_used = self.least_recently_used.next
        self.dict[key] = value
        new_node = ListNode(key)
        if not self.least_recently_used.next:
            self.least_recently_used = new_node

        else:
            temp = self.least_recently_used.next
            temp.next = new_node
            self.least_recently_used = new_node






# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
a = 5
b = a
print(a,b)
a = 4
print(a,b)