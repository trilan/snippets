import argparse
import sys

from .generator import Generator
from .repository import Repository
from .settings import get_settings, get_settings_from_file


def run(args=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--settings')
    parser.add_argument('-r', '--repository')
    parser.add_argument('-o', '--output')
    parser.add_argument('-t', '--theme')
    args = parser.parse_args(args)

    if args.settings is not None:
        settings = get_settings_from_file(args.settings)
    else:
        settings = get_settings({})

    if args.repository is not None:
        settings['REPOSITORY_PATH'] = args.repository
    if args.output is not None:
        settings['OUTPUT_PATH'] = args.output
    if args.theme is not None:
        settings['THEME'] = args.theme

    repository = Repository()
    repository.add_repopath(settings['REPOSITORY_PATH'])
    generator = Generator(repository, settings['THEME'], settings.copy())
    generator.generate(settings['OUTPUT_PATH'])


if __name__ == '__main__':
    run()
