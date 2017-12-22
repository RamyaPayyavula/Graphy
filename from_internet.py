
import urllib
from pyramid.response import Response
from pyramid.view import view_config

@view_config(route_name="from_internet", request_method='POST')
def from_internet(request):

    data=request.json_body
    web_url=data["url"]
    stock_price_url = web_url

    source_code = urllib.request.urlopen(stock_price_url).read().decode()

    stock_data = []
    split_source = source_code.split('\n')

    for line in split_source[0:]:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'values' not in line:
                stock_data.append(line)
    return Response("Data from websites")