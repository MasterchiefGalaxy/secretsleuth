import json
from jinja2 import Environment, FileSystemLoader

def generate_report(findings, report_type='html'):
    if report_type == 'json':
        with open('report.json', 'w') as f:
            json.dump(findings, f, indent=4)
    else:
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template('report_template.html')
        report_content = template.render(findings=findings)
        with open('report.html', 'w') as f:
            f.write(report_content)

# Example HTML template (save as report_template.html)
"""
<!DOCTYPE html>
<html>
<head>
    <title>SecretSleuth Report</title>
</head>
<body>
    <h1>SecretSleuth Findings</h1>
    <table>
        <tr>
            <th>Type</th>
            <th>Pattern</th>
            <th>Match</th>
            <th>File</th>
        </tr>
        {% for finding in findings %}
        <tr>
            <td>{{ finding.type }}</td>
            <td>{{ finding.pattern }}</td>
            <td>{{ finding.match }}</td>
            <td>{{ finding.file }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""
