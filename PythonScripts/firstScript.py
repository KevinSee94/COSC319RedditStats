import praw
import json
#Create a new instance of the Reddit object
r = praw.Reddit('Comment scraper for /r/twobestfriendsplay written by /u/Kev_alt')
#Log in with my alt account
r.login('Kev_alt', '2wsx@WSX')
#New instance of subreddit object for /r/twobestfriendsplay
#TODO: Once working build is done with staic, make this work off of user input
subreddit = r.get_subreddit('twobestfriendsplay')

#Get the 30 current top ('hot', as reddit calls them) posts
#TODO: Once working build is done with static, make this work off of user input
postList = subreddit.get_hot(limit=30)

#Empty list to hold elements to be written in loop
attrList = []

#Loop through posts in subreddit
for post in postList:
	#If the post has over 250 comments, make those 'more comments' into comments.  Error is caused without this
	post.replace_more_comments(limit=None, threshold=0)
	commList = post.comments
	for comment in commList:
		#Store the body, comment id, name of the parent post, the score of the post, and the parent id of the post
		#TODO: Add/change the attributes that are stored form each comment
		bod = str(comment.body.encode('utf-8'))
		auth = str(comment.author)
		commId = str(comment.id.encode('utf-8'))
		postSub = str(comment.submission)
		postScore = str(comment.score)
		parentId = str(comment.parent_id.encode('utf-8'))
		data =  { 'Body':bod, 'Author':auth, 'CommentId':commId, 'Submission':postSub, 'Score':postScore, 'ParentId':parentId }
		data_in_json = json.dumps(data)
		# print data_in_json
		attrList.append(data_in_json)
	#Open text file and write the JSON elements of attrList to it
	letstrythis = json.dumps(attrList)
	f = open("output133.txt", "w")
	f.write(letstrythis)
	# f.write( "$scope.names = [" )
	# for element in attrList:
	# 	f.write(element + ",")
	# f.write("]")
	f.close()
