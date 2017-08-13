import os, sys

r = os.path.realpath(__file__)
r = os.path.dirname(r)
r = os.path.dirname(r)

appName = "pyfox"
version = "0.07.22"
comment = "Rethinked Web BRowser"
home = "https://github.com/jeremi360/pyfox"
rapport = "https://github.com/jeremi360/pyfox/issues"
licenseText = os.path.join(r, 'LICENSE')
defaultSearchEngine = "https://www.qwant.com/?q="
aboutFile = os.path.join(r, 'README.md')
toDoFile = os.path.join(r, 'ToDo.md')
changelog = os.path.join(r, 'ChangeLog.md')
tabSize = 400

if sys.platform == 'win32':
    userDir = os.path.join("C:","Users", os.getlogin(), "pyfox")
else:
    userDir = os.path.join(os.getenv('HOME'), '.pyfox')

settingsFile = os.path.join(userDir, "settings.pyd")
historyFile = os.path.join(userDir, "history.pyd")
trashFile = os.path.join(userDir, "trash.pyd")
sessionFile = os.path.join(userDir, "session.pyd")
bookmarksFiles = os.path.join(userDir, "bookmarks.pyd")
