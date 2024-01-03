import argparse
import sys
from orchestrators.main import MainOrchestrator
from services.adder_service import AdderService
from services.square_service import SquareService
import time

def parse_args(args):
    parser = argparse.ArgumentParser(description='Add two integers.')
    parser.add_argument('a', type=int, help='First integer')
    parser.add_argument('b', type=int, help='Second integer')
    return parser.parse_args(args)

def cli_adapter(args):
    # This CLI adapter then gives us *another* way of interacting with the
    # MainOrchestrator. The CLI adapter creates some production services and
    # injects them into the service. Then we call the orchestration method.
    a = args.a
    b = args.b

    print(f"Running from CLI adapter with a={b} and b={b}")
    print(f"Simulating production run. Sleeping for 5 seconds.")
    time.sleep(5)

    adder = AdderService("PRODUCTION adder")
    squarer = SquareService("PRODUCTION squarer")
    o = MainOrchestrator(adder, squarer)
    res = o.orchestrate(a,b)

    return res

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    cli_adapter(args)