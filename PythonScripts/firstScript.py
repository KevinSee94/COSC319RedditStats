import praw

r = praw.Reddit('Comment scraper for /r/twobestfriendsplay written by /u/Kev_alt')
r.login('Kev_alt', '2wsx@WSX')
subreddit = r.get_subreddit('twobestfriendsplay')

findWords = ['woolie', 'hotdog man', 'hot dog man']
x = subreddit.get_new(limit=30)

for thing in x:
	y = thing.comments
	for that in y:
		comm = that.body
		commLow = comm.lower()
		found = any(string in commLow for string in findWords)
		if found:
			msg = comm
			r.send_message('Kev_alt', 'Bot found comment', msg)