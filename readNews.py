import praw
import pyttsx

def get_news(limit):
	subs = r.get_subreddit("worldnews").get_hot(limit=limit)
	news = []
	for sub in subs:
		news.append(sub.title)
	return news 

def speak_news(headlines=[]):
	for s in headlines:
        	print s
		rate = engine.getProperty('rate')
		engine.setProperty('rate', 150)
        	engine.say(s)
      		engine.runAndWait()
 

if __name__ == "__main__":
	number_of_headlines = 5
	r = praw.Reddit(user_agent="my_application")
	engine= pyttsx.init()
	titles = get_news(number_of_headlines)
	speak_news(titles)

