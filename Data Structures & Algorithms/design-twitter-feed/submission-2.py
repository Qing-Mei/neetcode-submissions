from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.posts = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.time, tweetId))
        
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.following[userId] | {userId}
        min_heap = []

        for uid in users:
            if self.posts[uid]:
                i = len(self.posts[uid]) - 1
                time, tweetId = self.posts[uid][i]
                heapq.heappush(min_heap, (time, tweetId, uid, i))
                
                if len(min_heap) > 10:
                    heapq.heappop(min_heap)
        
        max_heap = [(-time, tweetId, uid, i) for time, tweetId, uid, i in min_heap]
        heapq.heapify(max_heap)

        feed = []
        while max_heap and len(feed) < 10:
            neg_time, tweetId, uid, i = heapq.heappop(max_heap)
            feed.append(tweetId)

            if i > 0:
                time, tweetId = self.posts[uid][i - 1]
                heapq.heappush(max_heap, (-time, tweetId, uid, i - 1))
        
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            return
        self.following[followerId].discard(followeeId)
