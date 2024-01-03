
from argparse import Namespace
from entrypoint.cli import cli_adapter

def test_parse_args():
    assert 1

def test_cli_adapter(fake_args):
    a,b = fake_args
    args = Namespace(a=a, b=b)
    got = cli_adapter(args)
    want = 9
    assert got == want

