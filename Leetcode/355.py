import heapq
from collections import defaultdict
from typing import List


class Twitter:
    NEWSFEED_SIZE: int = 10

    def __init__(self):
        self.tweets: defaultdict[int, list[tuple[int, int]]] = defaultdict(list)
        self.follows: defaultdict[int, set[int]] = defaultdict(set)
        self.indexer = iter(range(10**9))

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.tweets[userId], (-next(self.indexer), tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap: list[tuple[int, int, int]] = []

        for followee_id in self.follows[userId].union({userId}):
            if self.tweets[followee_id]:
                _top = heapq.heappop(self.tweets[followee_id])
                heapq.heappush(heap, (_top[0], _top[1], followee_id))

        top_tweets: list[tuple[int, int, int]] = []

        while heap and len(top_tweets) < self.NEWSFEED_SIZE:

            idx, top_tweet, tweeter_id = heapq.heappop(heap)
            top_tweets.append((idx, top_tweet, tweeter_id))
            if self.tweets[tweeter_id]:
                _top = heapq.heappop(self.tweets[tweeter_id])
                heapq.heappush(heap, (_top[0], _top[1], tweeter_id))

        for idx, tweet_id, tweeter_id in top_tweets + heap:
            heapq.heappush(self.tweets[tweeter_id], (idx, tweet_id))

        return [i[1] for i in sorted(top_tweets, key=lambda x: x[0])]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
