#                                                                                   Tuples:
#                                                       Create a tuple with 3 elements. Try to modify one element (expect an error).
#                                               Convert the tuple into a list, modify the element, and convert it back into a tuple.




def create_tuple():
    return 'House of Cards', 'Squid Game', 'The Witcher'



def try_modify_tuple(original_tuple):

    try:
        original_tuple[2] = 'Desperate Housewives'

    except TypeError as error:
        print('TypeError:', error)

    except Exception as error:
        print('Unknown error:', error)



def modify_tuple_element(original_tuple):
    show_list = list(original_tuple)
    show_list[2] = 'Desperate Housewives'
    show_tuple = tuple(show_list)
    return show_tuple



def show_results(original, modified = None):

    print("\n" + "="*60)
    print(f'Original tuple: {original}')
    print(f'Modified tuple {modified}')
    print("="*60)


original = create_tuple()
show_results(original)                              # Haven't cheated yet

try_modify_tuple(original)

modified = modify_tuple_element(original)
show_results(original, modified)









