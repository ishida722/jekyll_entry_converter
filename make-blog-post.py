def __init__(self, text):
    title = text[0:text.find('\n')]
    return post

class front_matter:
    def set_title(self, post_title):
        self.title = self.title + post_title

    def set_date(self):
        nowtime = '{}-{}-{}-'.format()
        self.date = self.date + nowtime

    def make_matter(self):
        self.matter = self.line + '\n' + self.title + '\n' + self.pub + '\n' + self.date + '\n' + self.line + '\n'

    def __init__(self, post_title):
        self.title = 'title: '
        self.line = '---'
        self.pub = 'published: true'
        self.date = 'date: '

        self.set_title(post_title)
        self.set_date()
        make_matter()

        return self.matter

