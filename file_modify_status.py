import sublime_plugin
import sublime


class FileSavedStatus(sublime_plugin.EventListener):


    def on_modified(self, view):
        self.settings = sublime.load_settings("File Saved Status.sublime-settings")
        self.check_status(view)

    def on_activated(self, view):
        self.settings = sublime.load_settings("File Saved Status.sublime-settings")
        self.check_status(view)

    def on_post_save(self, view):
        self.settings = sublime.load_settings("File Saved Status.sublime-settings")
        view.set_status("(.0.file_saved_status", self.settings.get("saved_marker") )
       # view.settings().set("color_scheme", "Packages/Color Scheme - Default/Monokai.tmTheme")        


    def check_status(self, view):
        if view.get_status("(.0.file_saved_status")=="":
            view.set_status("(.0.file_saved_status", self.settings.get("unsaved_marker"))
         #   view.settings().set("color_scheme", "Packages/Color Scheme - Default/LAZY.tmTheme")   

    
