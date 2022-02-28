# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 12:19:39 2022

@author: Laura.Fiorentino
"""

import pytest
from ssp_fxns import read_ssp


@pytest.fixture
def example_ssp_dict():
    ssp_dict = read_ssp('Sutron.txt')
    return ssp_dict


def test_openfile(example_ssp_dict):
    test_keys = ['AVG_time', 'AVG', 'AVGSDI_time', 'AVGSDI', 'STD_time',
                 'STD', 'STDSDI_time', 'STDSDI', 'CNT_time', 'CNT',
                 'CNTSDI_time', 'CNTSDI', 'OUT_time', 'OUT', 'OUTSDI_time',
                 'OUTSDI']
    assert list(example_ssp_dict.keys()) == test_keys


def test_bad(example_ssp_dict):
    assert example_ssp_dict['AVG'][0] == 'NaN'


def test_good(example_ssp_dict):
    assert example_ssp_dict['OUTSDI'][0] == '0'


def test_timeformat(example_ssp_dict):
    assert example_ssp_dict['AVG_time'][0] == '11/29/2021 14:55:30'
