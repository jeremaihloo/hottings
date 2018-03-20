import os

from hottings.monitors import HottingMonitor


def test_parse():
    monitor = HottingMonitor.parse(os.path.dirname(__file__))
    assert monitor.version
