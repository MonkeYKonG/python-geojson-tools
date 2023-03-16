import json
from unittest import TestCase

import shapely

from src.constants import EntityTypes
from src.geometries import Polygon, MultiPolygon
from src.tools import load_file, load_file_content


class TestMultiPolygon(TestCase):
    valid_file_path = None
    data = None
    type_data = None
    coordinates_data = None
    tuple_coordinates = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.valid_file_path = 'files/valid_multi_polygon.json'
        cls.data = load_file(cls.valid_file_path)
        cls.type_data = cls.data['type']
        cls.coordinates_data = cls.data['coordinates']
        cls.tuple_coordinates = tuple(
            tuple(
                tuple(
                    tuple(point)
                    for point in polygon
                )
                for polygon in sub_polygon
            )
            for sub_polygon in cls.coordinates_data
        )

    def _test_polygon_values(self, multi_polygon: MultiPolygon):
        self.assertEqual(multi_polygon.type, EntityTypes.multi_polygon.value)
        self.assertIsInstance(multi_polygon._geometry, shapely.geometry.MultiPolygon)
        polygon_coordinates = tuple(
            (tuple(polygon.exterior.coords),) + tuple(tuple(p.coords) for p in polygon.interiors)
            for polygon in multi_polygon._geometry.geoms
        )
        self.assertEqual(polygon_coordinates, self.tuple_coordinates)

    def test_constructor(self):
        multi_polygon = MultiPolygon(self.coordinates_data)
        self._test_polygon_values(multi_polygon)

    def test_from_dict(self):
        multi_polygon = MultiPolygon.from_dict(self.data)
        self._test_polygon_values(multi_polygon)

    def test_from_string(self):
        multi_polygon = MultiPolygon.from_string(load_file_content(self.valid_file_path))
        self._test_polygon_values(multi_polygon)

    def test_from_file(self):
        multi_polygon = MultiPolygon.from_file(self.valid_file_path)
        self._test_polygon_values(multi_polygon)

    def test_invalid_constructor(self):
        self.assertRaises(TypeError, Polygon, [1])
        self.assertRaises(TypeError, Polygon, [1, 2, 3])
        self.assertRaises(TypeError, Polygon, [[1, 2, 3], [4, 5, 6]])
        self.assertRaises(ValueError, Polygon, [[[1, 3], [2, 4]], [1, 2]])
        self.assertRaises(TypeError, Polygon, [[[[1, 3], [2, 4]], [1, 2]], [[[1, 3], [2, 4]], [1, 2]]])
        self.assertRaises(TypeError, Polygon, [[[[[1, 3], [2, 4]], [1, 2]], [[[1, 3], [2, 4]], [1, 2]]],
                                                [[[[1, 3], [2, 4]], [1, 2]], [[[1, 3], [2, 4]], [1, 2]]]])

    def test_to_geojson(self):
        polygon = MultiPolygon.from_dict(self.data)

        self.assertEqual(
            json.dumps(polygon.to_geojson()),
            json.dumps(self.data)
        )
