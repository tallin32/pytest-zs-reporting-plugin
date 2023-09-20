# -*- coding: utf-8 -*-

import pytest
from pytest import StashKey, Stash
from custom_format import testcase

def pytest_addoption(parser):
    group = parser.getgroup('zs-reporting-plugin')
    group.addoption(
        '--foo',
        action='store',
        dest='dest_foo',
        default='2023',
        help='Set the value for the fixture "bar".'
    )

    parser.addini('HELLO', 'Dummy pytest.ini setting')


@pytest.fixture
def bar(request):
    return request.config.option.dest_foo
