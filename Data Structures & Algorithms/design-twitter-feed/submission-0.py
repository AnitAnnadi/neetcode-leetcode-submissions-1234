class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.posts = defaultdict(list)
        self.count = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        post = (self.count, tweetId)
        self.posts[userId].append(post)
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res, q = [], []

        for user in self.following[userId] | {userId}:
            for post in self.posts[user]:
                heapq.heappush(q, post)

                if len(q) > 10:
                    heapq.heappop(q)

        while q:
            _, tweetId = heapq.heappop(q)
            res.append(tweetId)
        
        res.reverse()
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
