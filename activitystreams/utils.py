import strict_rfc3339 as dateparser

from activitystreams.exception import ActivityException


def parse_date(raw_date, param_name, required=False):
    if raw_date is None:
        __raise_if_required(raw_date, param_name, required)
        return None

    if not isinstance(raw_date, str):
        raise ActivityException('param %s "%s" is not of instance str: %s' % (param_name, str(raw_date), type(raw_date)))

    raw_date = raw_date.strip()

    if len(raw_date) == 0:
        __raise_if_required(raw_date, param_name, required)
        return None

    if not dateparser.validate_rfc3339(raw_date):
        raise ActivityException('param %s "%s" is not a valid RGC3339 date' % (param_name, str(raw_date)))

    return raw_date


def parse_object(raw_object, param_name, required=False):
    from activitystreams.models.defobject import DefObject
    if raw_object is None:
        __raise_if_required(raw_object, param_name, required)
        return None

    if len(raw_object) == 0:
        return None

    return DefObject(raw_object)


def parse_list_of_objects(raw_list, param_name, required=False):
    from activitystreams.models.defobject import DefObject
    if raw_list is None:
        __raise_if_required(raw_list, param_name, required)
        return None

    if not isinstance(raw_list, list):
        raise ActivityException('param "%s" is not a list' % param_name)

    if len(raw_list) == 0:
        return None

    objects = list()
    for raw in raw_list:
        objects.append(DefObject(raw))

    return objects


def parse_int(number, param_name, required=False):
    if number is None:
        __raise_if_required(number, param_name, required)
        return None

    if isinstance(number, str) and len(number.strip()) == 0:
        return None

    try:
        return int(number)
    except ValueError as e:
        raise ActivityException('param %s "%s" is not a valid integer: %s' % (param_name, str(number), str(e)))


def parse_string(string, param_name, required=False):
    if string is None:
        __raise_if_required(string, param_name, required)
        return None

    if not isinstance(string, str):
        raise ActivityException('param %s "%s" is not a string but is a "%s"' % (param_name, str(string), type(string)))

    if len(string.strip()) == 0:
        __raise_if_required(None, param_name, required)
        return None

    return string


def __raise_if_required(value, name, required):
    if required and value is None:
        raise ActivityException('param %s is required but is None' % name)
