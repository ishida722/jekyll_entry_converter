from make_entry import entry
import unittest

testInputText ='''title test entry
body line1
body line2
body line3'''

post = entry(testInputText)

print(post.filename)
print(post.body)
