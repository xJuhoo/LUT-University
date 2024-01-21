CREATE VIEW Tweets_and_tags AS
SELECT 
    (SELECT Username FROM User WHERE User.UserID = Tweet.UserID) AS User,
    Tweet.Content AS Tweet,
    GROUP_CONCAT(Hashtag.Content, "") AS Hashtag
FROM 
    Tweet
    INNER JOIN HashtagsInContent ON HashtagsInContent.TweetID = Tweet.TweetID
    INNER JOIN Hashtag ON HashtagsInContent.HashtagID = Hashtag.HashtagID
GROUP BY
    User;
