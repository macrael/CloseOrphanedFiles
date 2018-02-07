import sublime
import sublime_plugin

import os


class CloseOrphanedFilesCommand(sublime_plugin.WindowCommand):
    def run(self):
        print("NONONONO")
        for view in self.window.views():
            if view.file_name() is not None:
                exists = os.path.exists(view.file_name())
                print(view.file_name())

                if not exists:
                    view.set_scratch(True)
                    view.close()

# Just do it on focus for the window. That's something you do after you go do a bunch of git commands. you switch back and then it should prune
# There's edges here for sure. but not big ones.

class CloseOrphanedFilesEventListener(sublime_plugin.ViewEventListener):
    pass

    # @classmethod
    # def is_applicable(self, settings):
    #     print("IS APPLIC")
    #     print(settings)
    #     print(dir(settings))
    #     print(settings.settings_id)

    # def on_load(self):
    #     print("LOAD")
    #     print(self)

    # def on_pre_close(self):
    #     print("CLOSING")
    #     print(self)

    # def on_modified(self):
    #     print("MODIF")
    #     print(self)

    # def on_post_save(self):
    #     print("SELOAVEVEVE")
    #     print(self)

    # def on_activated(self):
    #     print('on activated')
    #     print(self)
