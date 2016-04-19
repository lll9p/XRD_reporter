#!/usr/bin/env python
# -*- coding: utf-8 -*-
def try_float(s):
    try:
        result = float(s)
    except:
        result = s
    return result
