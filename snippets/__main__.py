import argparse
import sys

from .generator import Generator
from .repository import Repository


def run(args=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    parser.add_argument('-o', '--output', default='output')
    parser.add_argument('-t', '--theme')
    args = parser.parse_args(args)

    repository = Repository()
    repository.add_repopath(args.path)
    generator = Generator(repository, args.theme)
    generator.generate(args.output)


if __name__ == '__main__':
    run()
