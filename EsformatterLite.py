import sublime, sublime_plugin
import time
import os
import shutil
import subprocess

# https://www.sublimetext.com/docs/3/api_reference.html#sublime.Edit
# http://sublime-text-unofficial-documentation.readthedocs.org/en/latest/extensibility/plugins.html
# https://github.com/millermedeiros/esformatter
# http://kendriu.com/how-to-use-pipes-in-python-subprocesspopen-objects
# http://stackoverflow.com/questions/163542/python-how-do-i-pass-a-string-into-subprocess-popen-using-the-stdin-argument
#
class EsformatterLiteCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		filesrc = view.file_name()
		region = sublime.Region(0, self.view.size())

		selection = view.substr(region)
		p = subprocess.Popen(["esformatter"],
			shell=True,
			cwd=os.path.dirname(filesrc),
			stdout=subprocess.PIPE,
			stdin=subprocess.PIPE,
			universal_newlines=True)
		p.stdin.write(selection)
		formatted = p.communicate()[0];
		p.stdin.close()

		view.replace(edit, region, formatted)