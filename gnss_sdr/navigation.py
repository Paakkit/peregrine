#!/usr/bin/python
#--------------------------------------------------------------------------
#                           SoftGNSS v3.0
# 
# Copyright (C) Darius Plausinaitis and Dennis M. Akos
# Written by Darius Plausinaitis and Dennis M. Akos
# Converted to Python by Colin Beighley
#--------------------------------------------------------------------------
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301,
#USA.
#--------------------------------------------------------------------------
import numpy as np
from findPreambles import findPreambles
from ephemeris import ephemeris
import corrs2bits

def navigation(trackResults, settings):
  numGoodSats = 0
  for i in range(len(trackResults)):
    if (trackResults[i].status == 'T'):
      numGoodSats = numGoodSats + 1
  if (numGoodSats >= 4):
    Exception('Too few satellites to calculate nav solution')
  if (len(trackResults) < 36000):
    Exception('Length of tracking too short to calculate nav solution')

  (subFrameStart, activeChnList) = findPreambles(trackResults,settings)

  eph = [[] for i in range(32)]
#  eph = [i for i in range(32)]
  for channelNr in activeChnList:
    navBits = corrs2bits.unsigned(trackResults[channelNr].I_P[subFrameStart[channelNr]-20:subFrameStart[channelNr] + (1500*20)])
#    (eph[trackResults[channelNr].PRN], TOW) = ephemeris(navBits[])

  (navSolutions, eph) = (0,0)
  return (navSolutions, eph)