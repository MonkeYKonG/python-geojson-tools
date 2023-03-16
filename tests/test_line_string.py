import json
from unittest import TestCase

import shapely

from src.constants import EntityTypes
from src.geometries import LineString
from src.tools import load_file, load_file_content


class TestLineString(TestCase):
    valid_file_path = None
    data = None
    type_data = None
    coordinates_data = None
    tuple_coordinates = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.valid_file_path = 'files/valid_line_string.json'
        cls.data = load_file(cls.valid_file_path)
        cls.type_data = cls.data['type']
        cls.coordinates_data = cls.data['coordinates']
        cls.tuple_coordinates = tuple(
            tuple(point)
            for point in cls.coordinates_data
        )

    def _test_line_string_values(self, line_string: LineString):
        self.assertEqual(line_string.type, EntityTypes.line_string.value)
        self.assertIsInstance(line_string._geometry, shapely.geometry.LineString)
        self.assertEqual(tuple(line_string._geometry.coords), self.tuple_coordinates)

    def test_constructor(self):
        line_string = LineString(self.coordinates_data)
        self._test_line_string_values(line_string)

    def test_from_dict(self):
        line_string = LineString.from_dict(self.data)
        self._test_line_string_values(line_string)

    def test_from_string(self):
        line_string = LineString.from_string(load_file_content(self.valid_file_path))
        self._test_line_string_values(line_string)

    def test_from_file(self):
        line_string = LineString.from_file(self.valid_file_path)
        self._test_line_string_values(line_string)

    def test_invalid_constructor(self):
        self.assertRaises(TypeError, LineString, [1])
        self.assertRaises(TypeError, LineString, [1, 2, 3])
        self.assertRaises(TypeError, LineString, [[[1, 3], [2, 4]], [1, 2]])

    def test_to_geojson(self):
        line_string = LineString.from_dict(self.data)

        self.assertEqual(
            json.dumps(line_string.to_geojson()),
            json.dumps(self.data)
        )
