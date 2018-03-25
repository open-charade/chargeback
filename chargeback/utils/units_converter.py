# Units converter

import math
import re

# Symbols Prefix

SYMBOLS = ["b","B","Hz","bps","Bps"]

# SI PREFIX

SI_PREFIX = {
    "": {
        "name": "",
        "value" :1
    },
    "K": {
        "name": "kilo",
        "value": math.pow(10, 3)
     },
    "M": {
        "name": "mega",
        "value": math.pow(10, 6)
    },
    "G": {
        "name": "giga",
        "value": math.pow(10, 9)
    },
    "T": {
        "name": "tera",
        "value": math.pow(10, 12)
    },
    "P": {
        "name": "peta",
        "value": math.pow(10, 15)
    },
    "E": {
        "name": "exa",
        "value": math.pow(10, 18)
    },
    "d": {
        "name": "deci",
        "value": 1/10
    },
    "c": {
        "name": "centi",
        "value": 1/100
    },
    "m": {
        "name": "milli",
        "value": 1/math.pow(10, 3)
    },
    "µ": {
        "name": "micro",
        "value": 1/math.pow(10, 6)
    },
    "n": {
        "name": "nano",
        "value": 1/math.pow(10, 9)
    },
    "p": {
        "name": "pico",
        "value": 1/math.pow(10, 12)
    }
}

BINARY_PREFIX = {
    "": {
        "name": "",
        "value": 1
    },
    "Ki": {
        "name": "kibi",
        "value": 1024
    },
    "Mi": {
        "name": "mebi",
        "value": math.pow(1024, 2)
    },
    "Gi": {
        "name": "gibi",
        "value": math.pow(1024, 3)
    },
    "Ti": {
        "name": "tebi",
        "value": math.pow(1024, 4)
    },
    "Pi": {
        "name": "pebi",
        "value": math.pow(1024, 5)
    },
    "Ei": {
        "name": "exbi",
        "value": math.pow(1024, 6)
    }
}

ALL_PREFIXES =  dict(BINARY_PREFIX, **SI_PREFIX)

def to_unit(value, unit = '', destination_unit = '', prefix_type = 'ALL_PREFIXES'):
  # It returns the value converted to the new unit
  prefix = extract_prefix(unit)
  destination_prefix = extract_prefix(destination_unit)
  prefix_distance = distance(prefix, destination_prefix, prefix_type)
  if prefix_distance is None:
      return None
  return (float(value) * float(prefix_distance))

def extract_prefix(unit):
  prefix = None

  if unit is None:
      return ''

  for key in SYMBOLS:
    match = re.search('^(.*).*(' + key + ')\Z', unit)
    prefix = match.groups()[0] if match is not None else None
    if prefix is not None:
      break

  if prefix is not None:
    return prefix

  return unit

def distance(prefix, other_prefix = '', prefix_type = 'ALL_PREFIXES'):
  # Returns the distance and whether you need to divide or multiply
  # Check that the list of conversions exists or use the International Sistem SI
  if type(prefix_type) == dict:
      list = prefix_type
  elif type(prefix_type) == str:
      list = vars()[prefix_type] if prefix_type in vars() else ALL_PREFIXES
  else:
    return None

  # If I can't find the prefixes in the list:
  # If they are the same, return 1
  # If they are different (i.e. "cores" vs "none", return nil)
  if prefix == other_prefix:
      return 1
  if prefix not in list or other_prefix not in list:
     return None

  # Find the prefix name, value pair in the list
  orig = list[prefix]
  dest = list[other_prefix]

  return orig['value'] / dest['value']
