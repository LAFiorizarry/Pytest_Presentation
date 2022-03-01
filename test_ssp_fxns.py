# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 12:19:39 2022

@author: Laura.Fiorentino
"""

import csv
import pytest
from ssp_fxns import read_ssp, write_csv


@pytest.fixture
def example_ssp_dict():
    ssp_dict = read_ssp('Sutron.txt')
    return ssp_dict


@pytest.fixture
def example_keys():
    example_keys = ['AVG_time', 'AVG', 'AVGSDI_time', 'AVGSDI', 'STD_time',
                    'STD', 'STDSDI_time', 'STDSDI', 'CNT_time', 'CNT',
                    'CNTSDI_time', 'CNTSDI', 'OUT_time', 'OUT', 'OUTSDI_time',
                    'OUTSDI']
    return example_keys


def test_openfile(example_ssp_dict, example_keys):
    assert list(example_ssp_dict.keys()) == example_keys


def test_bad(example_ssp_dict):
    assert example_ssp_dict['AVG'][0] == 'NaN'


def test_good(example_ssp_dict):
    assert example_ssp_dict['OUTSDI'][0] == '0'


def test_timeformat(example_ssp_dict):
    assert example_ssp_dict['AVG_time'][0] == '11/29/2021 14:55:30'


def test_writecsv(example_ssp_dict, example_keys, tmpdir):
    filename = tmpdir.join("temp_csv")
    write_csv(example_ssp_dict, filename)
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        r1 = next(csv_reader)
        r2 = next(csv_reader)
        assert r1 == example_keys
        assert r2[0] == '11/29/2021 14:55:30'
        assert r2[1] == 'NaN'
        assert r2[9] == '0'