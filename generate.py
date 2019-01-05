from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML

import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch




if __name__ == "__main__":
	doc = SimpleDocTemplate("form_letter.pdf",pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)

	styles=getSampleStyleSheet()
	formatted_time = time.ctime()
	Story = []
	styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
	ptext = '<font size=12>%s</font>' % formatted_time
 
	Story.append(Paragraph(ptext, styles["Normal"]))
	Story.append(Spacer(1, 12))


	doc.build(Story)