#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess


def png_from_xps(fn, config):
    converter_path = (lambda c: os.path.join(
        c.get('Path'), c.get('Exe')))(config['Converter Path'])
    converter_paras = [(lambda k, v: ('=' if v else '').join((k, v)))(
        k, v) for k, v in config['Converter Paras'].items()]
    pro = subprocess.Popen(' '.join(
        [converter_path, *converter_paras, fn]), stdout=subprocess.PIPE, shell=True)
    return pro.stdout.read()

