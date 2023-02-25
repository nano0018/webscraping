"""
Returns sorted list of elements in the website
"""

import glob
import os

def create_html_index():

    """
    Creates an index.html with all scrapped html
    """
    # Current path
    cur_path = os.getcwd()
    path = cur_path + "\\web\\**\\*.html"

    # be printed simultaneously.
    print("\nPrinting all html files")
    dummy_html =  open(cur_path + '\\index.html', 'w', encoding='utf-8')
    dummy_html.write('<!DOCTYPE html>')
    dummy_html.write('\n')
    dummy_html.write('<html lang="en">')
    dummy_html.write('\n')
    dummy_html.write('<head>')
    dummy_html.write('\n')
    dummy_html.write('    <meta charset="UTF-8">')
    dummy_html.write('\n')
    dummy_html.write('    <meta http-equiv="X-UA-Compatible" content="IE=edge">')
    dummy_html.write('\n')
    dummy_html.write('    <meta name="viewport" content="width=device-width, initial-scale=1.0">')
    dummy_html.write('\n')
    dummy_html.write('<title>Landing page</title>')
    dummy_html.write('\n')
    dummy_html.write('</head>')
    dummy_html.write('\n')
    dummy_html.write('<body>')
    dummy_html.write('\n')
    dummy_html.write('    <h1>Website index</h1>')
    dummy_html.write('\n')
    dummy_html.write('    <div>')
    dummy_html.write('\n')
    dummy_html.write('      <h2>Live site:</h2>')
    dummy_html.write('\n')
    dummy_html.write('        <a href="https://scraping-web-classcentral.pages.dev/web/">Click here to go to the live site</a>')
    dummy_html.write('\n')
    dummy_html.write('    </div>')
    dummy_html.write('\n')
    dummy_html.write('    <div>')
    dummy_html.write('\n')
    dummy_html.write('      <h2>Here is the list of the translated pages:</h2>')
    dummy_html.write('\n')
    dummy_html.write('        <ol>')


    # Prints all types of txt files present in a Path
    for file in glob.iglob(path, recursive=True):
        printed_file = file.replace('E:\ProyectosOtros\webscraping', '')
        printed_file = printed_file.replace('\\', '/')
        dummy_html.write('\n           <li><a href="' + printed_file + '">' + printed_file + '</li>')
        print(printed_file)

    dummy_html.write('\n')
    dummy_html.write('        </ol>')
    dummy_html.write('\n')
    dummy_html.write('    </div>')
    dummy_html.write('\n')
    dummy_html.write('</body>')
    dummy_html.write('\n')
    dummy_html.write('</html>')