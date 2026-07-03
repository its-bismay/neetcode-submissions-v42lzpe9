class Twitter:

    def __init__(self):
        self.time = 0
        self.user_db = defaultdict(set)
        self.tweet_db = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.tweet_db[userId].append([self.time,tweetId])

        
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        posts = [] #it will be our heap to get most recent posts

        self.user_db[userId].add(userId)

        for user in self.user_db[userId]:
            if user in self.tweet_db:
                idx = len(self.tweet_db[user]) - 1
                time, tweet_id = self.tweet_db[user][idx]
                heapq.heappush(posts, [time, tweet_id, user, idx - 1])
        
        while posts and len(res) < 10:
            time, tweet_id, user, idx = heapq.heappop(posts)
            res.append(tweet_id)

            if idx >= 0:
                time, tweet_id = self.tweet_db[user][idx]
                heapq.heappush(posts, [time, tweet_id, user, idx - 1])
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_db[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_db[followerId]:
            self.user_db[followerId].remove(followeeId)
        
