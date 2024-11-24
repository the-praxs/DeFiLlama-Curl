from typing import List, Dict
from ._utils import get

BASE_URL = "https://api.llama.fi"


def get_dex_overview(exclude_total_data_chart: bool = False,
                     exclude_total_data_chart_breakdown: bool = False,
                     data: str = "daily",
                     chain: str = None) -> Dict[str, any]:
    """**Returns all dexs with their volume summaries and history for all or
    specified chain.**

    Function may return the following data:

    * totalDataChart: List of aggregated chart data with their timestamp
    * totalDataChartBreakdown: List of aggregated chart data broken down by
      chains with their timestamp

    * protocols: List of dictionaries that may contain the following data -

        * name: Name of the protocol
        * disabled: Whether the protocol is disabled or not
        * displayName: Protocol name as displayed on DeFiLlama
        * module: Name of the protocol as mentioned on adapter API
        * category: Category to which the protocol belongs
        * logo: Protocol logo URL
        * change_1d: Change in the protocol's volume in the last 24 hours
        * change_7d: Change in the protocol's volume in the last 7 days
        * change_1m: Change in the protocol's volume in the last 30 days
        * change_7dover7d: Change in the protocol's volume in the last
          7 days over the change in the protocol's fees in the last 7 days
        * change_30dover30d: Change in the protocol's volume in the last
          30 days over the change in the protocol's volume in the
          last 30 days
        * total24h: Total volume collected by the protocol in the
          last 24 hours
        * total48hto24h: Total volume collected by the protocol in the
          last 48 hours to the last 24 hours
        * total7d: Total volume collected by the protocol in the
          last 7 days
        * total30d: Total volume collected by the protocol in the
          last 30 days
        * total14dto7d: Total volume collected by the protocol in the
          last 14 days to the last 7 days
        * total60dto30d: Total volume collected by the protocol in the
          last 60 days to the last 30 days
        * totalAllTime: Total volume collected by the protocol since
          the beginning
        * breakdown24h: Total volume collected by the protocol in the
          last 24 hours broken down by chains
        * chains: List of chains supported by the protocol
        * protocolType: Whether its a protocol or a chain
        * methodologyURL: URL of the methodology used to calculate the fees
        * methodology: Dictionary containing the methodology used to calculate
          the fees
        * latestFetchIsOk: Whether the latest fetch was successful or not
        * dailyVolume: Daily volume of the protocol
        * totalVolume: Total volume of the protocol

    *Endpoint: GET /overview/dexs, GET /overview/dexs/{chain}*

    Args:
      exclude_total_data_chart(bool): To exclude aggregated chart
        from response. Defaults to False.

      exclude_total_data_chart_breakdown(bool): To exclude broken
        down chart from response. Defaults to False.

      data(str): Request 'daily' or 'total' volume data.
        Defaults to 'daily'.

      chain(str): Chain slug. Defaults to None.

    Returns:
      Dict[str, any]: Requested data

    """

    excludeTotalDataChartBreakdown = str(exclude_total_data_chart_breakdown).lower()
    excludeTotalDataChart = str(exclude_total_data_chart).lower()
    dataType = f"{data}Volume"

    if chain is None:

        url = f"{BASE_URL}/overview/dexs?excludeTotalDataChart={excludeTotalDataChart}&excludeTotalDataChartBreakdown={excludeTotalDataChartBreakdown}&dataType={dataType}"
    else:
        url = f"{BASE_URL}/overview/dexs/{chain}?excludeTotalDataChart={excludeTotalDataChart}&excludeTotalDataChartBreakdown={excludeTotalDataChartBreakdown}&dataType={dataType}"

    return get(url)


