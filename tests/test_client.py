from rdsmon import Client

def test_client():
    assert Client() is not None