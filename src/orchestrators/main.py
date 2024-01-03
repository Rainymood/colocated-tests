from services.adder_service import AdderServiceInterface
from services.square_service import SquareServiceAInterface

class MainOrchestrator:
    """Orchestrator to signify that this class does nothing on its own.

    The main idea is that MainOrchestrator takes in a bunch of services and then
    runs all the functions associated with those services. It just orchestrates
    things and does nothing on its own.

    At run time we use the production services, at test time we use lightweight
    testing services.
    """

    def __init__(self, adder_service: AdderServiceInterface, square_service: SquareServiceAInterface):
        self.adder_service = adder_service
        self.square_service = square_service

    def orchestrate(self, a, b):
        res = self.adder_service.add(a, b)
        res = self.square_service.square(res)
        return res
