#! ignore this line
# pylint: disable=redefined-builtin

from . import Testme

def setUp():
    Testme.globals = {}  # pylint: disable=redefined-builtin
