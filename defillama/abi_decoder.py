from typing import List, Dict
from ._utils import get, arg_parser

BASE_URL = "https://abi-decoder.llama.fi"


def get_signature_abi(func_sign: List,
                      events_sign: List = None) -> Dict[str, Dict[str, any]]:
    """**Returns the Application Binary Interface for a function
    or event signature.**

    *Endpoint: GET /fetch/signature*

    Args:
      func_sign(List): List of function signatures from the first 4 bytes
        of the Keccak-256 hash

      events_sign(List): List of event signatures

    Returns:
      Dict[str, Dict[str, any]]: Requested data

    """

    func_sign = arg_parser(func_sign, format='list')

    if events_sign is None:
        url = f"{BASE_URL}/fetch/signature?functions={func_sign}"
    else:
        events_sign = arg_parser(events_sign, format='list')
        url = f"{BASE_URL}/fetch/signature?functions={func_sign}&events={events_sign}"

    return get(url)


def get_contract_signature_abi(chain: str,
                               address: str,
                               func_sign: List,
                               events_sign: List = None) -> Dict[str, Dict[str, any]]:
    """**Returns the verbose Application Binary Interface for a function or
    event signature for a particular contract.**

    *Endpoint: GET /fetch/contract/{chain}/{address}*

    Args:
      chain(str): Chain the smart contract is located on. Can be either
        'arbitrum', 'avalanche', 'bsc', 'celo', 'ethereum', 'fantom',
        'optimism', 'polygon', 'tron', 'xdai', 'heco'

      address(str): Address of the smart contract

      func_sign(List): List of function signatures from the first 4 bytes
        of the Keccak-256 hash

      events_sign(List): List of event signatures

    Returns:
      Dict[str, Dict[str, any]]: Requested data

    """

    func_sign = arg_parser(func_sign, format='list')

    if events_sign is None:
        url = f"{BASE_URL}/fetch/contract/{chain}/{address}?functions={func_sign}"
    else:
        events_sign = arg_parser(events_sign, format='list')
        url = f"{BASE_URL}/fetch/contract/{chain}/{address}?functions={func_sign}&events={events_sign}"

    return get(url)
