# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 16:01:14 2020

@author: heart
"""

# Performing the following steps to install ReportLab if you do not have 
"""
$ wget http://www.reportlab.org/ftp/ReportLab_2_3.tar.gz
$ tar xvfz ReportLab_2_3.tar.gz
$ cd ReportLab_2_3
$ sudo python setup.py install

""" 

from reportlab.pdfgen.canvas import Canvas

# select the canvas of letter page size
from reportlab.lib.pagesizes import letter

pdf = Canvas("bond.pdf", pagesize = letter)

# import units
from reportlab.lib.units import cm, mm, inch, pica

pdf.setFont("Courier", 60)
pdf.setFillColorRGB(1, 0, 0)
pdf.drawCentredString(letter[0] / 2, inch * 6, "MI6 Classified")
pdf.setFont("Courier", 40)
pdf.drawCebtredString(letter[0] / 2, inch * 5, "For 007's Eyes Only")

# Close the drawing for current page
pdf.showPage()

# Save the pdf page
pdf.save()