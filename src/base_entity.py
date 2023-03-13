import abc
import json

from .constants import EntityTypes


class BaseEntity(abc.ABC):
    def __init__(self, entity_type: EntityTypes):
        self.type = entity_type

    def to_geojson(self) -> dict:
        raise NotImplementedError()

    def __str__(self) -> str:
        return json.dumps(self.to_geojson())
