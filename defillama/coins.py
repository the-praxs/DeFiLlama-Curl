import time
import math
from typing import List, Dict
from ._utils import get, arg_parser

BASE_URL = "https://coins.llama.fi"


def get_current_prices(tokens: List[Dict[str, str]],
                       search_width: str = '6h') -> Dict[str, Dict[str, any]]:
    """**Returns current prices of tokens using their contract addresses.**

    Function returns a dictionary where the key is the requested token(s) with
    the contract address and the value is a dictionary containing the
    following data:

    * price: Current price of the token
    * symbol: Trading symbol of the token
    * timestamp: Timestamp of the current price
    * confidence: Depth of liquidity of the token indicating quality of price

    *Endpoint: GET /prices/current/{coins}*

    Args:
      tokens(List[Dict[str, str]]): List of dictionaries having the tokens
        and their contract addresses in the form of {chain}: {address}.
        Can also use 'coingecko': {protocol} for tokens listed on coingecko.

      search_width(str): Time period on either side to find price data.
        Follows regular chart notion where W = Week, D = day, H = hour,
        M = minute (not case sensitive). Defaults to '6h'.

    Returns:
      Dict[str, Dict[str, any]]: Requested data

    """

    tokens = arg_parser(tokens, format='normal')
    url = f"{BASE_URL}/prices/current/{tokens}?searchWidth={search_width}"

    return get(url)['coins']


def get_historical_prices(tokens: List[Dict[str, str]],
                          timestamp: int = math.floor(time.time()),
                          search_width: str = '6h') -> Dict[str, Dict[str, any]]:
    """**Returns historical prices of tokens using their contract addresses.**

    Function returns a dictionary where the key is the requested token(s) with
    the contract address and the value is a dictionary containing the
    following data:

    * price: Historical price of the token
    * symbol: Trading symbol of the token
    * timestamp: Timestamp of the historical price
    * confidence: Depth of liquidity of the token indicating quality of price

    *Endpoint: GET /prices/historical/{timestamp}/{coins}*

    Args:
      tokens(List[Dict[str, str]]): List of dictionaries having the tokens
        and their contract addresses in the form of {chain}: {address}.
        Can also use 'coingecko': {protocol} for tokens listed on coingecko.

      timestamp(int): UNIX timestamp when the historical price
        is requested. Defaults to the current timestamp.

      search_width(str): Time period on either side to find price data.
       Follows regular chart notion where W = Week, D = day, H = hour,
       M = minute (not case sensitive). Defaults to '6h'.

    Returns:
      Dict[str, Dict[str, any]]: Requested data

    """

    tokens = arg_parser(tokens, format='normal')
    url = f"{BASE_URL}/prices/historical/{timestamp}/{tokens}?searchWidth={search_width}"

    return get(url)['coins']


def get_historical_batch(tokens: Dict[str, List],
                         search_width: str = '6h') -> Dict[str, Dict[str, any]]:
    """**Returns historical prices of tokens at multiple timestamps.**

    Function returns a dictionary where the key is the requested token(s) with
    the contract address and the value is a dictionary containing the
    following data:

    * symbol: Trading symbol of the token
    * prices: List of dictionaries having the requested timestamps, prices and
      confidence of the token

    *Endpoint: GET /batchHistorical*

    Args:
      tokens(Dict[str, List]): List of dictionaries having the tokens
        and their contract addresses in the form of {chain}: {address}.
        Can also use 'coingecko': {protocol} for tokens listed on coingecko.

      search_width(str): Time period on either side to find price data.
        Follows regular chart notion where W = Week, D = day, H = hour,
        M = minute (not case sensitive). Defaults to '6h'.

    Returns:
      Dict[str, Dict[str, any]]: Requested data

    """

    tokens = arg_parser(tokens, format='encoded')
    url = f'{BASE_URL}/batchHistorical?coins={tokens}&searchWidth={search_width}'

    return get(url)['coins']


