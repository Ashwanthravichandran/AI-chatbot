from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'Public Sector Organization - Employee Guide', 0, 1, 'C')
        self.ln(5)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.multi_cell(0, 8, title)
        self.ln(2)

    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 6, body)
        self.ln(4)

# Create PDF instance
pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Document Sections
sections = {
    "1. Introduction": "This document provides important information for employees of a large public sector organization...",
    "2. Human Resources (HR) Policies": "Employees are entitled to various types of leave to support work-life balance...",
    "2.1 Employee Leave Policy": "Annual Leave: Employees are entitled to 20 days of paid annual leave each year...",
    "2.2 Leave Application Process": "To apply for leave, log in to the Employee HR Portal, select Leave Application...",
    "2.3 Employee Conduct Policy": "Employees must maintain professional conduct at all times...",
    "3. IT Support and Technology Guidelines": "The IT department provides support for computer issues, network connectivity...",
    "3.1 IT Helpdesk Services": "Employees can contact IT support via email: it_support@organization.com...",
    "3.2 Password Management Policy": "Passwords must be at least 8 characters, include numbers and symbols...",
    "3.3 Acceptable Use of Technology": "Employees should use organizational technology responsibly...",
    "4. Company Events and Activities": "Public sector organizations regularly conduct events to promote employee engagement...",
    "4.1 Annual Employee Meet": "The next Annual Employee Meet will include awards, team-building exercises...",
    "4.2 Training Programs": "Employees are encouraged to participate in training for professional development...",
    "4.3 Wellness Programs": "Employee wellness is supported through health check-ups, stress management workshops...",
    "5. Workplace Communication Guidelines": "Use official email, respond promptly, maintain professionalism...",
    "6. Data Privacy and Security": "Employees must protect organizational data and report breaches immediately...",
    "7. Employee Support Services": "HR consultation, IT support, training programs, grievance system are available...",
    "8. Emergency Procedures": "Fire Emergency: remain calm, follow evacuation. Medical Emergency: contact medical team...",
    "9. Frequently Asked Questions": "Q: How do I apply for leave? A: Use the HR portal. Q: Computer not working? A: Contact IT...",
    "10. Conclusion": "This document provides a general overview of organizational policies and employee services..."
}

# Add content
for title, body in sections.items():
    pdf.chapter_title(title)
    pdf.chapter_body(body)

# Save PDF
pdf.output("Employee_Information_Guide.pdf")

print("PDF generated successfully!")