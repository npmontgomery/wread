

from pathlib import Path

def append_txt_line(input_file, content):
    '''Append a line to a text file, creates if doesnt exist.'''
    with open(f'{input_file}.txt', '+a') as out:
        out.write(content + '\n')

def write_2_txt(input_file, content):
    '''Checks if file exists, if not, writes content to new text file.'''
    q = Path(f'{input_file}.txt')
    if q.is_dir() == True:
        with open(f'{input_file}.txt', '+w') as out:
            out.write(content)
    else:
        print(f'Warning: {input_file} already exists')