def get_charts(tokens: List[Dict[str, str]],
               start: int = None,
               end: int = math.floor(time.time()),
               span: int = 0,
               period: str = '24h',
               search_width: str = '3h') -> Dict[str, Dict[str, any]]:
    """**Returns the token prices at regular time intervals.**

    Function returns a dictionary where the key is the requested token(s) with
    the contract address and the value is a dictionary containing the
    following data:

    * symbol: Trading symbol of the token
    * confidence: Depth of liquidity of the token indicating quality of price
    * decimals: Smallest unit of the token that can be traded or transferred
    * prices: List of dictionaries having the requested timestamps and
      respective prices

    *Endpoint: GET /chart/{coins}*

    Args:
      tokens(List[Dict[str, str]]): List of dictionaries having the tokens
        and their contract addresses in the form of {chain}: {address}.
        Can also use 'coingecko': {protocol} for tokens listed on coingecko.

      start(int): UNIX timestamp of the earliest data point
        requested. Defaults to None.

      end(int): UNIX timestamp of the latest data point
        requested. Defaults to the current timestamp.

      span(int): Number of data points returned. Defaults to 0.

      period(str): Duration between data points. Defaults to '24h'.

      search_width(str): Time period on either side to find price data.
        Follows regular chart notion where W = Week, D = day, H = hour,
        M = minute (not case sensitive). Defaults to '6h'.

    Returns:
      Dict[str, Dict[str, any]]: Requested data

    """

    tokens = arg_parser(tokens, format='normal')

    if start and end:
        return ("Use either start or end parameter, not both")
    elif start is not None:
        url = f"{BASE_URL}/chart/{tokens}?start={start}&span={span}&period={period}&searchWidth={search_width}"
        return get(url)['coins']
    else:
        url = f"{BASE_URL}/chart/{tokens}?end={end}&span={span}&period={period}&searchWidth={search_width}"
        return get(url)['coins']


def get_percentage(tokens: List[Dict[str, str]],
                   timestamp: int,
                   look_forward: bool = False,
                   period: str = '24h') -> Dict[str, any]:
    """**Returns the percentage change of the token prices over time.**

    Function returns a dictionary having {tokens}:{percentage change} as the
    key-value pairs.

    *Endpoint: GET /percentage/{coins}*

    Args:
      tokens(List[Dict[str, str]]): List of dictionaries having the tokens
        and their contract addresses in the form of {chain}: {address}.
        Can also use 'coingecko': {protocol} for tokens listed on coingecko.

      timestamp(int): UNIX timestamp when the historical price is requested.
        Defaults to the current timestamp.

      look_forward(bool): Whether to request the duration after the provided
        timestamp. Defaults to False (looking back).

      period(str): Duration between data points. Follows regular chart notion
        where W = Week, D = day, H = hour, M = minute (not case sensitive).
        Defaults to '24h'.

    Returns:
      Dict[str, any]: Requested data

    """

    tokens = arg_parser(tokens, format='normal')
    look_forward = str(look_forward).lower()
    url = f"{BASE_URL}/percentage/{tokens}?timestamp={timestamp}&lookForward={look_forward}&period={period}"

    return get(url)['coins']


def get_first_prices(tokens: List[Dict[str, str]]) -> Dict[str, Dict[str, any]]:
    """**Returns the earliest timestamp price record for the token.**

    Function returns a dictionary where the key is the requested token(s) with
    the contract address and the value is a dictionary containing the
    following data:

    * symbol: Trading symbol of the token
    * price: Earliest recorded price of the token
    * timestamp: Timestamp of the earliest recorded price of the token

    *Endpoint: GET /prices/first/{coins}*

    Args:
      tokens(List[Dict[str, str]]): List of dictionaries having
        {token}:{address} as the key-value pairs. Can also use
        'coingecko': {protocol} for tokens listed on coingecko.

    Returns:
      Dict[str, Dict[str, any]]: Requested data

    """

    tokens = arg_parser(tokens, format='normal')
    url = f"{BASE_URL}/prices/first/{tokens}"

    return get(url)['coins']


def get_nearest_block(chain: str,
                      timestamp: int) -> Dict[str, int]:
    """**Returns the nearest block to the timestamp.**

    Function runs a binary search over a blockchain's blocks to get the closest
    one to a timestamp. Every time this is run new data is added to DeFiLlama's
    database, so each query permanently speeds up future queries. The height
    and the timestamp of the block are returned.

    *Endpoint: GET /block/{chain}/{timestamp}*

    Args:
      chain(str): Chain slug

      timestamp(int): Timestamp of the block

    Returns:
      Dict[str, int]: Requested data

    """

    url = f"{BASE_URL}/block/{chain}/{timestamp}"

    return get(url)
