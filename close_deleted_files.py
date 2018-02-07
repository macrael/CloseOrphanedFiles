import sublime
import sublime_plugin

import os


class CloseOrphanedFilesCommand(sublime_plugin.WindowCommand):
    def run(self):
        for view in self.window.views():
            if view.file_name() is not None:
                exists = os.path.exists(view.file_name())

                # is_dirty is not set for a file that has been deleted
                # If there have been any edits since the deletion, then we won't close the buffer
                if not exists and not view.is_dirty() and view.size() > 0:
                    view.set_scratch(True)
                    view.close()

# Just do it on focus for the window. That's something you do after you go do a bunch of git commands. you switch back and then it should prune
# There's edges here for sure. but not big ones.

class CloseOrphandFilesEventListener(sublime_plugin.EventListener):
    def on_activated(self, view):
        view.window().run_command('close_orphaned_files')

