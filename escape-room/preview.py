# Rasterize pages of a PDF to PNG for visual checking: python3 preview.py pdf/x.pdf [pages] [dpi]
import sys, fitz
src=sys.argv[1]; pages=sys.argv[2] if len(sys.argv)>2 else 'all'; dpi=int(sys.argv[3]) if len(sys.argv)>3 else 70
doc=fitz.open(src); n=doc.page_count
idx=range(n) if pages=='all' else [int(p)-1 for p in pages.split(',')]
for i in idx:
    out=src.replace('.pdf',f'_p{i+1}.png'); doc[i].get_pixmap(dpi=dpi).save(out); print(out)
print('pages:',n)
