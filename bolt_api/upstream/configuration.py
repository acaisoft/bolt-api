import typing

from bolt_api.upstream.base import BaseQuery, InputType


class Configuration(typing.NamedTuple, InputType):
    name: str
    repository_id: str
    project_id: str
    type_id: str


class Query(BaseQuery):
    input_type = Configuration
