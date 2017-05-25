import facebook # pip install facebook-sdk
import json
import networkx as nx # pip install networkx
import requests # pip install requests
from networkx.readwrite import json_graph
from collections import Counter
from functools import reduce
#return a dict with {post_id1: [p1, ..., pk] , }
def getPeopleWhoLikeYourPost(id, token, friends_id):
    url = 'https://graph.facebook.com/%s?fields=posts&access_token=%s'
    r = requests.get(url % ( id , token,) )
    response=json.loads(r.content)
    result = {};
    if response.get("posts"): #have posts
        for post in response['posts']['data']:
            pid = post['id'] #get the post id
            
            url2 = 'https://graph.facebook.com/%s?fields=likes&access_token=%s'
            r2 = requests.get(url2 % (pid, token,) )
            response2=json.loads(r2.content)        
            if response2.get('likes'):
                pList = [ f['id'] for f in response2['likes']['data'] if (f['id'] in friends_id)]
                result[pid] = pList
    return result

# Create a connection to the Graph API with your access token
ACCESS_TOKEN= 'EAACEdEose0cBAClQWlZB8ve4iZBPKNiLwjD1h889a8eVqyyYv3R7Pj1akLSgPPeXhGjtNspHZAFHohPh7R86XqEJxySd1WGCxLmdmT0ynunwEFLQsMOZCjO8GrSPK5coFKRvkG0B1pDttWzBsAZAxpeQT2qkasVvFX5skoJX5pYJ1VSZCj6Ic98gvphSDYF1kZD'
g = facebook.GraphAPI(ACCESS_TOKEN)

res = g.get_object('me')
meId,meName = res['id'],res['name']

friends  = { friend['id']: friend['name']
               for friend in g.get_connections('me', 'friends')['data'] }

friends[meId] = meName

# {fid1: {postid1: [f1,f2,...], postid2: [f1,...],...}, fid2: {...}, ...., }
  
ff = g.get_connections("me", "friends")['data']
friends_id=[]
for i in ff[::]:
    friends_id.append(i['id'])

likeFriendPost = { id: getPeopleWhoLikeYourPost (id, ACCESS_TOKEN, friends_id) for (id, _) in friends.items()} 
  

result =  {  p:Counter( reduce (lambda x, y: x+y, likeFriendPost[p].values()) ) for p in likeFriendPost if  len(likeFriendPost[p].values()) > 0}

graphEdges = [ (friends[p2], friends[p], result[p][p2])  for p in result
                                          for p2 in result[p] ]

def saveJsonLabeledEdgeGraph(edges):
    nxg = nx.DiGraph() #not nx.Graph
    
    [ nxg.add_edge( s, d, {'weight': w}) for s,d,w in edges ]

    # Start from here to save to json file
    nld = json_graph.node_link_data(nxg)
    json.dump(nld, open('labeledEdge.json','w'))
    print ('labeledEdge.json file saved!')
    
saveJsonLabeledEdgeGraph(graphEdges)