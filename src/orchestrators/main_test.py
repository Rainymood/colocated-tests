from services.adder_service import AdderService
from services.square_service import SquareService
from orchestrators.main import MainOrchestrator


# In this test file we can create lightweight objects like a test_adder and a
# test_squarer and run the orchestrator with them.
test_adder = AdderService("Test adder")
test_squarer = SquareService("Test squarer")

def test_main_orchestrator(fake_args):
    # Note that this test is completely separate from any entrypoint or outside
    # influence, this is all internal domain models. If you look in `cli.py`
    # that's where you can find how we interact with the orchestrator from the
    # cli.
    o = MainOrchestrator(test_adder, test_squarer)
    a,b = fake_args
    o.orchestrate(a,b)
