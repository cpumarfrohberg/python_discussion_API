#utils.py
import numpy as np

class RedditDicts():
    
    def fill_reddit_dict(self, API_response) -> dict:
        '''Insert key-value pairs of indeces
        and title (text) for extracted Reddit discussion.
        @params:
        - API_response: list of dicts (.json) consisting
        of endpoint data.
        '''
        reddit_dict = dict()
        for post in API_response:
            id_ = post.get('data').get('id')
            title = post.get('data').get('title')
            reddit_dict[id_] = title
        return reddit_dict

    def enumerate_reddit_dict(self, reddit_json) -> dict:
        '''Insert additional key-value pairs of indeces.
        @params:
        - reddit_dict: list of dicts (.json) consisting
        of endpoint data.
        '''
        dict_vals = [vals for vals in reddit_json.values()]
        indeces = np.arange(0,28).tolist()
        reddit_json_indexed = dict(zip(indeces, list(dict_vals)))
        return reddit_json_indexed

