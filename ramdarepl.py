
import sublime, sublime_plugin
import subprocess
import re

PLUGIN_NAME = "ramdarepl"
SETTINGS_FILE = '{0}.sublime-settings'.format(PLUGIN_NAME)

class RamdaReplCommand(sublime_plugin.TextCommand):
  def run(self, edit, **args):
    self.edit = edit

    settings = sublime.load_settings(SETTINGS_FILE)
    node_modules_path = settings.get("node_modules_path")
    use_ramda_fantasy = settings.get("ramda-fantasy")
    contents = self.view.substr(sublime.Region(0, self.view.size()))
    js =  (
      "\"const R = require('ramda');\n"
      "const RF = " + ("require('ramda-fantasy')" if use_ramda_fantasy else "{}") + ";\n"
      "with(" + "R.merge(R,RF)" + ") {" + contents + "}\""
    )
    self.show_repl_panel()
    output = subprocess.getoutput("export NODE_PATH=" + node_modules_path +
      " && node -p " + js)
    self.append_data(output)

  def clear_panel_view(self):
    self.output_view.set_read_only(False)
    edit = self.edit
    self.output_view.erase(edit, sublime.Region(0, self.output_view.size()))
    self.output_view.set_read_only(True)

  def append_data(self, data):
    self.output_view.set_read_only(False)
    edit = self.edit
    self.output_view.insert(edit, self.output_view.size(), data)
    self.output_view.set_read_only(True)

  def show_repl_panel(self):
    if not hasattr(self, 'output_view'):
      hasattr(self, 'output_view')

    self.output_view = self.view.window().get_output_panel('ramda_repl')
    self.clear_panel_view()
    self.view.window().run_command('show_panel', {'panel': 'output.ramda_repl'})
