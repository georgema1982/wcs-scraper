from pyquery import PyQuery as pq
import codecs
import string
from jinja2 import Environment, FileSystemLoader
import requests

q = pq(url = 'http://www.radioexpress.com/charts/world-chart/')
title = q('div.entry-content strong')
table = q('#tablepress-4')
env = Environment(loader = FileSystemLoader('.'))
with codecs.open(string.replace(title.text(), ' | ', ' ') + '.html', "w", "utf-8-sig") as output:
    output.write(env.get_template('template.html').render(table_css = requests.get('http://www.radioexpress.com/wp-content/tablepress-combined.min.css?ver=10').text, title = title.outerHtml(), table = table.outerHtml()))
