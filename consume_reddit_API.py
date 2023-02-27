#consume_reddit_API
from  utils import RedditDicts
import config, requests
from requests.auth import HTTPBasicAuth

basic_auth = HTTPBasicAuth(
    username=config.CLIENT_ID,
    password=config.SECRET
)

GRANT_INFORMATION = dict(
    grant_type="password",
    username=config.USER, 
    password=config.PW 
)

headers = {'User-Agent': "Mozilla"}


POST_URL = "https://www.reddit.com/api/v1/access_token"

access_post_response = requests.post(
    url=POST_URL,
    headers=headers,
    data=GRANT_INFORMATION,
    auth=basic_auth
).json()

headers['Authorization'] = access_post_response.get('token_type') + ' ' + access_post_response.get('access_token')

topic = 'Python'
URL = f"https://oauth.reddit.com/r/{topic}/hot"

response = requests.get(
    url=URL,
    headers=headers
).json()

full_response = response.get('data').get('children')

oRedditDicts = RedditDicts()
endpoint_data = oRedditDicts.fill_reddit_dict(full_response)
indexed_endpoint_data = oRedditDicts.enumerate_reddit_dict(endpoint_data)





