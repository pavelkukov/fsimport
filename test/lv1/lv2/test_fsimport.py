import fsimport
import pytest

include_lv0 = fsimport('../../include_lv0')
include_lv1 = fsimport('../include_lv1')
include_lv2 = fsimport('./include_lv2')
include_lv3 = fsimport('./lv3/include_lv3')


def test_include_lv0():
    assert hasattr(include_lv0, 'get_text') == True
    assert include_lv0.get_text() == 'text from lv0'


def test_include_lv1():
    assert hasattr(include_lv1, 'get_text') == True
    assert include_lv1.get_text() == 'text from lv1'


def test_include_lv0_from_lv1():
    assert hasattr(include_lv1, 'get_text_lv0') == True
    assert include_lv1.get_text_lv0() == 'text from lv0'


def test_include_lv2():
    assert hasattr(include_lv2, 'get_text') == True
    assert include_lv2.get_text() == 'text from lv2'


def test_include_lv3():
    assert hasattr(include_lv3, 'get_text') == True
    assert include_lv3.get_text() == 'text from lv3'


def test_fail_import():
    with pytest.raises(Exception, match=r"cannot find file.*"):
        fsimport('./lv3/the_fail_import')
