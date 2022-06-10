# Copyright (C) 2012-2018 The python-bitcoinlib developers
#
# This file is part of python-bitcoinlib.
#
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution.
#
# No part of python-bitcoinlib, including this file, may be copied, modified,
# propagated, or distributed except according to the terms contained in the
# LICENSE file.


import safe.core

# Note that setup.py can break if __init__.py imports any external
# dependencies, as these might not be installed when setup.py runs. In this
# case __version__ could be moved to a separate version.py and imported here.
__version__ = '0.11.1dev'

class MainParams(safe.core.CoreMainParams):
    MESSAGE_START = b'\x62\x69\x6e\xcc'
    DEFAULT_PORT = 5555
    RPC_PORT = 5554
    DNS_SEEDS = (('120.78.227.96', '114.215.31.37'),
                 ('47.95.23.220', '47.96.254.235'),
                 ('106.14.66.206', '47.52.9.168'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':76,
                       'SCRIPT_ADDR':16,
                       'SECRET_KEY' :204}
    BECH32_HRP = 'bc'

"""Master global setting for what chain params we're using.

However, don't set this directly, use SelectParams() instead so as to set the
safe.core.params correctly too.
"""
#params = safe.core.coreparams = MainParams()
params = MainParams()

def SelectParams(name):
    """Select the chain parameters to use

    name is one of 'mainnet', 'testnet', or 'regtest'

    Default chain is 'mainnet'
    """
    global params
    safe.core._SelectCoreParams(name)
    if name == 'mainnet':
        params = safe.core.coreparams = MainParams()
    else:
        raise ValueError('Unknown chain %r' % name)
