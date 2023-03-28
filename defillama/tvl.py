from typing import List, Dict, Union
from ._utils import get

BASE_URL = "https://api.llama.fi"


def get_chains() -> List[Dict]:
    """**Returns basic information about all chains.**

    Function returns the following data for each chain:

    * gecko_id: CoinGecko ID of the chain
    * tvl: Current TVL in the chain
    * tokenSymbol: Chain symbol (e.g. ETH)
    * cmcId: CoinMarketCap ID of the chain
    * name: Given name of the chain
    * chainId: DeFillama ID of the chain

    *Endpoint: GET /chains*

    Returns:
      List[Dict]: Requested data

    """

    url = f"{BASE_URL}/chains"

    return get(url)


def get_protocols(protocol: str = None) -> Union[List[Dict], Dict]:
    """**Returns basic protocol data with their total TVL and TVL in
    each chain.**

    When no protocol is specified, function returns basic data for all
    protocols alongwith their TVL. When a protocol is specified, function
    returns basic data and additional protocol specific data.

    Function may return the following data when no protocol is specified:

    * id: DeFiLlama ID of the protocol
    * name: Registered protocol name
    * address: Protocol address
    * symbol: Protocol symbol
    * url: URL of the protocol website
    * description: Summary of the prtocol
    * chain: Chain the protocol is deployed on
    * logo: URL to the protocol logo
    * audits: Audits done on the protocol
    * audit_note: Audit note for the protocol
    * gecko_id: CoinGecko ID of the protocol
    * cmcId: CoinMarketCap ID of the chain
    * category: Type of the protocol
    * chains: List of chains where the protocol is deployed.
    * module: ???
    * twitter: Twitter username associated with the protocol
    * forkedFrom: Parent protocol of the protocol
    * oracles: List of oracles used by the protocol
    * listedAt: Timestamp when the protocol was listed
    * slug: Protocol slug name
    * tvl: Current TVL in the protocol
    * chainTvls: Current TVL in each chain on which the protocol is deployed.
      Note that this property changes to currentChainTvls when a chain is
      specified.
    * change_1h: Change in TVL within 1 hour
    * change_1d: Change in TVL within 1 day
    * change_7d: Change in TVL within 7 days
    * mcap: Current market cap of the protocol

    If a protocol is specified the following data maybe returned:

    * audit_links: Links to the audits done on the protocol
    * treasury: Treasury address of the protocol
    * openSource: Whether the protocol is open source or not (True/False)
    * governanceID: Snapshot of the ENS address of the protocol
    * currentChainTvls: Current TVL in each deployed chain of the deployed.
    * chainTvls: Historical TVL in each chain on which the protocol is deployed
    * tokens: History of TVL of associated tokens
    * tvl: History of TVL of the protocol
    * isParentProtocol: Whether the protocol is derived or not (True/False)
    * metrics: Historical data of the protocol's metrics
    * raises: Historical data of the protocol's funding rounds
    * tokenBreakdowns: Token TVL history
    * otherProtocols: List of protocols derived from the protocol
    * hallmarks: Hitory of the protocol's hallmarks

    *Endpoints: GET /protocols, GET /protocol/{protocol}*

    Args:
      protocol(str): Protocol slug. Defaults to None.

    Returns:
      List[Dict] | Dict: Requested data

    """

    if protocol is None:
        url = f"{BASE_URL}/protocols"
    else:
        url = f"{BASE_URL}/protocol/{protocol}"

    return get(url)


def get_historical_chains_tvl(chain: str = None) -> List[Dict]:
    """**Returns historical TVL (excludes liquid staking and double counted TVL)
    for all or a specified chain.**

    Passing a chain is optional as historical TVL (excluding liquid staking
    and double counted TVL) for all chains is returned by default.

    Function returns the following data:

    * date: Date of the TVL
    * tvl: Historical TVL (excluding liquid staking and double counted TVL)

    *Endpoints: GET /historicalChainTVL, GET /historicalChainTVL/{chain}*

    Args:
      chain(str): Chain slug. Defaults to None.

    Returns:
      List[Dict]: Requested data

    """

    if chain is None:
        url = f"{BASE_URL}/v2/historicalChainTvl"
    else:
        url = f"{BASE_URL}/v2/historicalChainTvl/{chain}"

    return get(url)


def get_charts(chain: str = None) -> List[Dict]:
    """**Returns historical TVL of all or a specified chain.**

    Passing a chain is optional as historical TVL for all chains is returned
    by default.

    Function returns the following data:

    * date: Date of the TVL
    * tvl: Historical TVL

    *Endpoints: GET /charts, GET /charts/{chain}*

    Args:
      chain(str): Chain slug. Defaults to None.

    Returns:
      List[Dict]: Requested data

    """

    if chain is None:
        url = f"{BASE_URL}/charts"
    else:
        url = f"{BASE_URL}/charts/{chain}"

    return get(url)


def get_protocol_tvl(protocol: str) -> int:
    """**Returns the current TVL of a specified protocol.**

    *Endpoint: GET /tvl/{protocol}*

    Args:
      protocol(str): Protocol slug

    Returns:
      int: Current TVL of the specified protocol

    """

    url = f"{BASE_URL}/tvl/{protocol}"

    return get(url)
