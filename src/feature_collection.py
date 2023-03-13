from .base_entity import BaseEntity
from .constants import EntityTypes


class FeatureCollection(BaseEntity):
    def __init__(self, features: list):
        super().__init__(EntityTypes.feature_collection)
        self.features = features

    def to_geojson(self) -> dict:
        return {
            'type': self.type,
            'features': self.features
        }

    def merge_features(self):
        pass
