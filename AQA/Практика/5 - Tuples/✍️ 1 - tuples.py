#                                                                                   Tuples:
#                                                       Create a tuple with 3 elements. Try to modify one element (expect an error).
#                                               Convert the tuple into a list, modify the element, and convert it back into a tuple.




def create_tuple():
    return ('House of Cards', 'Squid Game', 'The Witcher')


def try_modify_tuple(original_tuple):

    try:
        original_tuple[2] = 'Desperate Housewives'

    except TypeError:
        print("TypeError: 'tuple' object does not support item assignment")

    except Exception:
        print('Unknown error: skipped')


def modify_tuple_element(original_tuple):
    netflix_show_list = list(original_tuple)
    netflix_show_list[2] = 'Desperate Housewives'
    netflix_show_tuple = tuple(netflix_show_list)
    return netflix_show_tuple


def show_results(original, modified: object = None):

    print("\n" + "="*60)
    print(f'Original tuple: {original}')
    print(f'Modified tuple {modified}')
    print("="*60)


original = create_tuple()
show_results(original)

try_modify_tuple(original)

modified = modify_tuple_element(original)
show_results(original, modified)









