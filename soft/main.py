import Thumbnail_info
import requests
from time import sleep


#Run Code every [time_in_seconds] mins.

time_in_seconds = 180

while True:

    url = "https://www.mymarket.ge/ka/search/getproducts"
    payload = "PriceFrom=100&PriceTo=1000&CatID=53"
    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://www.mymarket.ge',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.mymarket.ge/ka/search/53/iyideba-Laptop-kompiuterebi/?PriceFrom=250&PriceTo=1200&CatID=53',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': 'split_test_version=v1; _ga=GA1.2.2002612496.1598946619; _fbp=fb.1.1598946619000.1811619757; _hjid=0104bc21-3511-451e-8f09-ab884b6fe526; __dtsu=10401598947266CBBA0F043530D17D8D; Lang=ka; ka=da; SHOW_BETA_POPUP=B; APP_VERSION=B; _gid=GA1.2.2088452579.1601231805; _hjShownFeedbackMessage=true; banShown-Vast=1; _fbc=fb.1.1601232781150.IwAR2LScR6c0BGuOQkBQXST6-4DOezJ53vsXR2jTbGhwBF3IlY-DUR6vz5488; PHPSESSID=974gad0d6lc30vk29g96ti09v1; _hjTLDTest=1; _hjAbsoluteSessionInProgress=1; PopUpLog=%7B%22%2A%22%3A%222020-09-28+12%3A57%3A51%22%7D; CSID=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJEYXRhIjp7IkJpcnRoWWVhciI6bnVsbCwiVHlwZUlEIjoiMCIsIkZpcnN0TmFtZSI6IiIsIkxhc3ROYW1lIjoiIiwiR2VuZGVySUQiOm51bGwsIkFQSVNJRCI6IjRjZGQyM2M4MTEzNWQwMjdjMDViODZiY2QzYWI3ZmQ1N2M5MDc5Y2UzN2I4NzgyNWI5YTU2YThlYjNiYTMwYzE2YTBiYjNiNDdmMjQ0YWJiNzExNTVhNDhiYTZjNmZiYTIzN2IyZjQ3MDA3NDIyYmEyYzIzYTczMmI1Y2ZlOGY0Lk16TXhOVGt4TVEifSwiVG9rZW5JRCI6IjVpc2NmbFwvOEVuMnoxYnQxaXJqXC8rRU1RaHJGZVNlVjVTbmR2MmM5Qjh6MD0iLCJJc3N1ZWRBdCI6MTYwMTI4ODcyNCwiRXhwaXJlc0F0IjoxNjAxMjg5MDI0fQ.bwve1eEBcC03kXlqe9PlpID7S3pDXDwwYg4fNJLxrYM; LastSearch=%7B%22CatID%22%3A%2253%22%2C%22CondTypeID%22%3A%22-1%22%2C%22PriceFrom%22%3A%22100%22%2C%22PriceTo%22%3A%221000%22%2C%22Keyword%22%3A%22%22%7D; CookieID=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJEYXRhIjp7IklEIjoiOTUwNjU1MSIsImN0IjoxNjAxMjg4NzkyLCJVc2VySUQiOiIzMzE1OTExIn0sIlRva2VuSUQiOiIxajJoUVlRVGszdlltcklidzVka2JtSHBCV0tjNXFPZFwvd29JT2dvZlc3UT0iLCJJc3N1ZWRBdCI6MTYwMTI4ODc5MiwiRXhwaXJlc0F0IjoxNjAxMjg5MDkyfQ.ydV8PZ0g1ON71sXgKFKQN5fwaoHglLUmkEDcahTfyUA; ka=da; SHOW_BETA_POPUP=B; APP_VERSION=B; Lang=ka; split_test_version=v1; CookieID=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJEYXRhIjp7IklEIjoiOTUwNjU1MSIsImN0IjoxNjAxMjg4ODU5LCJVc2VySUQiOiIzMzE1OTExIn0sIlRva2VuSUQiOiJlMUpYSGRSdWNvdTRIK01mU05VV2FBUU5BaE1cL09Xdmg5WURLejI3aGI2RT0iLCJJc3N1ZWRBdCI6MTYwMTI4ODg1OSwiRXhwaXJlc0F0IjoxNjAxMjg5MTU5fQ.-oN5tmfcz0hFH5CLx5NoUPn5WDE4hRulLFoDldgOM0s; LastSearch=%7B%22CatID%22%3A%2253%22%2C%22PriceFrom%22%3A%22100%22%2C%22PriceTo%22%3A%221000%22%7D'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    json_response = response.json()
    my_data = json_response['Data']['Prs']

    Thumbnail_info.retrieve_data(my_data)


    sleep(time_in_seconds)

