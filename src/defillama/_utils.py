import pycurl
import certifi
from json import loads, dumps
from io import BytesIO
from typing import List, Dict, Union

USERAGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'


def get(url: str) -> any:
    """Utility function for GET request to API
    
    Function uses PyCurl to make a GET request to the API.
    A user-agent is used to mimic a browser request.

    Args:
      url(str): String of the URL to make the request to.
      url: str: 

    Returns:
      any: Response from the API.

    """

    buffer = BytesIO()
    curl = pycurl.Curl()
    curl.setopt(pycurl.USERAGENT, USERAGENT)
    curl.setopt(pycurl.URL, url)
    curl.setopt(pycurl.WRITEDATA, buffer)
    curl.setopt(pycurl.CAINFO, certifi.where())
    curl.perform()
    curl.close()

    response = buffer.getvalue()
    response = loads(response.decode('utf-8'))

    return response


def arg_parser(arg: Union[List[Dict[str, str]], Dict[str, List], List],
               format: str) -> str:
    """Parse a list of dict of string key and value pairs to a formatted string
    
    The string formats that can be requested are:
    - normal: Characters are kept intact
    - encoded: Characters are encoded to HTML URL encoding
    - list: Characters are joined into a comma separated string

    Args:
      arg(Union[List[Dict[str): 
      arg(Union[List[Dict[str): Can be a list of dict of string key and value pairs, a dict of
      arg(Union[List[Dict[str): Can be a list of dict of string key and value pairs, a dict of
    string key and list of values, or a list of strings.
      format(str): Requested format of the string.
      arg: Union[List[Dict[str: 
      str]]: 
      Dict[str: 
      List]: 
      format: str: 

    Returns:
      str: Parsed string output for the API request.

    """

    if format == 'encoded':
        arg = dumps(arg).replace(' ', '')

        encodeDict = {'{': '%7B', '}': '%7D',
                      '[': '%5B', ']': '%5D',
                      '"': '%22'}

        for char, code in encodeDict.items():
            arg = arg.replace(char, code)

    elif format == 'list':
        arg = ','.join(arg)

    elif format == 'normal':
        arg = [f"{key}:{value}" for item in arg for key, value in item.items()]
        arg = ','.join(arg)

    return arg
