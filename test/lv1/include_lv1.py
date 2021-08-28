import fsimport

include_lv0 = fsimport('../include_lv0')


def get_text():
    return 'text from lv1'


def get_text_lv0():
    return include_lv0.get_text()