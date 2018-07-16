import pickle
def save_pickle(output_file, variable):
    '''Saves variable as pickle file.'''
    with open(output_file, 'wb') as f:
        pickle.dump(variable, f)

def read_pickle(input_file):
    '''Loads pickle file variable'''
    with open(input_file, "rb") as f:
        return pickle.load(f)