import typing
from schema.upstream.base import BaseQuery, InputType


class Conf(typing.NamedTuple, InputType):
    name: str
    repository_id: str
    project_id: str


class Query(BaseQuery):
    input_type = Conf
