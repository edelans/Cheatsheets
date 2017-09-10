# shrinking pdf size

        gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dDownsampleColorImages=true
-dColorImageResolution=150 -dNOPAUSE  -dBATCH -sOutputFile=output.pdf input.pdf

see https://askubuntu.com/a/407630/294354


# Merging PDF

        gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=merged.pdf mine1.pdf mine2.pdf

# Watermarking

<<<<<<< HEAD
        pdftk input.pdf stamp watermark.pdf output final.pdf
=======
        pdftk 1_20140120\ CNI\ Ed2.pdf stamp watermark.pdf output final.pdf
>>>>>>> 2e901494afd02c01eb2a6b5ea51013fe3cc5e4bb
