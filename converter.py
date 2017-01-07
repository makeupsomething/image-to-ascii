import charDict
from PIL import Image


def do_scale(image, new_width):
    (original_width, original_height) = image.size
    new_height = int((original_height / float(original_width)) * float(new_width)) /2
    #we divide by two as it produces a more accurate looking aspect ratio even if it is not actually correct

    scaled_image = image.resize((new_width, new_height))
    return scaled_image

def convert_to_grayscale(image):
    grayscale_image = image.convert('L')
    return grayscale_image

def convert_pixels_to_chars(image, color_range, charArray):
    pixels_in_image = list(image.getdata())
    pixels_to_chars = []
    for pixel_value in pixels_in_image:
        pixels_to_chars.append(charArray[pixel_value/color_range])
    return "".join(pixels_to_chars)

def generate_final_image(char_image, new_width):
    final_image = []
    for index in xrange(0, len(char_image), new_width):
        final_image.append(char_image[index: index + new_width])
    return "\n".join(final_image)

def import_image(image_filepath):
    image = None
    try:
        image = Image.open(image_filepath)
    except Exception, e:
        print "Unable to open image file {image_filepath}.".format(image_filepath=image_filepath)
    return image

def do_convert(image, new_width, lod, inverted, custom_char):
    scaled_image = do_scale(image, new_width)
    grayscale_image = convert_to_grayscale(scaled_image)
    charArray = charDict.get_char_array(inverted, custom_char)
    char_image = convert_pixels_to_chars(grayscale_image, lod, charArray)

    return generate_final_image(char_image, new_width)
