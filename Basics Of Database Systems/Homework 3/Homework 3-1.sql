CREATE TABLE Comments (
    CommentID INTEGER NOT NULL,
    UserID INTEGER NOT NULL,
    TweetID INTEGER,
    FK_CommentID INTEGER,
    Content VARCHAR(200),
    PRIMARY KEY(CommentID),
    FOREIGN KEY(UserID) REFERENCES User(UserID),
    FOREIGN KEY(TweetID) REFERENCES Tweet(TweetID),
    FOREIGN KEY(CommentID) REFERENCES Comments(CommentID)
);

CREATE TABLE Likes (
    LikeID INTEGER NOT NULL,
    UserID INTEGER NOT NULL,
    TweetID INTEGER,
    CommentID INTEGER,
    PRIMARY KEY(LikeID),
    FOREIGN KEY(UserID) REFERENCES User(UserID),
    FOREIGN KEY(TweetID) REFERENCES Tweet(TweetID),
    FOREIGN KEY(CommentID) REFERENCES Comments(CommentID)
);

CREATE TABLE User (
    UserID INTEGER NOT NULL,
    Username VARCHAR(50),
    Verified VARCHAR(10),
    Followers INTEGER,
    PRIMARY KEY(UserID)
);

CREATE TABLE Tweet (
    TweetID INTEGER NOT NULL,
    UserID INTEGER NOT NULL,
    Content VARCHAR(200),
    PRIMARY KEY(TweetID),
    FOREIGN KEY(UserID) REFERENCES User(UserID)
);

CREATE TABLE HashtagsInContent (
    HashtagID INTEGER NOT NULL,
    TweetID INTEGER,
    CommentID INTEGER,
    FOREIGN KEY(HashtagID) REFERENCES Hashtag(HashtagID),
    FOREIGN KEY(TweetID) REFERENCES Tweet(TweetID),
    FOREIGN KEY(CommentID) REFERENCES Comments(CommentID)
);

CREATE TABLE Hashtag (
    HashtagID INTEGER,
    Content VARCHAR(50),
    PRIMARY KEY(HashtagID)
);