def setify_list_of_dicts(list_of_dicts: list) -> list:
    """
    Takes a list of dicts and returns a list of unique dicts

    list of dicts = [{'a': 1, 'b': 2}, {'a': 1, 'b': 2}, {'a': 1, 'b': 2}]

    returns [{'a': 1, 'b': 2}]
    """
    # create a list to hold the unique dicts
    unique_dicts = []
    # loop through the list of dicts
    for dict in list_of_dicts:
        # if the dict is not in the list of unique dicts, add it
        if dict not in unique_dicts:
            unique_dicts.append(dict)
    # return the list of unique dicts
    return unique_dicts
