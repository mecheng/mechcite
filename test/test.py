from mechcite import Bibliography, cite


@cite('campbell_modified_1990')
def test(black, panter):
    return black + panter


@cite('wang_pvt_2012')
def test2(white, turd):
    return white - turd


bib = Bibliography()
bib.load_bib('test.bib')

test(2, 2)

test(3, 2)

test2(3, 3)

test2(4, 6)

bib._repr_markdown_()

bib._repr_html_()

bib._repr_latex_()
