import begin
import converter

@begin.start
def run(image_file_path='sample_images/isaax.jpg', width=120, lod=127, inverted=0, custom_char='.'):
    image = converter.import_image(image_file_path)
    ascii_image = converter.do_convert(image, int(width), lod, int(inverted), custom_char)
    print ascii_image