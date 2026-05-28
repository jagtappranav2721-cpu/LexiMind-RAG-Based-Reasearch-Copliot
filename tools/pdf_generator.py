import os
import re
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def markdown_to_html(text):
    """Convert simple markdown to reportlab-supported HTML tags."""
    # Bold
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    # Italics
    text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)
    # Remove remaining markdown chars if needed, or handle inline code
    text = re.sub(r'`(.*?)`', r'<font name="Courier">\1</font>', text)
    return text

def generate_professional_pdf(query, answer, web_context=None, pdf_context=None):
    """
    Generates a professional research report PDF using ReportLab.
    Returns the file path of the generated PDF.
    """
    filename = f"Research_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=50,
        leftMargin=50,
        topMargin=50,
        bottomMargin=50
    )

    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'MainTitle',
        parent=styles['Title'],
        fontName='Helvetica-Bold',
        fontSize=24,
        spaceAfter=12,
        textColor=colors.HexColor('#1f497d')
    )
    
    subtitle_style = ParagraphStyle(
        'SubTitle',
        parent=styles['Heading2'],
        fontName='Helvetica-Oblique',
        fontSize=14,
        spaceAfter=20,
        textColor=colors.HexColor('#555555')
    )

    heading_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=14,
        spaceBefore=15,
        spaceAfter=10,
        textColor=colors.HexColor('#2c3e50'),
        borderPadding=5,
        borderWidth=0,
        borderColor=colors.HexColor('#bdc3c7')
    )
    
    body_style = ParagraphStyle(
        'BodyText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        spaceAfter=10,
        leading=16
    )

    bullet_style = ParagraphStyle(
        'BulletText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=16,
        leftIndent=20,
        firstLineIndent=-10,
        spaceAfter=5
    )

    story = []

    # 1. TITLE SECTION
    story.append(Paragraph("AI Research Report", title_style))
    story.append(Paragraph(f"Query: {query}", subtitle_style))
    story.append(Paragraph(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", body_style))
    story.append(Spacer(1, 20))

    # Parse and format the answer text
    lines = answer.split('\n')
    
    in_list = False
    list_items = []

    def flush_list():
        nonlocal in_list, list_items
        if in_list and list_items:
            story.append(ListFlowable(list_items, bulletType='bullet', leftIndent=15, spaceAfter=10))
            list_items = []
            in_list = False

    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Parse Headings
        if line.startswith('### ') or line.startswith('## ') or line.startswith('# '):
            flush_list()
            heading_text = line.lstrip('#').strip()
            story.append(Paragraph(heading_text.upper(), heading_style))
        
        # Parse Bullet Points
        elif line.startswith('- ') or line.startswith('* '):
            in_list = True
            item_text = markdown_to_html(line[2:].strip())
            list_items.append(ListItem(Paragraph(item_text, body_style)))
            
        elif re.match(r'^\d+\.\s', line):
            in_list = True
            # Strip the number and space
            item_text = markdown_to_html(re.sub(r'^\d+\.\s', '', line).strip())
            list_items.append(ListItem(Paragraph(item_text, body_style)))
            
        # Parse Normal Paragraphs
        else:
            flush_list()
            formatted_text = markdown_to_html(line)
            story.append(Paragraph(formatted_text, body_style))

    flush_list()
    
    story.append(Spacer(1, 20))
    story.append(PageBreak())

    # 5. OPTIONAL CONTEXT SECTION
    story.append(Paragraph("SOURCES USED", heading_style))
    
    if web_context and web_context != "Not provided":
        story.append(Paragraph("<b>Web Sources</b>", body_style))
        for ctx_line in web_context.split('\n'):
            if ctx_line.strip():
                story.append(Paragraph(markdown_to_html(ctx_line), body_style))
        story.append(Spacer(1, 10))

    if pdf_context and pdf_context != "Not provided":
        story.append(Paragraph("<b>Document Sources</b>", body_style))
        # Avoid dumping the entire raw text if it's too long, truncate or dump raw
        for ctx_line in pdf_context.split('\n'):
            if ctx_line.strip():
                story.append(Paragraph(markdown_to_html(ctx_line), body_style))
    
    # Build PDF
    doc.build(story)
    
    return filename
