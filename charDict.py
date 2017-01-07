image_type = {
 'STANDARD' : [ '.', ' ', ' '],
 'INVERTED_STANDARD' : [ ' ', '.', '.']
}


def get_char_array(inverted, custom_char):
    ret_dict = []
    if not inverted:
        ret_dict = image_type['STANDARD']
        ret_dict[0] = custom_char
    else:
        ret_dict = image_type['INVERTED_STANDARD']
        ret_dict[1] = custom_char
        ret_dict[2] = custom_char
    return ret_dict