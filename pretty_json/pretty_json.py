from typing import Dict, List, Tuple, Any, Union

BASE_TYPES = (str, int, float, bool)


def pretty_json(data: Dict, indent: Union[str, int] = '\t', prefix: str = '', new_line: str = '\n'):
    """
    Prettify a JSON Object
    :param data: The JSON Object to prettify. Must be a dictionary
    :param indent: Optional indent string ('\t') or number of spaces to indent, at each new level
    :param prefix: Optional prefix, prepended to each line ('*')
    :param new_line: Optional new_line character/string
    :return: A pretty string of the incoming JSON Object
    """
    if not isinstance(data, Dict):
        raise TypeError(f'`data` must be a {dict}. It is {type(data)} instead')

    if isinstance(indent, int):
        indent = ' ' * indent

    lines = []

    for k, v in data.items():
        if isinstance(v, BASE_TYPES):
            lines.append(f'{prefix}{k}: {v}')

        if v is None:
            lines.append(f'{prefix}{k}: {None}')

        if isinstance(v, (Dict, List, Tuple)):
            lines.append(f'{prefix}{k}:')
            lines.extend(_prettify(v, 1, indent_str=indent, prefix=prefix))

    return new_line.join(lines)


def _prettify(data: Any, depth: int, indent_str: str = '\t', prefix: str = ''):
    lines = []

    full_prefix = f'{indent_str * depth}{prefix}'

    if isinstance(data, BASE_TYPES):
        lines.append(f'{full_prefix}{data}')

    elif data is None:
        lines.append(f'{full_prefix}{None}')

    elif isinstance(data, (List, Tuple)):
        if data:
            if len(data) == 1:
                lines.append(f'{full_prefix}{data[0]}')
            else:
                for entry in data:
                    lines.extend(_prettify(entry, depth, indent_str=indent_str, prefix=prefix))

    elif isinstance(data, Dict):
        if data:
            for k, v in data.items():
                if isinstance(v, BASE_TYPES):
                    lines.append(f'{full_prefix}{k}: {v}')

                elif v is None:
                    lines.append(f'{full_prefix}{k}: {None}')

                else:
                    lines.append(f'{full_prefix}{k}:')
                    lines.extend(_prettify(v, depth + 1, indent_str=indent_str, prefix=prefix))

    return lines
