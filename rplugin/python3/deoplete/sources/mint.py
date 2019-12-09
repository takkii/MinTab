import os
import re
import traceback
from deoplete.source.base import Base
from os.path import expanduser

# ------------------------------- KEYWORD -------------------------------------------------------------------------


home = expanduser("~")

dire1 = os.path.expanduser("~/.vim/.cache/dein/repos/github.com/takkii/MinTab_05d895a/")
dire2 = os.path.expanduser("~/.vim/repos/github.com/takkii/MinTab_05d895a/")
dire3 = os.path.expanduser("~/.config/nvim/.cache/dein/repos/github.com/takkii/MinTab_05d895a/")
dire4 = os.path.expanduser("~/.config/nvim/repos/github.com/takkii/MinTab_05d895a/")

if os.path.exists(dire1):
    scala = open(os.path.expanduser("~/.vim/.cache/dein/repos/github.com/takkii/MinTab_05d895a/autoload/source/scala"))
elif os.path.exists(dire2):
    scala = open(os.path.expanduser("~/.vim/repos/github.com/takkii/MinTab_05d895a/autoload/source/scala"))
elif os.path.exists(dire3):
    scala = open(os.path.expanduser("~/.config/nvim/.cache/dein/repos/github.com/takkii/MinTab_05d895a/autoload/source/scala"))
elif os.path.exists(dire4):
    scala = open(os.path.expanduser("~/.config/nvim/repos/github.com/takkii/MinTab_05d895a/autoload/source/scala"))
else:
    print('どれにも該当しません、MinTabを入れてください。')

scala_lib = scala.readlines()
data_scala = list(map(lambda s:s.rstrip(),scala_lib))
scala.close()

# ------------------------------- KEYWORD -------------------------------------------------------------------------

class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'MinTab'
        self.filetypes = ['scala']
        self.mark = '[ Change_The_World ]'
        scalamatch = [r'\.[a-zA-Z0-9_?!]*|[a-zA-Z]\w*::\w*']
        regexmatch = [r'[<a-zA-Z(?: .+?)?>.*?<\/a-zA-Z>]']
        self.input_pattern = '|'.join(scalamatch + regexmatch)
        self.rank = 500

    def get_complete_position(self, context):
        m = re.search('[a-zA-Z0-9_?!]*$', context['input'])
        return m.start() if m else -1

    def gather_candidates(self, context):
        try:
            dic = data_scala
            dic.sort(key=lambda dic: dic[0])
            return dic
        except Exception:
            traceback.print_exc()
