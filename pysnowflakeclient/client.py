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

import consts
from connection import Connection

class Client(object):
	"""
    :Parameters:
      - `servers`: list of servers. Each server is a string in the format of host:port (i.e. localhost:30303)
      - `user_agent` (optional): the user_agent to use
      - `socket_timeout` (optional): the socket_timeout in ms
    """
	def __init__(self, servers, user_agent=consts.USER_AGENT, socket_timeout=None):
		if type(servers) == list:
			self._servers = servers
		elif type(servers) == str:
			self._servers = [servers]

		self._server_connections = []

		for s in self._servers:
			p = s.split(":")
			if len(p) == 1:
				c = Connection(p[0], consts.DEFAULT_PORT, user_agent, socket_timeout)
			elif len(p) == 2:
				c = Connection(p[0], int(p[1]), user_agent, socket_timeout)

			self._server_connections.append(c)

	def _get_connection(self):
		return self._server_connections[0]

	def get_id(self):
		return self._get_connection().get_id()

