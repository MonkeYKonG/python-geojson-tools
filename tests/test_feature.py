import json
from unittest import TestCase

from src.feature import Feature
from src.geometries import Point
from src.tools import load_file, load_file_content


class TestFeatureCollection(TestCase):
    valid_file_path = None
    data = None
    properties_data = None
    geometry_data = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.valid_file_path = 'files/valid_feature.json'
        cls.data = load_file(cls.valid_file_path)
        cls.properties_data = cls.data['properties']
        cls.geometry_data = cls.data['geometry']

    def _test_feature_values(self, feature: Feature):
        self.assertDictEqual(feature.properties, self.properties_data)
        self.assertIsInstance(feature.geometry, Point)

    def test_constructor(self):
        feature = Feature(self.geometry_data, self.properties_data)
        self._test_feature_values(feature)
        # TODO: Test with baseGeometry

    def test_from_dict(self):
        feature = Feature.from_dict(self.data)
        self._test_feature_values(feature)

    def test_from_file(self):
        feature = Feature.from_file(self.valid_file_path)
        self._test_feature_values(feature)

    def test_from_string(self):
        feature = Feature.from_string(load_file_content(self.valid_file_path))
        self._test_feature_values(feature)

    def test_constructor_invalid_features(self):
        self.assertRaises(AttributeError, Feature, None)

    def test_to_geojson(self):
        feature = Feature.from_dict(self.data)
        self.assertEqual(
            json.dumps(feature.to_geojson()),
            json.dumps(self.data),
        )
