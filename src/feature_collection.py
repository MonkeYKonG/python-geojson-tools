from . import errors
from .base_entity import BaseEntity
from .constants import EntityTypes
from .feature import Feature


class FeatureCollection(BaseEntity):
    def __init__(self, features: list):
        super().__init__(EntityTypes.feature_collection)
        self.features = [
            Feature.from_dict(feature)
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
            'features': self.features
        }

    def merge_features(self):
        pass
