#!/usr/bin/env python
# encoding: utf-8
"""
Created by Sean Nelson on 2009-09-20.
Copyright 2009 Sean Nelson <audiohacked@gmail.com>

This file is part of pyBusPirate.

pyBusPirate is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pyBusPirate is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with pyBusPirate.  If not, see <http://www.gnu.org/licenses/>.
"""

class MacrosRaw2Wire:
	pass
	""" ISO 7813-3 ATR for smart cards, parses reply bytes. """
	def ATR_SmartCards(self):
		self.ExecMacro(1)
	""" ISO 7813-3 parse only (provide your own ATR command). """
	def ATR(self):
		self.ExecMacro(2)

class Raw2Wire:
	pass