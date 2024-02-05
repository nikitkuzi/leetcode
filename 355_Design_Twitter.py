class Twitter:

    def __init__(self):
        self.tweetMap = defaultdict(list)
        self.follows = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        listOfFollowees = self.follows[userId]
        listOfFollowees.add(userId)

        maxHeap = []
        for user in listOfFollowees:
            if user in self.tweetMap:
                index = len(self.tweetMap[user]) - 1
                time, tweetId = self.tweetMap[user][index]
                heapq.heappush(maxHeap, [time, tweetId, user, index - 1])

        res = []
        while maxHeap and len(res) < 10:
            _, tweetId, user, next_index = heapq.heappop(maxHeap)
            res.append(tweetId)
            if next_index >= 0:
                time, tweetId = self.tweetMap[user][next_index]
                heapq.heappush(maxHeap, [time, tweetId, user, next_index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)