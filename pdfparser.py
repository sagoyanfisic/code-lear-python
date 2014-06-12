from pdfminer.pdfparser import PDFParser, PDFDocument, PDFNoOutlines, PDFSyntaxError
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTFigure, LTImage, LTTextLineHorizontal, LTTextBoxHorizontal, LTChar, LTRect, LTLine, LTAnon
from binascii import b2a_hex
from operator import itemgetter


def getTables(pdf_content):
    parser = PDFParser(pdf_content)
    doc = PDFDocument()
    parser.set_document(doc)
    doc.set_parser(parser)

    doc.initialize("")
    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
   
    for n, page in enumerate(doc.get_pages()):
        interpreter.process_page(page)
        layout = device.get_result()
        ParsePage(layout)


def ParsePage(layout):
	xset, yset = set(), set()
	tlines = [ ]
	objstack = list(reversed(layout._objs))
	while objstack:
    		b = objstack.pop()
	    	if type(b) in [LTFigure, LTTextBox, LTTextLine, LTTextBoxHorizontal]:
        		objstack.extend(reversed(b._objs))  # put contents of aggregate object into stack
    		elif type(b) == LTTextLineHorizontal:
        		tlines.append(b)
    		elif type(b) == LTLine:
        		if b.x0 == b.x1:
            			xset.add(b.x0)
        		elif b.y0 == b.y1:
            			yset.add(b.y0)
        		else:
            			print "sloped line", b
    		elif type(b) == LTRect: 
        		if b.x1 - b.x0 < 2.0:
            			xset.add(b.y0)
        		else:
            			yset.add(b.x0)
    		else:
        		assert False, "Unrecognized type: %s" % type(b)
	
	xlist = sorted(list(xset))
	ylist = sorted(list(yset))
	tboxes = [ [ [ ]  for xl in xlist ]  for yl in ylist ]
	for lt in tlines:
		y = (lt.y0 + lt.y1)/2
		iy = Wposition(ylist, y)
		previx = None
		for lct in lt:
			if type(lct) == LTAnon:
				continue  # a junk element in LTTextLineHorizontal
			x = (lct.x0+lct.x1)/2
        		ix = Wposition(xlist, x)
        		if previx != ix:
            			tboxes[iy][ix].append([])  # begin new chain of characters
            			previx = ix
        		tboxes[iy][ix][-1].append(lct.get_text())
	for iy in range(len(ylist)):
		for ix in range(len(xlist)):
			tboxes[iy][ix] = [ "".join(s)  for s in tboxes[iy][ix] ]
	headers = [" ".join(lh.strip()  for lh in h).strip()  for h in tboxes.pop() ]
	print headers
	
def Wposition(wlist, w):
    ilo, ihi = 0, len(wlist)
    while ilo < ihi -1:
        imid = (ilo + ihi) / 2
        if w < wlist[imid]:
            ihi = imid
        else:
            ilo = imid
    return ilo
