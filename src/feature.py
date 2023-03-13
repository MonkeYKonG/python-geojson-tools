from .base_entity import BaseEntity
from .constants import EntityTypes


class Feature(BaseEntity):
    def __init__(self, geometry, properties: dict = None):
        super().__init__(EntityTypes.feature)
        if properties is None:
            properties = dict()
        self.properties = properties
        self.geometry = geometry

    def to_geojson(self) -> dict:
        return {
            'type': self.type,
            'properties': self.properties,
            'geometry': self.geometry.to_geojson
        }
