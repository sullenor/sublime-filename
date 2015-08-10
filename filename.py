import os
import sublime, sublime_plugin

class FilenameCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    fn = self.view.file_name()

    if fn:
      # Оставляем только имя файла
      fn = os.path.splitext(fn)[0]
      # Позиция курсора
      pos = self.view.sel()[0].begin()

      self.view.insert(edit, pos, fn)
