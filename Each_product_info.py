from requests_html import HTMLSession

url = "https://www.mymarket.ge"
s = HTMLSession()
r = s.get(url)
r.html.render(sleep=1, timeout=10000)



def get_info(url):
    r = s.get(url)
    product_info_dict = {}
    try:
        detailed_info = r.html.find('.spec-list', first=True).html

        splitted_elements = detailed_info.split('\n')
        product_info_list = [x.strip() for x in splitted_elements if splitted_elements.index(x) % 2 == 1]
        # The code above is getting elements from specifications and convert to list same as below
        # for x in splitted_elements:
        #     if splitted_elements.index(x)%2 == 1:
        #         test1.append(x.strip())

        x = 0
        while x < len(product_info_list):
            product_info_dict[product_info_list[x]] = product_info_list[x + 1]
            x += 2
        return product_info_dict
    except:
        product_info_dict ={}
        return product_info_dict

