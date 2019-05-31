from mechcite import Bibliography, cite


@cite('campbell_modified_1990')
def test(black, panter):
    return black + panter


@cite('wang_pvt_2012')
def test2(white, turd):
    return white - turd

@cite('altinkaynak_melting_2011')
def test3(bla, blaat):
    return bla ** blaat

bib = Bibliography()
bib.load_bib('test.bib')
bib.load_bib('test2.bib', append=True)

test(2, 2)

test(3, 2)

test2(3, 3)

test2(4, 6)

test3(4, 2)

bib._repr_markdown_()

bib._repr_html_()

bib._repr_latex_()
