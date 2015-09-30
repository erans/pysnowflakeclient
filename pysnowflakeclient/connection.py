#!/bin/env python
#
# Copyright 2011 Eran Sandler <eran@sandler.co.il>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import os
import sys

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
try:
	from thrift.protocol import TBinaryProtocolAccelerated as TBinaryProtocol
except ImportError:
	from thrift.protocol import TBinaryProtocol

# Small hack to avoid the need to set PYTHONPATH environment variable
#sys.path.append(os.path.join(os.path.dirname(__file__), "thrift", "gen-py"))

from Snowflake import Snowflake
from Snowflake.ttypes import *
from Snowflake.constants import *

import consts

class Connection(object):
	def __init__(self, host, port=30303, user_agent=consts.USER_AGENT, socket_timeout=None):
		self._host = host
		self._port = port
		self._user_agent = user_agent

		self._transport = TSocket.TSocket(host, port)
		self._transport.setTimeout(socket_timeout)
		print 'socket_timeout is', socket_timeout
		self._transport = TTransport.TFramedTransport(self._transport)
		self._protocol = TBinaryProtocol.TBinaryProtocol(self._transport)
		self._client = Snowflake.Client(self._protocol)
		self._transport.open()

	def get_id(self):
		return self._client.get_id(self._user_agent)


