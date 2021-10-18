#!/usr/bin/env python
import sys
import click
import eyed3
import re
from datetime import datetime


def fix_meta(file_name: str):
    click.secho(f'Setting meta for file: {file_name}', fg="blue")
    audio_file = eyed3.load(file_name)
    tag = audio_file.tag
    tag.album = f'BIS Radio Show {mix_date(file_name)}'

    click.secho(f'-->  {tag.album} - {tag.title} ({tag.artist})', fg="green")
    audio_file.tag.save(version=(2, 3, 0))


def mix_date(file_name: str):
    match = re.search(r'bis-([0-9\-]*)-', file_name)
    formatted_date = datetime.strptime(match.group(1), '%m-%d-%y').strftime('%d.%m.%Y')
    return formatted_date


@click.command()
@click.argument('files', nargs=-1, type=click.Path(exists=True))
def main(files):
    for mp3_file in files:
        fix_meta(mp3_file)


if __name__ == '__main__':
    main()
