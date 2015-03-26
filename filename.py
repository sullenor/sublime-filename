import re
import sublime, sublime_plugin

class FilenameCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    fn = self.view.file_name()

    if fn:
      # Оставляем только имя файла
      fn = re.sub("^.*?([^\/]+)$", r"\1", fn)
      # Позиция курсора
      pos = self.view.sel()[0].begin()

      self.view.insert(edit, pos, fn)
