"""DeFiLlama-Curl is a Python wrapper for the DeFiLlama API built using the
   fantastic PyCurl module.

   The DeFiLlama API is a free, open-source API that provides access to DeFi
   data. It is maintained by DeFiLlama.com, a DeFi data aggregator. This
   Python wrapper is developed to prvoide access to those API requests in a
   simple and easy to use manner.

   This API contains the following submodules:
   - abi-decoder: Function and event signatures decoded
   - bridges: Data from DeFiLlama's bridges dashboard
   - coins: General blockchain data used by DeFiLlama
   - fees and revenue: Data from DeFiLlama's fees and revenue dashboard
   - stablecoins: Data from DeFiLlama's stablecoins dashboard
   - tvl: Retrieve TVL data
   - volumes: Data from DeFiLlama's volumes dashboards
   - yields: Data from DeFiLlama's yields/APY dashboard
"""

__all__ = ['__version__', '_utils', 'tvl', 'coins', 'stablecoins', 'yields',
           'abi_decoder', 'bridges', 'volumes', 'fees_revenue']
