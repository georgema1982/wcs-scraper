from pyquery import PyQuery as pq
import codecs
import string
from jinja2 import Environment, FileSystemLoader
import requests

q = pq(url = 'http://www.radioexpress.com/charts/world-chart/')
title = q('#primary p > strong > font')
table = q('#tablepress-2')
env = Environment(loader = FileSystemLoader('.'))
with codecs.open(string.replace(title.text(), ' | ', ' ') + '.html', "w", "utf-8-sig") as output:
    output.write(env.get_template('template.html').render(table_css = requests.get('http://www.radioexpress.com/wp-content/plugins/tablepress/css/default.min.css?ver=1.6.1').text, title = title.text(), table = table.outerHtml()))
