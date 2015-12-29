
import comgen
import imggrab



# just a place for me to generate a bunch of results and sanity check them


def generate_compliments():
    cg = comgen.ComGen()
    for i in xrange(1000):
        gen = cg.generate()
        cg.do_selection()
        print gen[0]


def generate_html_file():
    cg = comgen.ComGen()
    with open('test.html', 'w') as f:
        f.write('<html><head></head><body>')
        for i in xrange(10):
            # generate a compliment and its keyword
            cg.do_selection()
            phrase, terms = cg.generate()

            # search for an image relevant to those keywords
            ig = imggrab.ImgGrab()
            image_url = ig.search('+'.join(terms))
            f.write("<h2>{}</h2><p>{}</p>".format(phrase, ', '.join(terms)))
            if image_url:
                f.write("<img src={}><hr>".format(image_url))
        f.write('</body></html>')
        f.flush()
        f.close()

generate_compliments()

generate_html_file()
