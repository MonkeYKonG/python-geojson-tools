from . import constants, geometries, errors

GEOMETRY_CLASSES = {
    constants.EntityTypes.point.value: geometries.Point,
    constants.EntityTypes.line_string.value: geometries.LineString,
    constants.EntityTypes.polygon.value: geometries.Polygon,
    constants.EntityTypes.multi_polygon.value: geometries.MultiPolygon,
}


def load_geometry(obj: dict):
    obj_type = obj.get('type')
    if obj_type is None:
        raise ValueError(errors.INVALID_FORMAT)
    if obj_type not in (entity.value for entity in constants.EntityTypes):
        raise ValueError(errors.UNKNOWN_TYPE)
    return GEOMETRY_CLASSES[obj_type].from_dict(obj)
