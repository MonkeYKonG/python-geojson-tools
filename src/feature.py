from typing import Union

from . import errors
from .base_entity import BaseEntity
from .constants import EntityTypes
from .geometries import BaseGeometry
from .geometry_tools import load_geometry


class Feature(BaseEntity):
    def __init__(self, geometry: Union[dict, BaseGeometry], properties: dict = None):
        super().__init__(EntityTypes.feature)
        if properties is None:
            properties = dict()
        self.properties = properties
        self.geometry = geometry if isinstance(geometry, BaseGeometry) else load_geometry(geometry)

    @classmethod
    def from_dict(cls, obj: dict):
        if obj.get('type') != EntityTypes.feature.value:
            raise ValueError(errors.UNKNOWN_TYPE)
        obj_geometry = obj.get('geometry')
        obj_properties = obj.get('properties')
        return cls(obj_geometry, obj_properties)

    def to_geojson(self) -> dict:
        return {
            'type': self.type,
            'properties': self.properties,
            'geometry': self.geometry.to_geojson()
        }
