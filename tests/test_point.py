import json
from unittest import TestCase

import shapely

from src.constants import EntityTypes
from src.geometries import Point
from src.tools import load_file, load_file_content


class TestPoint(TestCase):
    valid_file_path = None
    data = None
    type_data = None
    coordinates_data = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.valid_file_path = 'files/valid_point.json'
        cls.data = load_file(cls.valid_file_path)
        cls.type_data = cls.data['type']
        cls.coordinates_data = cls.data['coordinates']

    def _test_point_values(self, point: Point):
        self.assertEqual(point.type, EntityTypes.point.value)
        self.assertIsInstance(point._geometry, shapely.geometry.Point)
        self.assertEqual(list(*point._geometry.coords), self.coordinates_data)

    def test_constructor(self):
        point = Point(self.coordinates_data)
        self._test_point_values(point)

    def test_from_dict(self):
        point = Point.from_dict(self.data)
        self._test_point_values(point)

    def test_from_string(self):
        point = Point.from_string(load_file_content(self.valid_file_path))
        self._test_point_values(point)

    def test_from_file(self):
        point = Point.from_file(self.valid_file_path)
        self._test_point_values(point)

    def test_invalid_constructor(self):
        self.assertRaises(ValueError, Point, [])
        self.assertRaises(ValueError, Point, [1])
        self.assertRaises(ValueError, Point, [1, 2, 3])
        self.assertRaises(ValueError, Point, [[1, 3], [2, 4]])

    def test_to_geojson(self):
        point = Point.from_dict(self.data)

        self.assertEqual(
            json.dumps(point.to_geojson()),
            json.dumps(self.data)
        )

    def test_to_circle(self):
        # TODO: todo
        pass

    def test_to_square(self):
        # TODO: todo
        pass
