from services.square_service import SquareService

# But also possible without
mock_square_service = SquareService("Testing Jan")

def test_SquareService():
    got = mock_square_service.square(10)
    want = 100
    assert got == want
