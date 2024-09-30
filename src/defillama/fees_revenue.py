from typing import List, Dict
from ._utils import get

BASE_URL = "https://api.llama.fi"


def get_overview(
    exclude_total_data_chart: bool = False,
    exclude_total_data_chart_breakdown: bool = False,
    data: str = "daily",
    type: str = "fees",
    chain: str = None,
) -> Dict[str, any]:
    """**Returns a list of protocols alongwith summaries of their fees and
    revenue data and fees/revenue historical data.**

    Chain name is optional and if provided, the function returns the data
    for the specified chain only.

    Function returns the following data:

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
        * change_1d: Change in the protocol's fees/revenue in the last 24 hours
        * change_7d: Change in the protocol's fees/revenue in the last 7 days
        * change_1m: Change in the protocol's fees/revenue in the last 30 days
        * change_7dover7d: Change in the protocol's fees/revenue in the last
          7 days over the change in the protocol's fees/revenue in the last
          7 days
        * change_30dover30d: Change in the protocol's fees/revenue in the last
          30 days over the change in the protocol's fees/revenue in the
          last 30 days
        * total24h: Total fees/revenue collected by the protocol in the
          last 24 hours
        * total48hto24h: Total fees/revenue collected by the protocol in the
          last 48 hours to the last 24 hours
        * total7d: Total fees/revenue collected by the protocol in the
          last 7 days
        * total30d: Total fees/revenue collected by the protocol in the
          last 30 days
        * total14dto7d: Total fees/revenue collected by the protocol in the
          last 14 days to the last 7 days
        * total60dto30d: Total fees/revenue collected by the protocol in the
          last 60 days to the last 30 days
        * totalAllTime: Total fees/revenue collected by the protocol since
          the beginning
        * breakdown24h: Total fees/revenue collected by the protocol in the
          last 24 hours broken down by chains
        * chains: List of chains supported by the protocol
        * protocolType: Whether its a protocol or a chain
        * methodologyURL: URL of the methodology used to calculate the fees
        * methodology: Dictionary containing the methodology used to calculate
          the fees
        * parentProtocol: Name of the parent protocol
        * latestFetchIsOk: Whether the latest fetch was successful or not
        * dailyRevenue: Daily revenue of the protocol
        * dailyUserFees: Daily user fees of the protocol
        * dailyHoldersRevenue: Daily holders revenue of the protocol
        * dailyCreatorRevenue: Daily creator revenue of the protocol
        * dailySupplySideRevenue: Daily supply side revenue of the protocol
        * dailyProtocolRevenue: Daily protocol revenue of the protocol
        * dailyFees: Daily fees collected by the protocol
        * totalFees: Totoal fees collected by the protocol
        * totalUserFees: Total user fees collected by the protocol
        * totalRevenue: Total revenue collected by the protocol
        * totalHoldersRevenue: Total holders revenue collected by the protocol
        * totalCreatorRevenue: Total creator revenue collected by the protocol

    * allChains: List of all the chains that are tracked on DeFiLlama
    * total24h: Total fees collected in the last 24 hours
    * total48hto24h: Total fees collected in the last 48 hours to the
    * last 24 hours
    * total7d: Total fees collected in the last 7 days
    * total14dto7d: Total fees collected in the last 14 days to the
      last 7 days
    * total60dto30d: Total fees collected in the last 60 days to the
      last 30 days
    * total30d: Total fees collected in the last 30 days
    * change_1d: Change in the total fees in the last 24 hours
    * change_7d: Change in the total fees in the last 7 days
    * change_1m: Change in the total fees in the last 30 days
    * change_7dover7d: Change in the total fees in the last 7 days over the
    * change in the total fees in the last 7 days
    * change_30dover30d: Change in the total fees in the last 30 days over the
    * change in the total fees in the last 30 days
    * breakdown24h: Total fees collected in the last 24 hours broken down
      by chains
    * dailyRevenue: Daily revenue collected by all the protocols
    * dailyUserFees: Daily user fees collected by all the protocols
    * dailyHoldersRevenue: Daily holders revenue collected by all the protocols
    * dailyCreatorRevenue: Daily creator revenue collected by all the protocols
    * dailySupplySideRevenue: Daily supply side revenue collected by
      all the protocols
    * dailyProtocolRevenue: Daily protocol revenue collected by all
      the protocols

    *Endpoints: GET /overview/fees, GET /overview/fees/{chain}*

    Args:
      exclude_total_data_chart(bool): To exclude aggregated chart
        from response. Defaults to False.

      exclude_total_data_chart_breakdown(bool): To exclude broken
        down chart from response. Defaults to False.

      data(str): Request 'daily' or 'total' data.
        Defaults to 'daily'.

      type(str): Request 'fees' or 'revenue' data.
        Defaults to 'fees'.

      chain(str): Chain slug. Defaults to None.

    Returns:
      Dict[str, any]: Requested data

    """

    excludeTotalDataChart = str(exclude_total_data_chart).lower()
    excludeTotalDataChartBreakdown = str(exclude_total_data_chart_breakdown).lower()
    dataType = f"{data}{type.capitalize()}"

    if chain is None:
        url = f"{BASE_URL}/overview/fees?excludeTotalDataChart={excludeTotalDataChart}&excludeTotalDataChartBreakdown={excludeTotalDataChartBreakdown}&dataType={dataType}"
    else:
        url = f"{BASE_URL}/overview/fees/{chain}?excludeTotalDataChart={excludeTotalDataChart}&excludeTotalDataChartBreakdown={excludeTotalDataChartBreakdown}&dataType={dataType}"

    return get(url)


def get_summary(
    protocol: str, data: str = "daily", type: str = "fees"
) -> Dict[str, any]:
    """**Returns a summary of the fees/revenue collected by a protocol with
    historical data.**

    Function may return the following data:

    * id: Protocol ID
    * name: Protocol name
    * url: Protocol URL
    * description: Protocol description
    * logo: Protocol logo URL
    * chains: List of chains supported by the protocol
    * gecko_id: CoinGecko ID of the protocol
    * cmcId: CoinMarketCap ID of the protocol
    * twitter: Twitter handle of the protocol
    * governanceID: Governance ID of the protocol
    * displayName: Protocol name as displayed on DeFiLlama
    * total24h: Total fees/revenue collected by the protocol in the
      last 24 hours
    * totalAllTime: Total fees/revenue collected by the protocol
      since the beginning
    * latestFetchIsOk: Whether the latest fetch was successful or not
    * disabled: Whether the protocol is disabled or not
    * change_1d: Change in the total fees/revenue in the last 24 hours
    * methodologyURL: URL of the methodology used to calculate the fees
    * module: Name of the protocol as mentioned on adapter API
    * totalDataChart: List of aggregated chart data with their timestamp.
      This data is only available for total data
    * totalDataChartBreakdown: List of aggregated chart data broken down by
      chains with their timestamp. This data is only available for total data
      childProtocols: Protocols derived from this protocol

    *Endpoint: GET /summary/fees/{protocol}*

    Args:
      protocol(str): Protocol slug

      data(str): Request 'daily' or 'total' data.
        Defaults to 'daily'.

      type(str): Request 'fees' or 'revenue' data.
        Defaults to 'fees'.

    Returns:
      Dict[str, any]: Requested data

    """

    dataType = f"{data}{type.capitalize()}"

    url = f"{BASE_URL}/summary/fees/{protocol}?dataType={dataType}"

    return get(url)
