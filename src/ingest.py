from gzip import GzipFile
import json
from os import path

import click
from redis.commands.search.field import TextField, NumericField
from redis.commands.search.indexDefinition import IndexDefinition
from redis.exceptions import ResponseError

from clients import REDIS

def source(filename: str) -> GzipFile:
    if not path.exists(filename):
        raise FileNotFoundError(f"file {filename} not found")

    return GzipFile(filename, 'rb')


def ensure_types(line: dict) -> dict:
    ret = {}
    for k, v in line.items():
        if isinstance(v, bool):
            v = int(v)

        ret[k] = v

    return ret


def insert(filetype: str, pointer: GzipFile) -> bool:
    try:
        for line in pointer:
            _line = json.loads(line)
            if 'adult' in _line and _line['adult']:
                continue

            if '_' in filetype:
                _, filetype = filetype.split('_')

            _name = f"{filetype}:{_line['id']}"
            _mapping = ensure_types(_line)
            _mapping['type'] = filetype
            REDIS.hset(name=_name, mapping=_mapping)

        return True
    except Exception as _err:
        print(_err)

    return False


def create_index(filetype: str):
    if '_' in filetype:
        _, filetype = filetype.split('_')

    indexable_columns = {
        "movie": "original_title",
        "person": "name",
        "series": "original_name"
    }
    schema = (
        TextField(indexable_columns[filetype], sortable=True),
    )
    try:
        REDIS.ft(f"idx:{filetype}").create_index(schema, definition=IndexDefinition(prefix=[f"{filetype}:"]))
    except ResponseError:
        pass

    return


@click.command()
@click.option("--records/--no-records", default=True, help="ingest TMDb records")
@click.option("--index/--no-index", default=True, help="create Redis searchable indexes")
def run(records, index):
    for filetype in ['movie', 'person', 'tv_series']:
        if records == 1:
            print(f"Importing {filetype}")
            filename = f"{filetype}_ids_09_03_2023.json.gz"
            filepointer = source(filename)
            insert(filetype, filepointer)
            print("- Done...")

        if index == 1:
            print("Creating search index")
            create_index(filetype)
            print("- Done...")


if __name__ == '__main__':
    run()
