# Wread
> Stop writing code for simple read and write functions in Python. 

![MIT](https://img.shields.io/dub/l/vibe-d.svg?style=flat-square)
![dependencies](https://img.shields.io/david/expressjs/express.svg?style=flat-square)
![python](https://img.shields.io/badge/python-3.6%2C3.7-blue.svg?style=flat-square)


Wread simplifies common actions of ``pickle``, ``txt``, and ``csv``, making life just a little easier for noobs like me and anyone else who wants to write a few lines less of code.

## Installation

OS X & Linux:

```
pip install wread
```

## Usage example

Wread includes three types of function: ``pickle``, ``txt``, and ``csv``. Import all of them by importing the package ``wread``.

```
import wread  
----
# Append a line to a text file, creates if doesnt exist.

append_txt_line(input_file, content)
----
# Checks if file exists, if not, writes content to new text file.

write_2_txt(input_file, content)
```

```
import wread
----
# Saves variable as pickle file.

save_pickle(output_file, variable)
----
# Loads pickle file variable

read_pickle(input_file)
```

```
import wread
----
# Load csv and output row content as lists in list of rows.

csv_list_rows(input_file)
----
# Load csv and output individual row as list.

def get_csv_row(input_file, line_number)
----  
# Appends items in list to new line of csv file. Makes file if does't exist.

csv_append(input_file, input_list)
```


## Development setup

All dependent modules are already included in the standard library :smile:


## Release History

* 0.0.1
    * Initial release (still a work in progress)

## Meta

NPM – [email me](https://github.com/npmontgomery)

Distributed under the MIT license. See ``LICENSE`` for more information.


## Contributing

If you would like to contribute or have any suggestions on how to improve, just send me a private message!

<!-- Markdown link & img dfn's -->


