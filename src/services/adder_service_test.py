


# It's possible to do this with fixtures
def test_AdderService(mock_adder_service):
    got = mock_adder_service.add(1,1)
    want = 2
    assert got == want
