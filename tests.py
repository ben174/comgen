
import comgen


cg = comgen.ComGen()
for i in xrange(1000):
    gen = cg.generate()
    cg.do_selection()
    print gen[0]
    #print '     ' + ', '.join(gen[1])