def get_dex_summary(protocol: str,
                    exclude_total_data_chart: bool = False,
                    exclude_total_data_chart_breakdown: bool = False,
                    data: str = "daily") -> Dict[str, any]:
    """**Returns summary of a dex volume with historical data.**

    Function may return the following data:

    * name: Name of the protocol
    * displayName: Protocol name as displayed on DeFiLlama
    * disabled: Whether the protocol is disabled or not
    * logo: URL to the logo of the protocol
    * address: Protocol address on the blockchain
    * url: Protocol logo URL
    * description: Protocol description
    * audits: List of audits
    * category: Category to which the protocol belongs
    * twitter: Twitter handle of the protocol
    * audit_links: List of audit links
    * forkedFrom: Parent protocol from which this protocol was forked
    * gecko_id: CoinGecko ID of the protocol
    * totalDataChart: List of aggregated chart data with their timestamp
    * totalDataChartBreakdown: List of aggregated chart data broken down by
      chains with their timestamp
    * total24h: Total volume collected by the protocol in the
      last 24 hours
    * total48hto24h: Total volume collected by the protocol in the
      last 48 hours to the last 24 hours
    * total14dto7d: Total volume collected by the protocol in the
      last 14 days to the last 7 days
    * totalAllTime: Total volume collected by the protocol since
      the beginning
    * change_1d: Change in the protocol's volume in the last 24 hours
    * module: Name of the protocol as mentioned on adapter API
    * protocolType: Whether its a protocol or a chain
    * chains: List of chains supported by the protocol
    * methodologyURL: URL of the methodology used to calculate the fees
    * latestFetchIsOk: Whether the latest fetch was successful or not
    * childProtocols: Protocols derived from this protocol

    *Endpoint: GET /summary/dexs/{protocol}*

    Args:
      protocol(str): Protocol slug

      exclude_total_data_chart(bool): To exclude aggregated chart
        from response. Defaults to False.

      exclude_total_data_chart_breakdown(bool): To exclude broken
        down chart from response. Defaults to False.

      data(str): Request 'daily' or 'total' volume data.
        Defaults to 'daily'.

    Returns:
      Dict[str, any]: Requested data

    """

    excludeTotalDataChartBreakdown = str(exclude_total_data_chart_breakdown).lower()
    excludeTotalDataChart = str(exclude_total_data_chart).lower()
    dataType = f"{data}Volume"

    url = f"{BASE_URL}/summary/dexs/{protocol}?excludeTotalDataChart={excludeTotalDataChart}&excludeTotalDataChartBreakdown={excludeTotalDataChartBreakdown}&dataType={dataType}"

    return get(url)


