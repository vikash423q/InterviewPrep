#   https://leetcode.com/problems/design-twitter/


from typing import List
import heapq


class Twitter:

    def __init__(self):
        self.t = 0
        self.users = {}
        self.feeds = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feeds.setdefault(userId, [])
        self.feeds[userId].append((self.t, tweetId))
        self.t -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = list(self.feeds.get(userId, []))
        for followee in self.users.get(userId, []):
            tweets += self.feeds.get(followee, [])

        heapq.heapify(tweets)
        res = []
        i = 0
        while tweets and i < 10:
            res.append(heapq.heappop(tweets)[1])
            i += 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users.setdefault(followerId, set())
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            return
        self.users[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
