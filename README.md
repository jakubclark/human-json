# Pretty JSON

`pretty_json` is a simple python library, that can take a JSON Object, and create a pretty string for that object.

JSON is easy to transport, and quite easy to read, but requires some form of prior training to properly understand it.
This library allows one to transform JSON Objects into an easier to read format

## Example

The following JSON Object:


```json
{
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
    'students': ('student1', 'student2', 'studentabc', 2019, None, 10.5),
}
```

turns into the following pretty string:

```text
className: ComputerScience
classId: 2020
assignments:
	assignment1:
		average_grade: 5.5
		description: Complete Assignment 1
		grades:
			5
			5
			5
			7
	assignment2:
		average_grade: None
		description: Complete Assignment 2
		grades:
students:
	student1
	student2
	studentabc
	2019
	None
	10.5
```

### Custom Prefixes

You can also specify an optional prefix, that will be prefixed to each line. A possible prefix is "* ".
Using this prefix, will return a markdown list. This can be directly copy-pasted into a markdown file, for example:


* className: ComputerScience
* classId: 2020
* assignments:
	* assignment1:
		* average_grade: 5.5
		* description: Complete Assignment 1
		* grades:
			* 5
			* 5
			* 5
			* 7
	* assignment2:
		* average_grade: None
		* description: Complete Assignment 2
		* grades:
* students:
	* student1
	* student2
	* studentabc
	* 2019
	* None
	* 10.5
	
### Custom Indentations

You can also specify a custom indentation. The default is `\t`, but you can specify ` ` or even a number of spaces.
Below is an example using `2`:

```text
className: ComputerScience
classId: 2020
assignments:
  assignment1:
    average_grade: 5.5
    description: Complete Assignment 1
    grades:
      5
      5
      5
      7
  assignment2:
    average_grade: None
    description: Complete Assignment 2
    grades:
students:
  student1
  student2
  studentabc
  2019
  None
  10.5
```