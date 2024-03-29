import pytest

from human_json import to_human_json


@pytest.mark.parametrize('args', [
    set()
])
def test_non_dict(args):
    with pytest.raises(TypeError):
        to_human_json(args)


@pytest.mark.parametrize('args,expected', [
    (1, '1'),
    (-5.1, '-5.1'),
    (True, 'True'),
    (None, 'None')
])
def test_literals(args, expected):
    result = to_human_json(args)
    assert result == expected


def test_dict():
    result = to_human_json({
        'key1': 'value1',
        'key2': (1, 2),
        'key3': None
    })

    expected = 'key1: value1\nkey2:\n\t1\n\t2\nkey3: None'

    assert result == expected


def test_list():
    result = to_human_json(['a', 'b', None, True, 1])
    expected = 'a\nb\nNone\nTrue\n1'
    assert result == expected


def test_tuple():
    result = to_human_json(('a', 'b', None, True, 1))
    expected = 'a\nb\nNone\nTrue\n1'
    assert result == expected


@pytest.mark.parametrize('args,expected', [
    ({'key': 'val'}, 'key: val'),
    ({'key': ''}, 'key: '),
    ({'key': 1}, 'key: 1'),
    ({'key': -50}, 'key: -50'),
    ({'key': 1.1}, 'key: 1.1'),
    ({'key': -49.91}, 'key: -49.91'),
    ({'key': True}, 'key: True'),
    ({'key': False}, 'key: False'),
    ({'key': None}, 'key: None')
])
def test_simple_dict(args, expected):
    res = to_human_json(args)
    assert res == expected


def test_nested_dict():
    result = to_human_json({
        'key1': {
            'in_key1': True,
            'in_key2': False,
            'in_key3': None,
            'in_key4': [],
            'in_key5': ('a', 'b')
        },
        'key2': 'string'
    })

    expected = ('key1:\n'
                '\tin_key1: True\n'
                '\tin_key2: False\n'
                '\tin_key3: None\n'
                '\tin_key4:\n'
                '\t\t-\n'
                '\tin_key5:\n'
                '\t\ta\n'
                '\t\tb\n'
                'key2: string')

    assert result == expected


def test_nested_with_prefix():
    result = to_human_json({
        'className': 'ComputerScience',
        'classId': 2020,
        'assignments': {
            'assignment1': {
                'average_grade': 5.5,
                'description': 'Complete Assignment 1',
                'grades': [5, 5, 5, 7]
            },
            'assignment2': {
                'average_grade': None,
                'description': 'Complete Assignment 2',
                'grades': ()
            }
        },
        'students': ('student1', 'student2', 'studentabc', 2019, None, 10.5)
    }, prefix='* ')

    expected = ('* className: ComputerScience\n'
                '* classId: 2020\n'
                '* assignments:\n'
                '\t* assignment1:\n'
                '\t\t* average_grade: 5.5\n'
                '\t\t* description: Complete Assignment 1\n'
                '\t\t* grades:\n'
                '\t\t\t* 5\n'
                '\t\t\t* 5\n'
                '\t\t\t* 5\n'
                '\t\t\t* 7\n'
                '\t* assignment2:\n'
                '\t\t* average_grade: None\n'
                '\t\t* description: Complete Assignment 2\n'
                '\t\t* grades:\n'
                '\t\t\t* -\n'
                '* students:\n'
                '\t* student1\n'
                '\t* student2\n'
                '\t* studentabc\n'
                '\t* 2019\n'
                '\t* None\n'
                '\t* 10.5'
                )

    assert result == expected
