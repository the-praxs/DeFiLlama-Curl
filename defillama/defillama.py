"""
DeFi Llama Python API interface using PyCurl library.
"""

import pycurl
import certifi
from json import loads
from io import BytesIO

# --------- Constants --------- #

BASE_URL = "https://api.llama.fi"
PRICE_URL = "https://coins.llama.fi"

# --------- Constants --------- #
class DefiLlama:
    """
    DeFi Llama class to act as DeFi Llama's API client.
    All the requests can be made through this class.
    """

    def __init__(self):
        """
        Initialize the object
        """
        self.buffer = BytesIO()
        self.curl = pycurl.Curl()
        self.curl.setopt(pycurl.USERAGENT, "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36")

    def _send_message(self, method, endpoint, type, data=None):
        """
        Send API request.
        :param method: HTTP method (get, post, delete, etc.)
        :param endpoint: Endpoint (to be added to base URL)
        :param params: HTTP request parameters
        :param data: JSON-encoded string payload for POST
        :return: dict/list: JSON response
        """
        if type == 'COINS':
            url = PRICE_URL + endpoint
        else:
            url = BASE_URL + endpoint

        self.curl.setopt(pycurl.URL, url)
        self.curl.setopt(pycurl.WRITEDATA, self.buffer)
        self.curl.setopt(pycurl.CAINFO, certifi.where())
        self.curl.perform()
        self.curl.close()
        
        response = self.buffer.getvalue()
        response = loads(response.decode('utf-8'))

        return response

    def _get(self, endpoint, type):
        """
        Get API request
        :param endpoint: Endpoint (to be added to base URL)
        :param type: TVL or coins for URL access
        :return:
        """
        return self._send_message('GET', endpoint, type=type)

    def _post(self, endpoint, type, data, params=None):
        """
        Post API request
        :param endpoint: Endpoint (to be added to base URL)
        :return:
        """
        return self._send_message('POST', endpoint, type=type, data=data)

    def get_protocols(self):
        """
        Returns basic information on all listed protocols, their current
        TVL and the changes to it in the last hour/day/week.
        Endpoint: GET /protocols

        :return: JSON response
        """
        path = '/protocols'

        return self._get(path, type='TVL')

    def get_protocol(self, protocol):
        """
        Returns historical data on the TVL of a protocol along with some basic data on it.
        The fields `tokensInUsd` and `tokens` are only available for some protocols..
        Endpoint: GET /protocol/{name}

        :param: name : ID of the protocol to get (eg: uniswap, WBTC...).
            This can be obtained from the /protocols endpoint
        :return: JSON response
        """
        path = f'/protocol/{protocol}'

        return self._get(path, type='TVL')

    def get_charts(self):
        """
        Returns historical values of the total sum of TVLs from all listed protocols.
        Endpoint: GET /charts

        :return: JSON response
        """
        path = '/charts'

        return self._get(path, type='TVL')

    def get_chart(self, chain):
        """
        Returns historical values of the TVLs of a chain.
        Endpoint: GET /charts/{chain}

        :return: JSON response
        """
        path = f'/charts/{chain}'

        return self._get(path, type='TVL')

    def get_tvl_protocol(self, protocol):
        """
        Returns historical values of the total sum of TVLs from given protocol.
        Mainly meant to make life easier for users that import data to spreadsheets
        Endpoint: GET /tvl/{protocol}

        :param: name : ID of the protocol to get (eg: uniswap, WBTC...).
            This can be obtained from the /protocols endpoint
        :return: JSON response
        """
        path = f'/tvl/{protocol}'

        return self._get(path, type='TVL')

    def get_chains(self):
        """
        Returns current tvl of all chains.
        Endpoint: GET /chains

        :return: JSON response
        """
        path = '/chains'

        return self._get(path, type='TVL')

    def get_block_timestamp(self, chain, timestamp):
        """
        Returns the closest block of a timestamp
        Endpoint:

        :params: chain: 
                timestamp: 
        :return: JSON response
        """
        path = f'/block/{chain}/{timestamp}'

        return self._get(path, type='COINS')

    def post_prices(self, data):
        """
        Returns the closest block of a timestamp
        Endpoint:

        :params: data:  
        :return: JSON response
        """

        path = '/prices'
        
        return self._post(path, type='COINS', data=data)

    