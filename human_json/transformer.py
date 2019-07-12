from typing import Any, Dict, List, Tuple, Union

BASE_TYPES = (str, int, float, bool)

ALLOWED_TYPES = BASE_TYPES + (dict, list, tuple)


def to_human_json(json_data: Any, indent: Union[str, int] = '\t', prefix: str = '', new_line: str = '\n'):
    """
    Prettify a JSON Object
    :param json_data: The JSON Object to prettify.
    :param indent: Optional indent string ('\t') or number of spaces to indent, at each new level
    :param prefix: Optional prefix, prepended to each line ('*')
    :param new_line: Optional new_line character/string
    :return: A pretty string of the incoming JSON Object
    """

    def _serialize(data: Any, depth: int):
        lines = []

        full_prefix = f'{indent * depth}{prefix}'

        if isinstance(data, BASE_TYPES):
            lines.append(f'{full_prefix}{data}')

        elif data is None:
            lines.append(f'{full_prefix}{None}')

        elif isinstance(data, (List, Tuple)):
            if data:
                for entry in data:
                    lines.extend(_serialize(entry, depth))
            else:
                lines.append(f'{full_prefix}-')

        elif isinstance(data, Dict):
            if data:
                for k, v in data.items():
                    if isinstance(v, BASE_TYPES):
                        lines.append(f'{full_prefix}{k}: {v}')

                    elif v is None:
                        lines.append(f'{full_prefix}{k}: {None}')

                    else:
                        lines.append(f'{full_prefix}{k}:')
                        lines.extend(_serialize(v, depth + 1))
            else:
                lines.append(f'{full_prefix}-')

        return lines

    if not isinstance(json_data, ALLOWED_TYPES) and json_data is not None:
        raise TypeError(f'Expected one of {ALLOWED_TYPES + (None,)}. Instead, it is {type(json_data)}')

    if isinstance(indent, int):
        indent = ' ' * indent

    return new_line.join(_serialize(json_data, 0))
