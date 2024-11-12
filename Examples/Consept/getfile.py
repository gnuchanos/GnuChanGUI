import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class GGetFilePath(Gtk.Window):
    def __init__(self, Title="Select File", ShowHiden=False):
        super().__init__(title="Dosya Seçici")
        self.set_default_size(200, 100)
        self.Path = ""
        self.title = Title
        self.showHiden = ShowHiden
        self.Filters = [
                ("ALL Type", "*.*"),
                ("GC Text File", "*.gc"), 
                ("PROGRAM-> Python Files", "*.py"),
                ("PROGRAM-> C Files", "*.c"),
                ("IMAGE-> PNG", "*.png"),
                ("IMAGE-> JPG", "*.jpg"),
            ]

    def Get(self):
        dialog = Gtk.FileChooserDialog( title=self.title, parent=self, action=Gtk.FileChooserAction.OPEN )
        dialog.set_show_hidden(self.showHiden)
        dialog.add_buttons( Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.OK )

        # Add file type filters
        for filter_name, pattern in self.Filters:
            file_filter = Gtk.FileFilter()
            file_filter.set_name(filter_name)
            file_filter.add_pattern(pattern)
            dialog.add_filter(file_filter)

        # Dialog sonuçlarını işleme
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            self.Path = dialog.get_filename()
        else:
            self.Path = None

        dialog.destroy()
        return self.Path

# Kullanım örneği
if __name__ == "__main__":
    app = GGetFilePath()
    file_path = app.get()
    print("Path:", file_path)