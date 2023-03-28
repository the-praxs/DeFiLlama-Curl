from typing import List, Dict
from ._utils import get

BASE_URL = "https://bridges.llama.fi"


def get_bridges(include_chains: bool = True) -> List[Dict[str, any]]:
    """**Returns a list of bridges with summaries of their
    recent volumes.**

    Function returns the following data:

    * id: Bridge ID
    * name: Bridge name
    * displayName: Birdge name as displayed on DeFiLlama
    * icon: Icon link as on the parent server
    * volumePrevDay: Bridge volume on previous day
    * volumePrev2Day: Bridge volume on day before previous day
    * lastHourlyVolume: Bridge volume in the last hour
    * currentDayVolume: Bridge volume in the current day
    * lastDailyVolume: Bridge volume in the last day
    * dayBeforeLastVolume: Bridge volume in the day before last day
    * weeklyVolume: Bridge volume in the last week
    * monthlyVolume: Bridge volume in the last month
    * chains: Number of chains supported by the bridge
    * destinationChain: Destination chain of the bridge

    *Endpoint: GET /bridges*

    Args:
      include_chains(bool): Whether to include a list of chains.
        Defaults to True.

      include_chains: bool:  (Default value = True)

    Returns:
      List[Dict[str, any]]: Requested data

    """

    url = f"{BASE_URL}/bridges?includeChains={str(include_chains).lower()}"

    return get(url)['bridges']


def get_bridge_by_id(id: int) -> Dict[str, any]:
    """**Returns the summary of a bridge volume and volume breakdown by chain
    with the given ID.**

    Function returns the following data:

    * id: Bridge ID
    * name: Bridge name
    * displayName: Birdge name as displayed on DeFiLlama
    * lastHourlyVolume: Bridge volume in the last hour
    * currentDayVolume: Bridge volume in the current day
    * lastDailyVolume: Bridge volume in the last day
    * dayBeforeLastVolume: Bridge volume in the day before last day
    * weeklyVolume: Bridge volume in the last week
    * monthlyVolume: Bridge volume in the last month
    * lastHourlyTxs: Number of deposits and withdrawls in the last hour
    * currentDayTxs: Number of deposits and withdrawls in the current day
    * prevDayTxs: Number of deposits and withdrawls in the last day
    * dayBeforeLastTxs: Number of deposits and withdrawls in the day before last day
    * weeklyTxs: Number of deposits and withdrawls in the last week
    * monthlyTxs: Number of deposits and withdrawls in the last month
    * chainBreakdown: Volume and transaction breakdown by chain
    * destinationChain: Destination chain of the bridge

    *Endpoint: GET /bridges/{id}*

    Args:
      id(int): Bridge ID

    Returns:
      Dict[str, any]: Requested data

    """

    url = f"{BASE_URL}/bridge/{id}"

    return get(url)


def get_volume(chain: str = 'all',
               id: int = None) -> List[Dict[str, any]]:
    """**Returns histirical volume data for a bridge, chain, or bridge on a
    particular chain.**

    Function returns the following data:

    * date: Timestmap of the data
    * depositUSD: Deposited volume in USD
    * withdrawUSD: Volume withdrawn in USD
    * depositTxs: Number of deposits
    * withdrawTxs: Number of withdrawls

    *Endpoint: GET /bridgevolume/{chain}*

    Args:
      chain(str): Chain slug. Defaults to 'all' for volumes
        on all chain.

      id(int): Bridge ID. Defaults to None.

    Returns:
      List[Dict[str, any]]: Requested data

    """

    if id is None:
        url = f"{BASE_URL}/bridgevolume/{chain}"
    else:
        url = f"{BASE_URL}/bridgevolume/{chain}?id={id}"

    return get(url)


def get_stats(timestamp: int,
              chain: str,
              id: int = None) -> Dict[str, any]:
    """**Returns a 24 hour token and address volume breakdown for a bridge.**

    Function returns the following data:

    * date: Timestamp of the data

    * totalTokensDeposited: Dictionary containing token address as the key and
      the total volume and amount in USD deposited as the value

    * totalTokensWithdrawn: Dictionary containing token address as the key and
      the total volume and amount in USD withdrawn as the value

    * totalAddressesDeposited: Dictionary containing address as the key and
      the total volume deposited in USD and number of transactions as
      the value.

    *Endpoint: GET /bridgestats/{timestamp}/{chain}*

    Args:
      timestamp(int): UNIX timestamp requested. Data returned will be for
        the 24hr period starting at 00: 00 UTC that the timestamp lands in.

      chain(str): Chain slug

      id(int): Bridge ID. Defaults to None.

    Returns:
      Dict[str, any]: Requested data

    """

    if id is None:
        url = f"{BASE_URL}/bridgestats/{timestamp}/{chain}"
    else:
        url = f"{BASE_URL}/bridgedaystats/{timestamp}/{chain}?id={id}"

    return get(url)


def get_transactions(id: int,
                     chain: str,
                     address: dict,
                     start: int,
                     end: int,
                     limit: int = 100) -> List[Dict[str, any]]:
    """**Returns all the transactions for a bridge within a date range.**

    Transactions are only returned that are bridging from the specified source
    chain and with specified address as from or to.

    Function returns the following data:

    * tx_hash: Transaction hash address
    * ts: Transaction timestamp
    * tx_block: Transaction block number
    * tx_from: Transaction from address
    * tx_to: Transaction to address
    * token: Token address
    * amount: Amount of token transferred
    * chain: Chain where the transaction occurred
    * bridge_name: Bridge name that the transaction occurred on
    * usd_value: USD value of the transaction
    * sourceChain: Source chain of the token transfer

    *Endpoint: GET /transactions/{id}*

    Args:
      id(int): Bridge ID

      chain(str): Chain slug

      address(dict): Chain name and from/to address as key-value pair

      start(int): Start timestamp for date range

      end(int): End timestamp for date range

      limit(int): Number of transactions to return.
        Defaults to 100.

    Returns:
      List[Dict[str, any]]: Requested data

    """

    url = f"{BASE_URL}/transactions/{id}?starttimestamp={start}&endtimestamp={end}&sourcechain={chain}&address={address}&limit={limit}"

    return get(url)
