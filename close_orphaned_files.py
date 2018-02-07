import sublime
import sublime_plugin

import os


class CloseOrphanedFilesCommand(sublime_plugin.WindowCommand):
    def run(self):
        close_count = 0
        for view in self.window.views():
            if view.file_name() is not None:
                exists = os.path.exists(view.file_name())

                # is_dirty is not set for a file that has just been deleted
                if not exists and not view.is_dirty() and view.size() > 0:
                    view.set_scratch(True)
                    view.close()
                    close_count += 1

        if close_count > 0:
            plural = "s" if close_count > 1 else ""
            self.window.status_message("Closed {} orphaned file{}.".format(close_count, plural))


class CloseOrphandFilesEventListener(sublime_plugin.EventListener):
    # Just do it on focus for the window. That's something you do after you go
    # do a bunch of git commands. you switch back and then it should prune
    def on_activated(self, view):
        view.window().run_command('close_orphaned_files')
