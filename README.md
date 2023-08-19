# DeFiLlama Python API

![Python](https://img.shields.io/pypi/pyversions/DeFiLlama-Curl?style=flat-square)
[![Conda](https://img.shields.io/conda/v/conda-forge/defillama-curl)](https://anaconda.org/conda-forge/defillama-curl)
![Platforms](https://anaconda.org/conda-forge/defillama-curl/badges/platforms.svg)
![Conda Downloads](https://anaconda.org/conda-forge/defillama-curl/badges/downloads.svg)
![Last Updated](https://anaconda.org/conda-forge/defillama-curl/badges/latest_release_date.svg)

[![PyPi](https://img.shields.io/pypi/v/DeFiLlama-Curl)](https://pypi.org/project/DeFiLlama-Curl/)
[![Wheel](https://img.shields.io/pypi/wheel/DeFiLlama-Curl)](https://github.com/the-praxs/DeFiLlama-Curl/releases)
[![PyPi Downloads](https://static.pepy.tech/badge/defillama-curl)](https://pepy.tech/project/defillama-curl)
[![Documentation Status](https://readthedocs.org/projects/defillama-curl/badge/?version=latest)](https://defillama-curl.readthedocs.io/en/latest/?badge=latest)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

-------

### Unofficial Python 3 wrapper for the [DeFiLlama](https://defillama.com/home) API using the fantastic [PyCurl](http://pycurl.io/) module

Built from the ground up to be fast, reliable and easy to use.

For detailed information about the API endpoints, see DeFiLlama API [Documentation](https://defillama.com/docs/api)

### Installation:

Use either [pip](https://pypi.org/project/DeFiLlama-Curl/) or [conda](https://anaconda.org/conda-forge/defillama-curl) to install:

```python
pip install DeFiLlama-Curl
```
```python
conda install -c conda-forge defillama-curl
```

-----------

### Authentication:

Endpoints are accessible without requiring any API key.

-----------

### Documentation:

Extensive documentation is available [here.](http://defillama-curl.readthedocs.io/)

-----------

### Debugging

If you receive this error after importing the library, the solution can be found [here.](https://stackoverflow.com/questions/47888757/importerror-pycurl-libcurl-link-time-ssl-backend-openssl-is-different-from-c/74173308#74173308) (Credits to [imrane](https://github.com/imrane))

```python
ImportError: pycurl: libcurl link-time ssl backends (secure-transport, openssl) do not include compile-time ssl backend (none/other)
```
