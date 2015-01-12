#!/usr/bin/env python

import re

from core.common import retrieve_content
from core.common import BLACKLIST

__type__ = (BLACKLIST.IP,)
__url__ = "http://rules.emergingthreats.net/open/suricata/rules/botcc.rules"
__check__ = "CnC Server"
__info__ = "C&C"
__reference__ = "emergingthreats.net"

def fetch():
    retval = dict((_, {}) for _ in __type__)
    content = retrieve_content(__url__)

    if __check__ in content:
        for match in re.finditer(r"\d+\.\d+\.\d+\.\d+", content):
            retval[BLACKLIST.IP][match.group(0)] = (__info__, __reference__)

    return retval