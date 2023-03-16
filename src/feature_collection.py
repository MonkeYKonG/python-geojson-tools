from typing import Union

from . import errors
from .base_entity import BaseEntity
from .constants import EntityTypes
from .feature import Feature
from .geometries import BaseGeometry


class FeatureCollection(BaseEntity):
    def __init__(self, features: list):
        super().__init__(EntityTypes.feature_collection)
        self.features = [
            feature if isinstance(feature, Feature) else Feature.from_dict(feature)
            for feature in features
        ]

    @classmethod
    def from_dict(cls, obj: dict):
        if obj.get('type') != EntityTypes.feature_collection.value:
            raise ValueError(errors.UNKNOWN_TYPE)
        obj_features = obj.get('features')
        return cls(obj_features)

    def to_geojson(self) -> dict:
        return {
            'type': self.type,
            'features': [feature.to_geojson() for feature in self.features]
        }

    def merge_features(self):
        """Merge all features together then return Feature with"""
        pass

    def append(self, entity: BaseEntity):
        """Add entity to features"""
        if isinstance(entity, FeatureCollection):
            self.features += entity.features
        elif isinstance(entity, Feature):
            self.features.append(entity)
        elif isinstance(entity, BaseGeometry):
            self.features.append(Feature(entity))
        return self

    def delete(self, index):
        """Remove feature at index"""
        self.features.pop(index)

    def __add__(self, other: BaseEntity):
        return self.append(other)

    def __iter__(self):
        return self.features
