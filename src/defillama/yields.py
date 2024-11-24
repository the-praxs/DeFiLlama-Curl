from typing import List, Dict
from ._utils import get

BASE_URL = "https://yields.llama.fi"


def get_pools() -> List[Dict[str, any]]:
    """**Returns the latest data for all pools.**

    Function returns the following data:

    * chain: Name of the chain the pool is on
    * project: Protocol name
    * symbol: Symbol of the pool
    * tvlUsd: Current TVL in USD in the pool
    * apyBase: Annual Percent Yield from pool fees/supplying in %
    * apyReward: Annual Percent Yield from pool LM rewards in %
    * apy: Current Annual Percent Yield of the pool
    * rewardTokens: Reward token addresses
    * pool: Pool ID
    * apyPct1D: % change in Annual Percent Yield within 24 hours
    * apyPct7D: % change in Annual Percent Yield within 7 days
    * apyPct30D: % change in Annual Percent Yield within 30 days
    * stablecoin: Stablecoins in the pool
    * ilRisk: Whether Impermanent Loss Risk is associated with the pool
    * exposure: 'Single' or 'Multi' token exposure to the pool
    * predictions: Dictionary contating the 'predictedClass',
      'predictedProbability' and 'binnedConfidence' of the pool
    * poolMeta: Wrapped tokens in the pool
    * mu: Mean APY of the pool
    * sigma: Standard Deviation of the APY of the pool
    * count: Number of tokens in the pool
    * outlier: ???
    * underlyingTokens: Underlying token addresses from a pool
    * il7d: Impermanent Loss within 7 days
    * apyBase7d: Annual Percent Yield from pool fees/supplying in %
      within 7 days
    * apyMean30d: Mean Annual Percent Yield of the pool within 30 days
    * volumeUsd1d: Volume in USD within 24 hours of the tokens in the pool
    * volumeUsd7d: Volume in USD within 7 days of the tokens in the pool
    * apyBaseInception: ???

    *Endpoint: GET /pools*

    Returns:
      List[Dict[str, any]]: Requested data

    """

    url = f"{BASE_URL}/pools"

    return get(url)['data']


def get_pool_chart(pool: str) -> List[Dict[str, any]]:
    """**Returns the historical APY and TVL data for a pool.**

    Function returns the following data:

    * timestamp: Timestmap of the data
    * tvlUsd: Current TVL in USD in the pool
    * apy: Annual Percent Yield of the pool
    * apyBase: Annual Percent Yield from pool fees/supplying in %
    * apyReward: Annual Percent Yield from pool LM rewards in %
    * il7d: Impermanent Loss within 7 days
    * apyBase7d: Annual Percent Yield from pool fees/supplying in %
      within 7 days

    *Endpoint: GET /chart/{pool}*

    Args:
      pool(str): Pool ID.

    Returns:
      List[Dict[str, any]]: Requested data

    """

    url = f"{BASE_URL}/chart/{pool}"

    return get(url)['data']
