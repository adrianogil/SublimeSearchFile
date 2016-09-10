import sublime, sublime_plugin  

import os

class OpenSearchFile(sublime_plugin.EventListener):  
    def on_load(self, view):  
        filename, file_extension = os.path.splitext(view.file_name())
        if file_extension == '.sublime-search':
        	view.set_syntax_file("Packages/Default/Find Results.hidden-tmLanguage")
        	view.settings().set('result_line_regex', '^ +([0-9]+):')
        	view.settings().set('result_file_regex', "^([A-Za-z\\\\/<].*):$")
        # print(view.file_name() + " just got loaded with extension " + file_extension)