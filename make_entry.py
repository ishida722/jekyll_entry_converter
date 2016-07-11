import datetime

class entry:
    def make_filename(self):
        dateStamp = datetime.date.today().strftime('%Y-%m-%d-')
        self.filename = dateStamp + '.md'
        
    def __init__(self, text):
        text = str(text)
        self.title = text[0:text.find('\n')]
        self.body = text[text.find('\n'):]
        matter = str(front_matter(self.title))
        self.body = matter + self.body
        self.make_filename()

class front_matter:
    def set_title(self, post_title):
        self.title = self.title + post_title

    def set_date(self):
        time = datetime.datetime.today()
        nowtime = time.strftime('%Y-%m-%d %H:%M:%S +0900')
        self.date = self.date + nowtime

    def make_matter(self):
        self.matter = self.line + '\n' + self.layout + '\n' + self.title + '\n' + self.pub + '\n' + self.date + '\n' + self.line + '\n'

    def __init__(self, post_title):
        self.title  = 'title: '
        self.line   = '---'
        self.layout = 'layout: post'
        self.pub    = 'published: true'
        self.date   = 'date: '

        self.set_title(post_title)
        self.set_date()
        self.make_matter()

    def __str__(self):
        return self.matter