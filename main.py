#!/usr/bin/env python
import sys
import eyed3
import re
from datetime import datetime


def fix_meta(file_name: str):
    print(f'Adjusting meta for file: {file_name}', file=sys.stderr)
    audio_file = eyed3.load(file_name)
    tag = audio_file.tag
    tag.album = f'BIS Radio Show {mix_date(file_name)}'

    print(f'-->  {tag.album} - {tag.title} ({tag.artist})', file=sys.stderr)
    audio_file.tag.save(version=(2, 3, 0))


def mix_date(file_name: str):
    match = re.search(r'bis-([0-9\-]*)-', file_name)
    formatted_date = datetime.strptime(match.group(1), '%m-%d-%y').strftime('%d.%m.%Y')
    return formatted_date


if __name__ == '__main__':
    for mp3_file in sys.argv[1:]:
        fix_meta(mp3_file)
