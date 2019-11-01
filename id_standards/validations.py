import os

from typing import (
    Union
)

from io import IOBase

from os.path import (
    exists,
    join,
)

from functools import (
    partial
)

from fnc import (
    map as mapF,
)

from . import validator

def validate_on_schema(schema_version, f):
    schema_file = os.path.join(os.path.dirname(__file__), '..', 'schema', schema_version, 'schema.rng')
    return validate_one(schema_file, f)

def validate_one(schema_file, f:Union[IOBase, str]):
    validator.set_schema(schema_file)
    return [validator.validate(f), validator.errors()]

def validate_many(schema_file, fs):
    validate_on_schema = partial(validate_one, schema_file)
    return mapF(validate_on_schema, fs)