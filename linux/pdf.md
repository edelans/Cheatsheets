# shrinking pdf size

        gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dDownsampleColorImages=true
-dColorImageResolution=150 -dNOPAUSE  -dBATCH -sOutputFile=output.pdf input.pdf

see https://askubuntu.com/a/407630/294354


# Merging PDF

        gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=merged.pdf mine1.pdf mine2.pdf

# Watermarking

        pdftk 1_20140120\ CNI\ Ed2.pdf stamp watermark.pdf output final.pdf
