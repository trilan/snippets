import argparse
import sys

from .generator import Generator
from .repository import Repository


def run(args=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--repository', default='snippets')
    parser.add_argument('-o', '--output', default='output')
    parser.add_argument('-t', '--theme')
    args = parser.parse_args(args)

    repository = Repository()
    repository.add_repopath(args.repository)
    generator = Generator(repository, args.theme)
    generator.generate(args.output)


if __name__ == '__main__':
    run()
