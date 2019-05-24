from pybtex.database.input import bibtex
from pybtex.database import BibliographyData
from pytablewriter import MarkdownTableWriter, HtmlTableWriter, LatexTableWriter
from pytablewriter.style import Style


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Bibliography(metaclass=Singleton):
    def __init__(self):
        self._bib: BibliographyData = BibliographyData()

    def load_bib(self, filename, append=False):
        parser = bibtex.Parser()
        self._bib = parser.parse_file(filename)

    def cite(self, key):
        if key in self._bib.entries:
            self._bib.citations.add(key)

    def _tbl_writer(self, writer, italic):
        writer.table_name = 'Bibliography'
        writer.headers = ['Index', 'Citation']
        writer.styles = [Style(align='center'), Style(align='left')]
        citations = []
        for idx, citation in enumerate(self._bib.citations):
            cit = self._bib.entries[citation]
            author = ''
            if 'author' in cit.persons:
                author = '{}, '.format(cit._find_person_field('author'))
            title = ''
            if 'title' in cit.fields:
                title = '{}. '.format(italic.format(cit.fields['title'].replace('{', '').replace('}', '')))
            publisher = ''
            if 'publisher' in cit.fields:
                publisher = '{}, '.format(cit.fields['publisher'])
            journal = ''
            if 'journal' in cit.fields:
                journal = '{}, '.format(cit.fields['journal'])
            year = ''
            if 'year' in cit.fields:
                year = '{}'.format(cit.fields['year'])
            row = ['[{}]'.format(idx + 1), '{}{}{}{}{}.'.format(author, title, publisher, journal, year)]
            citations.append(row)
        writer.value_matrix = citations
        writer.margin = 1
        return writer

    def _repr_markdown_(self):
        writer = self._tbl_writer(MarkdownTableWriter(), '*{}*')
        return writer.write_table()

    def _repr_html_(self):
        writer = self._tbl_writer(HtmlTableWriter(), '<em>{}</em>')
        return writer.write_table()

    def _repr_latex_(self):
        writer = self._tbl_writer(LatexTableWriter(), r'\textit{{{}}}')
        return writer.write_table()