def get_options_overview(exclude_total_data_chart: bool = False,
                         exclude_total_data_chart_breakdown: bool = False,
                         data: str = "daily",
                         type: str = "premium",
                         chain: str = None) -> Dict[str, any]:
    """**Returns all options dexs with their volume summaries and history for
    all or specified chain.**

    Function may return the following data:

    * totalDataChart: List of aggregated chart data with their timestamp
    * totalDataChartBreakdown: List of aggregated chart data broken down by
      chains with their timestamp

    * protocols: List of dictionaries that may contain the following data -

        * name: Name of the protocol
        * disabled: Whether the protocol is disabled or not
        * displayName: Protocol name as displayed on DeFiLlama
        * module: Name of the protocol as mentioned on adapter API
        * category: Category to which the protocol belongs
        * logo: Protocol logo URL
        * change_1d: Change in the protocol's volume in the last 24 hours
        * change_7d: Change in the protocol's volume in the last 7 days
        * change_1m: Change in the protocol's volume in the last 30 days
        * change_7dover7d: Change in the protocol's volume in the last
          7 days over the change in the protocol's fees in the last 7 days
        * change_30dover30d: Change in the protocol's volume in the last
          30 days over the change in the protocol's volume in the
          last 30 days
        * total24h: Total volume collected by the protocol in the
          last 24 hours
        * total48hto24h: Total volume collected by the protocol in the
          last 48 hours to the last 24 hours
        * total7d: Total volume collected by the protocol in the
          last 7 days
        * total30d: Total volume collected by the protocol in the
          last 30 days
        * total14dto7d: Total volume collected by the protocol in the
          last 14 days to the last 7 days
        * total60dto30d: Total volume collected by the protocol in the
          last 60 days to the last 30 days
        * totalAllTime: Total volume collected by the protocol since
          the beginning
        * breakdown24h: Total volume collected by the protocol in the
          last 24 hours broken down by chains
        * chains: List of chains supported by the protocol
        * protocolType: Whether its a protocol or a chain
        * methodologyURL: URL of the methodology used to calculate the fees
        * methodology: Dictionary containing the methodology used to calculate
          the fees
        * latestFetchIsOk: Whether the latest fetch was successful or not
        * dailyPremiumVolume: Daily premium volume of the protocol
        * totalNotionalVolume: Total notional volume of the protocol

    *Endpoint: GET /overview/options, GET /overview/options/{chain}*

    Args:
      exclude_total_data_chart(bool): To exclude aggregated chart
        from response. Defaults to False.

      exclude_total_data_chart_breakdown(bool): To exclude broken
        down chart from response. Defaults to False.

      data(str): Request 'daily' or 'total' volume data.
        Defaults to 'daily'.

      type(str): Request 'premium' or 'notional' volume data.
        Defaults to 'premium'.

      chain(str): Chain slug. Defaults to None.

    Returns:
      Dict[str, any]: Requested data

    """

    excludeTotalDataChartBreakdown = str(exclude_total_data_chart_breakdown).lower()
    excludeTotalDataChart = str(exclude_total_data_chart).lower()
    dataType = f"{data}{type.capitalize()}Volume"

    if chain is None:

        url = f"{BASE_URL}/overview/options?excludeTotalDataChart={excludeTotalDataChart}&excludeTotalDataChartBreakdown={excludeTotalDataChartBreakdown}&dataType={dataType}"
    else:
        url = f"{BASE_URL}/overview/options/{chain}?excludeTotalDataChart={excludeTotalDataChart}&excludeTotalDataChartBreakdown={excludeTotalDataChartBreakdown}&dataType={dataType}"

    return get(url)


def get_options_summary(protocol: str,
                        data: str = "daily",
                        type: str = "premium") -> Dict[str, any]:
    """**Returns summary of an options dex volume with historical data.**

    Function may return the following data:

    * name: Name of the protocol
    * displayName: Protocol name as displayed on DeFiLlama
    * disabled: Whether the protocol is disabled or not
    * logo: 'https://icons.llama.fi/0x.png',
    * address: Protocol address on the blockchain
    * url: Protocol logo URL
    * description: Protocol description
    * audits: List of audits
    * category: Category to which the protocol belongs
    * twitter: Twitter handle of the protocol
    * audit_links: List of audit links
    * gecko_id: CoinGecko ID of the protocol
    * totalDataChart: List of aggregated chart data with their timestamp
    * totalDataChartBreakdown: List of aggregated chart data broken down by
      chains with their timestamp
    * total24h: Total volume collected by the protocol in the
      last 24 hours
    * total48hto24h: Total volume collected by the protocol in the
      last 48 hours to the last 24 hours
    * total14dto7d: Total volume collected by the protocol in the
      last 14 days to the last 7 days
    * totalAllTime: Total volume collected by the protocol since
      the beginning
    * change_1d: Change in the protocol's volume in the last 24 hours
    * module: Name of the protocol as mentioned on adapter API
    * protocolType: Whether its a protocol or a chain
    * chains: List of chains supported by the protocol
    * methodologyURL: URL of the methodology used to calculate the fees
    * latestFetchIsOk: Whether the latest fetch was successful or not
    * childProtocols: Protocols derived from this protocol

    *Endpoint: GET /summary/options/{protocol}*

    Args:
      protocol(str): Protocol name

      data(str): Request 'daily' or 'total' volume data.
        Defaults to 'daily'.

      type(str): Request 'premium' or 'notional' volume data.
        Defaults to 'premium'.

    Returns:
      Dict[str, any]: Requested data

    """

    dataType = f"{data}{type.capitalize()}Volume"

    url = f"{BASE_URL}/summary/options/{protocol}?dataType={dataType}"

    return get(url)
