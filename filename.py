import os
from os.path import basename
import sublime, sublime_plugin

class FilenameCommand(sublime_plugin.TextCommand):  
  def run(self, edit):
    fn = self.view.file_name()
    sel = self.view.sel()

    if fn:
      # Оставляем только имя файла
      fn = basename(os.path.splitext(fn)[0])
    else:
      fn = "Error: file buffer is empty"

    if len(sel) > 0:
      # если выбран текст - заменяем каждый элемент
      for region in sel:
        self.view.replace(edit, region, fn)

    else: 
      # Позиция курсора
      pos = sel[0].begin()
      self.view.insert(edit, pos, fn)