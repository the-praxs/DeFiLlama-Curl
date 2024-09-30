from typing import List, Dict, Union
from ._utils import get

BASE_URL = "https://stablecoins.llama.fi"


def get_stablecoins(include_prices: bool = True) -> List[Dict[str, any]]:
    """**Returns a list of all stablecoins alongwith their circulating amounts.**

    Function returns the following data:

    * id: Stablecoin ID as per DeFiLlama
    * name: Name of the stablecoin
    * symbol: Trading symbol of the stablecoin
    * gecko_id: CoinGecko ID of the stablecoin
    * pegType: Currency pegged to
    * pegMechanism: Type of currency pegged (fiat or crypto backed)
    * priceSource: Major source of price data
    * circulating: Current circulating amount in pegged currency
    * circulatingPrevDay: Circulating amount previous day in pegged currency
    * circulatingPrevWeek: Circulating amount previous week in pegged currency
    * circulatingPrevMonth: Circulating amount previous month in pegged
      currency
    * chainCirculating: Chains circulating the stablecoin alongwith their
      'circulating', 'circulatingPrevDay', 'circulatingPrevWeek' and
      'circulatingPrevMonth'.
    * chains: List of chains on which the stablecoin is available

    *Endpoint: GET /stablecoins*

    Args:
      include_prices(bool): whether to include current stablecoin prices.
        Defaults to True.

    Returns:
      List[Dict[str, any]]: Requested data

    """

    url = f"{BASE_URL}/stablecoins?includePrices={str(include_prices).lower()}"

    return get(url)["peggedAssets"]


def get_charts(
    type: str = "all", chain: str = None, stablecoin: int = None
) -> List[Dict[str, any]]:
    """**Returns historical market cap sum of all stablecoins or on a given
    chain.**

    Function returns the following data:

    * date: Timestamp of the data
    * totalCirculating: Market cap of all circulating pegged currencies
    * totalUnreleased: Market cap of all unreleased circulating pegged
      currencies
    * totalCirculatingUSD: Market cap of all circulating pegged currencies
      in USD
    * totalMintedUSD: Market cap of all minted pegged currencies in USD
    * totalBridgedToUSD: Market cap of all pegged currencies bridged to USD

    *Endpoints: GET /stablecoincharts/all, GET /stablecoincharts/{chain}*

    Args:
      type(str): Request data for 'all' stablecoins or those in 'chain'.
        Defaults to "all".

      chain(str): Chain slug. Requires type argument to be 'chain'.
        Defaults to None.

      stablecoin(int): Stablecoin ID. Requires type argument to be 'chain'.
        Defaults to None.

    Returns:
      List[Dict[str, any]]: Requested data

    """

    if type == "all":
        url = (
            f"{BASE_URL}/stablecoincharts/all"
            if stablecoin is None
            else f"{BASE_URL}/stablecoincharts/all?stablecoin={stablecoin}"
        )
    elif type == "chain":
        url = (
            f"{BASE_URL}/stablecoincharts/{chain}"
            if stablecoin is None
            else f"{BASE_URL}/stablecoincharts/{chain}?stablecoin={stablecoin}"
        )
    return get(url)


def get_distribution(stablecoin: int) -> Dict[str, any]:
    """**Returns the historical market cap and historical chain distribution
    of a stablecoin.**

    Function returns the following data:

    * id: Stablecoin ID as per DeFiLlama
    * name: Name of the stablecoin
    * address: Stablecoin address
    * symbol: Trading symbol of the stablecoin
    * url: Link to the stablecoin's website
    * description: Short summary describing the stablecoin
    * mintRedeemDescription: Short description describing the minting
      and exchange of the stablecoin
    * onCoinGecko: Whether the stablecoin is listed on CoinGecko
    * gecko_id: CoinGecko ID of the stablecoin
    * cmcId: CoinMarketCap ID of the stablecoin
    * pegType: Currency pegged to
    * pegMechanism: Type of currency pegged (fiat or crypto backed)
    * priceSource: Major source of price data
    * auditLinks: List of URL to the audit reports
    * twitter: Twitter link of the stablecoin
    * wiki: DeFiLlama wiki page for the stablecoin
    * chainBalances: Dictionary containing the chains on which the
      stablecoin is available alongwith their 'tokens', 'circulating',
      'minted', 'unreleased' and 'bridgedTo' amounts.

    *Endpoint: GET /stablecoin/{asset}*

    Args:
      stablecoin(int): Stablecoin ID.

    Returns:
      Dict[str, any]: Requested data

    """

    url = f"{BASE_URL}/stablecoin/{stablecoin}"

    return get(url)


def get_chains() -> List[Dict[str, any]]:
    """**Returns current market cap sum of all stablecoins on each chain.**

    Function requires no arguments and returns the following data:

    * gecko_id: CoinGecko ID of the stablecoin
    * totalCirculatingUSD: Market cap of all circulating pegged currencies
      in USD
    * tokenSymbol: Trading symbol of the stablecoin
    * name: Name of the chain on which the stablecoin is available

    *Endpoint: GET /stablecoinchains*

    Returns:
      List[Dict[str, any]]: Requested data

    """

    url = f"{BASE_URL}/stablecoinchains"

    return get(url)


def get_prices() -> List[Dict[str, any]]:
    """**Returns historical prices of all stablecoins.**

    Function requires no arguments and returns the following data:

    * date: Timestamp of the data
    * prices: Dictionary containing the stablecoin name and its price in USD

    *Endpoint: GET /stablecoinprices*

    Returns:
      List[Dict[str, any]]: Requested data

    """

    url = f"{BASE_URL}/stablecoinprices"

    return get(url)
