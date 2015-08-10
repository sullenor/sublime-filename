import os
import sublime, sublime_plugin

class FilenameCommand(sublime_plugin.TextCommand):  
  def run(self, edit):
    fn = self.view.name()
    sel = self.view.sel()

    if fn :
      # Оставляем только имя файла
      fn = os.path.splitext(fn)[0]
    else :
      fn = "Error: select file"

    # если выбран текст
    if len(sel) > 0 :
      for region in sel:
        self.view.replace(edit, region, fn)

    else : 
      # Позиция курсора
      pos = sel[0].begin()
      self.view.insert(edit, pos, fn)