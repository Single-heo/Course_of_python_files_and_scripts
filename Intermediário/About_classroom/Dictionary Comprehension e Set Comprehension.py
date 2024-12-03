from orca.settings import chatMessageVerbosity

from functionss import pretty_list_and_dict_output

example_dict = {
    'name': 'Blue Pen...Pen blue', # Brazil reference => Manoel Gomes
    'preço U$$': 0.25,
    'categoria': 'Escritório'
}



new_dict = {
    key : values
    if isinstance(values, (int,float))
    else values.upper()
    for key, values
    in example_dict.items()
}
pretty_list_and_dict_output(new_dict)


