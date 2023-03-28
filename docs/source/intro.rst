Introduction
============

``defillama-curl`` is a high-level Python package which aims to provide a Python wrapper for the `DeFiLlama <https://defillama.com/docs/api/>`_ API using the fantastic `PyCurl <http://pycurl.io/>`_ module.

The aim here was to define a single package that can be used to access all the data provided by the DeFiLlama API, without having to worry about the underlying HTTP requests and responses.

The current implementation has been developed in Python 3 on a Windows-based machine but the package is itself OS independent and can be run on any machine that supports Python 3.6+ and PyCurl.

Motivation
**********

As a developer looking to source data from different APIs om the internet, it was a fantastic opportunity to learn how to use the PyCurl module and develop and publish a Python package along with its documentation to ease the work for other developers

This package is intended to provide all the functions of the DeFiLlama API in the Python programming language with the power of the cURL module using PyCurl for simulatneous HTTP requests.

Limitations
***********

- The package is supposed to interact with the API as-is and hence the data is returned in the same format as it is provided by the API. This means that the user is expected to parse the data as per their requirements.

- The documentation provides information about the data fields returned but due to lack of information on the internet, some fields do not have any description.

Installation
************

The package is published on `PyPi <https://pypi.org/project/DeFiLlama-Curl/>`_ and `Anaconda <>`_. To install the module, simply run the following command in the terminal:

``pip install DeFiLlama-Curl``

or

``conda install -c anaconda defillama-curl``