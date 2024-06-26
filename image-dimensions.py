import urllib.parse
import gi
gi.require_version('Nautilus', '3.0')
from gi.repository import Nautilus, GObject, Gtk
from PIL import Image

class ColumnExtension(GObject.GObject, Nautilus.ColumnProvider, Nautilus.InfoProvider):
    def __init__(self):
        pass

    def get_columns(self):
        return Nautilus.Column(name="NautilusPython::image_dimensions_column",
                               attribute="image_dimensions",
                               label="Image dimensions",
                               description="Get image dimensions"),

    def update_file_info(self, file):
        if file.get_uri_scheme() != 'file' or file.get_mime_type()[0:5] != 'image':
            file.add_string_attribute('image_dimensions', '')
            return
        
        filename = urllib.parse.unquote(file.get_uri()[7:])
        size = ''
        try:
            im = Image.open(filename)
            size = 'x'.join(map(str, list(im.size)))
        except IOError:
            pass
        file.add_string_attribute('image_dimensions', size)

