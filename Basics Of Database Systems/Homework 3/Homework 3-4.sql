CREATE VIEW Comments_of_comments AS
SELECT 
    (SELECT Username FROM User WHERE User.UserID = Comments.UserID) AS User,
    Content AS Comment,
    FK_CommentID AS "Commented on"
FROM
    Comments
WHERE FK_CommentID IS NOT NULL
ORDER BY User;