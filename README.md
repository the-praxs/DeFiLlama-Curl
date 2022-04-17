# DeFiLlama Python API

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

-------

### Unofficial Python wrapper for the [DeFi Llama API](https://defillama.com/home) using PyCurl module

Inspired from itzmestar's [DeFi Llama](https://github.com/itzmestar/DeFiLlama) Python API.

For detailed information about the API endpoints, see [DeFi Llama API Documentation](https://docs.llama.fi/api)

### Installation:

Use pip to install:

```python
pip install DeFiLlama
```

-----------

### Authentication:

Endpoints are accessible without an API key.

-----------

### Documentation:

To import the package and initialize API client
```python
# Import library
from defillama import defillama

# Client object to interact with DeFi Llama API
llama = DefiLlama()
```

#### TVL : Retrieve TVL data -->

1. **GET/protocols** : List all protocols on defillama along with their TVL.
```python
llama.get_protocols()
```

2. **GET/protocol/{protocol}** : Get historical TVL of a protocol and breakdown by token and chain.
```python
# For e.g. aave
llama.get_protocol(protocol='aave')
```

3. **GET/charts** : Get historical TVL of DeFi on all chains.
```python
llama.get_charts()
```

4. **GET/charts/{chain}** : Get historical TVL of a chain.
Chains can be obtained from **GET/chains** or the chains property on **GET/protocols**.
```python
# For e.g. Ethereum
llama.get_chart(chain='Ethereum')
```

5. **GET/tvl/{protocol}** : Get only protocol TVL as a number.
```python
# For e.g. uniswap
llama.get_tvl_protocol(protocol='uniswap')
```

6. **GET/chains** : Get current TVL of all chains.
```python
llama.get_chains()
```

#### coins : General blockchain data used by DeFi Llama and open-sourced -->

1. **GET/block/{chain}/{timestamp}** : Get the closest block on a timestamp.
Runs binary search over a blockchain's blocks to get the closest one to a timestamp.
Every time this is run DeFi Llama adds new data to their database, so each query permanently speeds up future queries.
```python
# For e.g. Fantom chain for timestamp 1650207158
llama.get_block_timestamp(block='fantom', timestamp=1650207158)
```

2. **POST/prices** : Get current or historical prices of tokens by contract address.
If timestamp is not provided we just return the latest data.
```python
# Sample data JSON
body = {
  "coins": [
    "ethereum:0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
    "avax:0xd586e7f844cea2f87f50152665bcbc2c279d8d70"
  ],
  "timestamp": 1603964988
}

llama.post_prices(data=body)
```