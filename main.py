from flask import Flask, render_template, request
from parsepdf import convert_pdf_to_html

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def pdf_():
    if request.method == 'POST':
        f = request.files['pdf']
        f.save('temp.pdf')
        markup = """
            <form id="fileform" action="/" method="POST" enctype="multipart/form-data" style="margin-bottom:0">
                <input type="file" name="pdf" id="pdfinput">
                <input type="submit" value="submit">
            </form>
            <button id="highlightBtn">save</button>
            <a href="/highlights">Highlights page</a>
        """
        markup += convert_pdf_to_html(open('temp.pdf', 'rb'))
        markup += """
            <script>
                let currentSelection = ''
                document.addEventListener('DOMContentLoaded', () => {
                    if (!JSON.parse(localStorage.getItem('highlights'))) {
                        localStorage.setItem('highlights', '[]')
                    }
                    document.addEventListener('mouseup', () => {
                        currentSelection = window.getSelection().toString()
                    })
                    document.getElementById('highlightBtn').addEventListener('click', () => {
                        let existing = JSON.parse(localStorage.getItem('highlights'))
                        existing.push( { text: currentSelection } )
                        localStorage.setItem('highlights', JSON.stringify(existing))
                    })
                })
            </script>

        """
        return markup
    return render_template('pdf.html')


@app.route('/highlights')
def highlights_():
    return render_template('highlights.html')




app.run(debug=True)