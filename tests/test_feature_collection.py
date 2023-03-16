import json
from unittest import TestCase

from src.feature import Feature
from src.feature_collection import FeatureCollection
from src.tools import load_file, load_file_content


class TestFeatureCollection(TestCase):
    valid_file_path = None
    data = None
    features_data = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.valid_file_path = 'files/valid_feature_collection.json'
        cls.data = load_file(cls.valid_file_path)
        cls.features_data = cls.data['features']

    def _test_feature_collection_values(self, feature_collection: FeatureCollection):
        self.assertEqual(len(self.features_data), len(feature_collection.features))
        for feature in feature_collection.features:
            with self.subTest(feature=feature):
                self.assertIsInstance(feature, Feature)

    def test_constructor(self):
        feature_collection = FeatureCollection(self.features_data)
        self._test_feature_collection_values(feature_collection)
        # TODO: Test with Feature into list

    def test_from_dict(self):
        feature_collection = FeatureCollection.from_dict(self.data)
        self._test_feature_collection_values(feature_collection)

    def test_from_file(self):
        feature_collection = FeatureCollection.from_file(self.valid_file_path)
        self._test_feature_collection_values(feature_collection)

    def test_from_string(self):
        feature_collection = FeatureCollection.from_string(load_file_content(self.valid_file_path))
        self._test_feature_collection_values(feature_collection)

    def test_constructor_invalid_features(self):
        self.assertRaises(TypeError, FeatureCollection, None)

    def test_to_geojson(self):
        feature_collection = FeatureCollection.from_dict(self.data)
        self.assertEqual(
            json.dumps(feature_collection.to_geojson()),
            json.dumps(self.data),
        )

    def test_merge_features(self):
        # TODO
        pass

    def test_append(self):
        # TODO
        pass

    def test_delete(self):
        # TODO
        pass

    def test_add_operator(self):
        # TODO
        pass

    def test_iter_operator(self):
        # TODO
        pass
