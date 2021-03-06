import json
import urllib2

def parseComment(url, t1Score, t1Body, postTitle):
    jsonUrl = url + '.json?sort=top'
    hdr = { 'User-Agent' : 'just testing the tests'}
    req = urllib2.Request(jsonUrl, headers=hdr)
    response = urllib2.urlopen(req)
    the_page = response.read()
    page = json.loads(the_page)
    page = page[1]['data']['children'][0]['data']
    if page['body'] == '[deleted]':
        return
    if page['replies'] == "":
        return
    try:
        page = page['replies']['data']['children']
    except Exception, e:
        print url
        raise Exception(e)
    for comment in page:
        if comment['kind'] == 't1' and comment['data']['score'] > t1Score + 100 + t1Score/20:
            if comment['data']['body'] != "[deleted]" and len(comment['data']['body']) < 384:
                commentPairs.append({'postTitle': postTitle, 'comment': t1Body, 'response': comment['data']['body']})
                print 'Comment Added'
        else:
            return


def getPage(url, postTitle):
    jsonUrl = url + '.json?sort=top'
    hdr = { 'User-Agent' : 'just testing the tests'}
    req = urllib2.Request(jsonUrl, headers=hdr)
    response = urllib2.urlopen(req)
    the_page = response.read()
    page = json.loads(the_page)
    page = page[1]['data']['children']
    for comment in page:
        if comment['kind'] == 't1':
            if comment['data']['score'] > 50 and len(comment['data']['body']) < 384:
                parseComment(url + comment['data']['id'], comment['data']['score'], comment['data']['body'], postTitle)
            else:
                break
    with open('data.txt', 'w') as outfile:
        json.dump(commentPairs, outfile)
    print 'File Saved'


def getPageList(url):
    hdr = { 'User-Agent' : 'just testing the tests' }
    req = urllib2.Request(url, headers=hdr)
    response = urllib2.urlopen(req)
    the_page = response.read()
    page = json.loads(the_page)
    for i in page['data']['children']:
        print i['data']['title'].encode('ascii', 'ignore')
        if alreadyHave(i['data']['title']):
            continue
        getPage("http://www.reddit.com" + i['data']['permalink'], i['data']['title'])

def alreadyHave(title):
    for exists in commentPairs:
        if exists['postTitle'] == title:
            return True
    return False


commentPairs = json.load(open('data.txt'))
getPageList("http://www.reddit.com/r/AskReddit/top/.json?sort=top&t=week")
getPageList("http://www.reddit.com/r/todayilearned/top/.json?sort=top&t=week")
getPageList("http://www.reddit.com/r/Showerthoughts/top/.json?sort=top&t=week")

print commentPairs

with open('data.txt', 'w') as outfile:
  json.dump(commentPairs, outfile)