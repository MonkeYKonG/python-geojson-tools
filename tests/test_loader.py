import json
from unittest import TestCase

from src.feature_collection import FeatureCollection
from src.tools import load


class TestLoad(TestCase):
    def test_load_feature_collection(self):
        with open('valid_feature_collection.json') as file:
            data = json.load(file)
        feature_collection = load(data)

        self.assertIsInstance(feature_collection, FeatureCollection)
