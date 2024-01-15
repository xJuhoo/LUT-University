CREATE TABLE "Comments" (
    "CommentID" INTEGER NOT NULL,
    "UserID" INTEGER NOT NULL,
    "TweetID" INTEGER,
    "FK_CommentID" INTEGER,
    "Content" VARCHAR(200),
    PRIMARY KEY("CommentID"),
    FOREIGN KEY("UserID") REFERENCES "User"("UserID") ON DELETE CASCADE,
    FOREIGN KEY("TweetID") REFERENCES "Tweet"("TweetID") ON DELETE CASCADE,
    FOREIGN KEY("CommentID") REFERENCES "Comments"("CommentID") ON DELETE CASCADE
);

CREATE TABLE "Likes" (
    "LikeID" INTEGER NOT NULL,
    "UserID" INTEGER NOT NULL,
    "TweetID" INTEGER,
    "CommentID" INTEGER,
    PRIMARY KEY("LikeID"),
    FOREIGN KEY("UserID") REFERENCES "User"("UserID") ON DELETE CASCADE,
    FOREIGN KEY("TweetID") REFERENCES "Tweet"("TweetID") ON DELETE CASCADE,
    FOREIGN KEY("CommentID") REFERENCES "Comments"("CommentID") ON DELETE CASCADE
);

CREATE TABLE "User" (
    "UserID" INTEGER NOT NULL,
    "Username" VARCHAR(50),
    "Verified" VARCHAR(10),
    "Followers" INTEGER,
    PRIMARY KEY("UserID")
);

CREATE TABLE "Tweet" (
    "TweetID" INTEGER NOT NULL,
    "UserID" INTEGER NOT NULL,
    "Content" VARCHAR(200),
    PRIMARY KEY("TweetID"),
    FOREIGN KEY("UserID") REFERENCES "User"("UserID") ON DELETE CASCADE
);

CREATE TABLE "HashtagsInContent" (
    "HashtagID" INTEGER NOT NULL,
    "TweetID" INTEGER,
    "CommentID" INTEGER,
    FOREIGN KEY("HashtagID") REFERENCES "Hashtag"("HashtagID") ON DELETE CASCADE,
    FOREIGN KEY("TweetID") REFERENCES "Tweet"("TweetID") ON DELETE CASCADE,
    FOREIGN KEY("CommentID") REFERENCES "Comments"("CommentID") ON DELETE CASCADE
);

CREATE TABLE "Hashtag" (
    "HashtagID" INTEGER,
    "Content" VARCHAR(50),
    PRIMARY KEY("HashtagID")
);