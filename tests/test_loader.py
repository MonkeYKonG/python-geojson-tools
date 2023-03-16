import json
from unittest import TestCase

from src.feature import Feature
from src.feature_collection import FeatureCollection
from src.geometries import Point, LineString, Polygon, MultiPolygon
from src.tools import load, load_from_string, load_from_file, load_file, load_file_content


class TestLoad(TestCase):
    def test_load_feature_collection(self):
        data = load_file('files/valid_feature_collection.json')
        feature_collection = load(data)

        self.assertIsInstance(feature_collection, FeatureCollection)

    def test_load_feature(self):
        data = load_file('files/valid_feature.json')
        feature = load(data)

        self.assertIsInstance(feature, Feature)

    def test_load_point(self):
        data = load_file('files/valid_point.json')
        point = load(data)

        self.assertIsInstance(point, Point)

    def test_load_line_string(self):
        data = load_file('files/valid_line_string.json')
        line_string = load(data)

        self.assertIsInstance(line_string, LineString)

    def test_load_polygon(self):
        data = load_file('files/valid_polygon.json')
        polygon = load(data)

        self.assertIsInstance(polygon, Polygon)

    def test_load_multi_polygon(self):
        data = load_file('files/valid_multi_polygon.json')
        multi_polygon = load(data)

        self.assertIsInstance(multi_polygon, MultiPolygon)

    def test_load_invalid_type(self):
        data = {'type': 'INVALID'}
        self.assertRaises(ValueError, load, data)


class TestLoadFromString(TestCase):
    def test_load_feature_collection(self):
        file_content = load_file_content('files/valid_feature_collection.json')
        feature_collection = load_from_string(file_content)

        self.assertIsInstance(feature_collection, FeatureCollection)

    def test_load_feature(self):
        file_content = load_file_content('files/valid_feature.json')
        feature = load_from_string(file_content)

        self.assertIsInstance(feature, Feature)

    def test_load_point(self):
        file_content = load_file_content('files/valid_point.json')
        point = load_from_string(file_content)

        self.assertIsInstance(point, Point)

    def test_load_line_string(self):
        file_content = load_file_content('files/valid_line_string.json')
        line_string = load_from_string(file_content)

        self.assertIsInstance(line_string, LineString)

    def test_load_polygon(self):
        file_content = load_file_content('files/valid_polygon.json')
        polygon = load_from_string(file_content)

        self.assertIsInstance(polygon, Polygon)

    def test_load_multi_polygon(self):
        file_content = load_file_content('files/valid_multi_polygon.json')
        multi_polygon = load_from_string(file_content)

        self.assertIsInstance(multi_polygon, MultiPolygon)

    def test_invalid_json(self):
        string = "{hello]"
        self.assertRaises(ValueError, load_from_string, string)


class TestLoadFromFile(TestCase):
    def test_load_feature_collection(self):
        feature_collection = load_from_file('files/valid_feature_collection.json')

        self.assertIsInstance(feature_collection, FeatureCollection)

    def test_load_feature(self):
        feature = load_from_file('files/valid_feature.json')

        self.assertIsInstance(feature, Feature)

    def test_load_point(self):
        point = load_from_file('files/valid_point.json')

        self.assertIsInstance(point, Point)

    def test_load_line_string(self):
        line_string = load_from_file('files/valid_line_string.json')

        self.assertIsInstance(line_string, LineString)

    def test_load_polygon(self):
        polygon = load_from_file('files/valid_polygon.json')

        self.assertIsInstance(polygon, Polygon)

    def test_load_multi_polygon(self):
        multi_polygon = load_from_file('files/valid_multi_polygon.json')

        self.assertIsInstance(multi_polygon, MultiPolygon)

    def test_unknown_file(self):
        self.assertRaises(FileNotFoundError, load_from_file, 'invalid/path')

    def test_invalid_file_type(self):
        self.assertRaises(IsADirectoryError, load_from_file, '.')
