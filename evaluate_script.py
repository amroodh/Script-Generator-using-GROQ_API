from sklearn.metrics import f1_score, precision_score, recall_score
from fpdf import FPDF
import random

def evaluate_script(true_scripts, generated_script):
    true_script = random.choice(true_scripts)
    true_scripts = [true_script]
    generated_scripts = [generated_script.strip()]
    f1 = f1_score(true_scripts, generated_scripts, average='weighted', zero_division=1)
    precision = precision_score(true_scripts, generated_scripts, average='weighted', zero_division=1)
    recall = recall_score(true_scripts, generated_scripts, average='weighted', zero_division=1)
    true_positives = sum([1 for true, gen in zip(true_scripts, generated_scripts) if true == gen])
    false_positives = sum([1 for true, gen in zip(true_scripts, generated_scripts) if true != gen])
    return f1, precision, recall, true_positives, false_positives

def generate_pdf(generated_script, f1, precision, recall, true_positives, false_positives):
    class PDF(FPDF):
        def header(self):
            self.set_font('Arial', 'B', 12)
            self.cell(0, 10, 'Evaluation Metrics', 0, 1, 'C')

        def chapter_title(self, title):
            self.set_font('Arial', 'B', 12)
            self.cell(0, 10, title, 0, 1, 'L')
            self.ln(10)

        def chapter_body(self, body):
            self.set_font('Arial', '', 12)
            self.multi_cell(0, 10, body)
            self.ln()

    pdf = PDF()
    pdf.add_page()
    pdf.chapter_title('Generated Script')
    pdf.chapter_body(generated_script)
    pdf.chapter_title('Evaluation Metrics')
    metrics = f"F1 Score: {f1}\nPrecision: {precision}\nRecall: {recall}\nTrue Positives: {true_positives}\nFalse Positives: {false_positives}"
    pdf.chapter_body(metrics)
    pdf.output('evaluation_metrics.pdf')
