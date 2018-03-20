from hottings.monitors import HottingMonitor


def test_parse():
    monitor = HottingMonitor.parse()
    assert monitor.version
