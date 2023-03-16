import abc
import json

from .constants import EntityTypes


class BaseEntity(abc.ABC):
    def __init__(self, entity_type: EntityTypes):
        self.type = entity_type.value

    @classmethod
    def from_dict(cls, obj: dict):
        raise NotImplementedError()

    @classmethod
    def from_string(cls, string: str):
        obj = json.loads(string)
        return cls.from_dict(obj)

    @classmethod
    def from_file(cls, path: str):
        with open(path) as file:
            obj = json.load(file)
        return cls.from_dict(obj)

    def to_geojson(self) -> dict:
        raise NotImplementedError()

    def __str__(self) -> str:
        return json.dumps(self.to_geojson())
