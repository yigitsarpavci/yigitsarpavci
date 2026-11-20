#!/usr/bin/env python3
"""Post-process the compiled CV so ATS / copy-paste text extraction is clean.

The Source Sans Pro hyphen glyph is mapped to U+2011 (non-breaking hyphen) in the PDF's
ToUnicode CMaps, so parsers read "x86-64" or "full-stack" with a non-ASCII hyphen and keyword
matching can miss them. This rewrites that mapping to the ASCII hyphen-minus (U+002D).
It changes only the invisible text layer, never the rendering.

Usage: python3 fix_pdf_text.py Yigit_Sarp_Avci_CV.pdf   (requires: pip install pymupdf)
"""
import re
import sys

import pymupdf


def main(path: str) -> int:
    doc = pymupdf.open(path)
    patched = 0
    for xref in range(1, doc.xref_length()):
        try:
            if doc.xref_get_key(xref, "Type")[1] != "/Font":
                continue
            kind, value = doc.xref_get_key(xref, "ToUnicode")
            if kind != "xref":
                continue
            cmap_xref = int(value.split()[0])
            data = doc.xref_stream(cmap_xref).decode("latin1")
            new = re.sub(r"(<[0-9A-Fa-f]+>)\s+<2011>", r"\1 <002D>", data)
            if new != data:
                doc.update_stream(cmap_xref, new.encode("latin1"))
                patched += 1
        except Exception:
            continue
    doc.save(path + ".tmp", garbage=3, deflate=True)
    doc.close()
    import os
    os.replace(path + ".tmp", path)
    print(f"patched {patched} ToUnicode map(s) in {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "Yigit_Sarp_Avci_CV.pdf"))
