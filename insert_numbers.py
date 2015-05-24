import sublime, sublime_plugin

class InsertNumbersCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        number = 1
        for region in self.view.sel():
            self.view.insert(edit, region.begin(), str(number) )
            number += 1