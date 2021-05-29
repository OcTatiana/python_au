# Design

+ [Design Twitter](#design-twitter)

[comment]: <> (Stop)

## Design Twitter

https://leetcode.com/problems/design-twitter/

```python
def __init__(self):
    self.followers = collections.defaultdict(list)
    self.following = collections.defaultdict(list)
    self.tweets = collections.defaultdict(list)
    self.time = 0
def postTweet(self, userId: int, tweetId: int) -> None:
    self.time += 1
    self.tweets[userId].append((self.time, tweetId))
def getNewsFeed(self, userId: int) -> List[int]:
    heap = []
    if userId in self.tweets: 
        heap.extend(self.tweets[userId])
    for id in self.following.get(userId, []):
        if id != userId: 
            heap.extend(self.tweets.get(id, []))
    heap = sorted(heap, key=lambda tweet: tweet[0], reverse = True)
    res = []
    while heap and len(res) < 10: 
        item = heap.pop(0)
        res.append(item[1])
    return res 
def follow(self, followerId: int, followeeId: int) -> None:
    if followeeId not in self.following[followerId]:
        self.following[followerId].append(followeeId)
def unfollow(self, followerId: int, followeeId: int) -> None:
    if followerId in self.following: 
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
```