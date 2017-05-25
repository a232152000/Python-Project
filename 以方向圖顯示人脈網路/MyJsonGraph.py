import json
import networkx as nx # pip install networkx
import requests # pip install requests
from networkx.readwrite import json_graph

# Display noded graph
#in_set: the input to'me'
#out_set: the output from 'me'
#file is saved to force.json
def saveJsonGraph(in_set,  out_set, in_weight=1, out_weight=10, in_color='red', out_color='blue'):
    nxg = nx.DiGraph() #not nx.Graph

    nxg.add_node('me', {'size': 10, 'score': 0.5, 'type': 'circle'})
    
    [ nxg.add_node(mf, {'size': 20, 'score': 0.8, 'type': 'square'}) for mf in in_set ]

    [ nxg.add_node(mf, {'size': 10, 'score': 0.2, 'type': 'triangle'}) for mf in out_set ]
    
    [ nxg.add_edge('me', mf, {'weight': in_weight, 'color':in_color}) for mf in in_set ]

    [ nxg.add_edge(mf, 'me',{'weight': out_weight, 'color': out_color}) for mf in out_set ]


    # Start from here to save to json file
    nld = json_graph.node_link_data(nxg)
    json.dump(nld, open('force.json','w'))
    print ('force.json file saved!')


# Display edged graph
#in_set: the input to'me'
#out_set: the output from 'me'
#file is saved to force.json
def saveJsonEdgedGraph(in_set,  out_set):
    nxg = nx.DiGraph() #not nx.Graph
    
    [ nxg.add_edge( mf, 'me', {'type': 'licensing'}) for mf in in_set ]

    [ nxg.add_edge( 'me', mf,{'type': 'suit'}) for mf in out_set ]


    # Start from here to save to json file
    nld = json_graph.node_link_data(nxg)
    json.dump(nld, open('force.json','w'))
    print ('force.json file saved!')
def saveJson(in_set1, out_set1, person1, in_set2, out_set2, person2):
    #第一個人追隨的,第一個人被追的,第一個人,...
    nxg = nx.DiGraph() #not nx.Graph
    
    [ nxg.add_edge( mf, person1, {'type': 'licensing'}) for mf in in_set1 ]

    [ nxg.add_edge( person1, mf,{'type': 'suit'}) for mf in out_set1 ]
    
    [ nxg.add_edge( mf, person2, {'type': 'licensing'}) for mf in in_set2 ]

    [ nxg.add_edge( person2, mf,{'type': 'suit'}) for mf in out_set2 ]

    # Start from here to save to json file
    nld = json_graph.node_link_data(nxg)
    json.dump(nld, open('force.json','w'))
    print ('force.json file saved...!')
