RESUME_HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{ data.name }} - Technical Portfolio</title>
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    body { font-family: 'Inter', sans-serif; background-color: #0f172a; color: #cbd5e1; margin: 0; padding: 40px 20px; line-height: 1.6; }
    .container { max-width: 850px; margin: 0 auto; background: #1e293b; padding: 50px; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
    .header { text-align: center; border-bottom: 2px solid #38bdf8; padding-bottom: 25px; margin-bottom: 35px; }
    h1 { margin: 0; color: #f8fafc; font-size: 38px; font-weight: 700; letter-spacing: -0.5px; }
    .contact { font-size: 15px; color: #94a3b8; margin-top: 12px; font-weight: 500; }
    .contact a { color: #14b8a6; text-decoration: none; transition: color 0.2s ease-in-out; }
    .contact a:hover { color: #5eead4; }
    h2 { color: #38bdf8; border-bottom: 1px dashed #475569; font-size: 20px; margin-top: 40px; text-transform: uppercase; letter-spacing: 1.5px; padding-bottom: 8px; font-weight: 600; }
    .item { margin-bottom: 24px; page-break-inside: avoid; background: #0f172a; padding: 20px 25px; border-radius: 8px; border-left: 4px solid #14b8a6; transition: transform 0.2s ease; }
    .item:hover { transform: translateX(4px); }
    .item-title-row { display: flex; justify-content: space-between; align-items: baseline; font-weight: 700; font-size: 17px; color: #f1f5f9; }
    .meta-row { display: flex; justify-content: space-between; font-style: italic; color: #5eead4; font-size: 14px; margin-bottom: 12px; margin-top: 6px; }
    ul { margin: 10px 0 0 20px; padding: 0; }
    li { font-size: 14.5px; margin-bottom: 8px; color: #cbd5e1; }
    .skills-container { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 15px; }
    .skill-tag { background: rgba(20, 184, 166, 0.1); color: #5eead4; padding: 6px 16px; border-radius: 20px; font-size: 13.5px; font-weight: 600; border: 1px solid rgba(20, 184, 166, 0.3); }
    p { font-size: 14.5px; margin: 12px 0 0 0; color: #cbd5e1; line-height: 1.7; }
    @media print {
        body { background: white; color: black; padding: 0; margin: 0; }
        .container { background: white; padding: 20px; box-shadow: none; border-radius: 0; }
        h1, h2, .item-title-row { color: black; }
        .header { border-bottom: 2px solid black; }
        .item { background: white; border-left: 2px solid black; padding: 10px 15px; }
        .skill-tag { border: 1px solid black; color: black; background: white; }
        .meta-row { color: #444; }
    }
</style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{{ data.name }}</h1>
            <div class="contact">
                📧 {{ data.email }} &nbsp;|&nbsp; 
                🔗 <a href="{{ data.linkedin }}" target="_blank">{{ data.linkedin }}</a>
            </div>
        </div>
        <h2>🛠️ Core Technical Skills</h2>
        <div class="skills-container">
            {% for skill in data.skills %}
            <span class="skill-tag">{{ skill }}</span>
            {% endfor %}
        </div>
        <h2>💼 Professional Experience</h2>
        {% for exp in data.experience %}
        <div class="item">
            <div class="item-title-row">
                <span>{{ exp.role }}</span>
                <span>{{ exp.company }}</span>
            </div>
            <div class="meta-row">
                <span>Tasks & Achievements</span>
                <span>{{ exp.duration }}</span>
            </div>
            <ul>
                {% for bullet in exp.bullets %}
                <li>{{ bullet }}</li>
                {% endfor %}
            </ul>
        </div>
        {% endfor %}
        <h2>🚀 Featured Engineering Projects</h2>
        {% for proj in data.projects %}
        <div class="item">
            <div class="item-title-row">
                <span>{{ proj.title }}</span>
            </div>
            <div class="meta-row">
                <span>Technologies Used: {{ proj.technologies | join(', ') }}</span>
            </div>
            <p>{{ proj.description }}</p>
        </div>
        {% endfor %}
        <h2>🎓 Education Profile</h2>
        {% for edu in data.education %}
        <div class="item">
            <div class="item-title-row">
                <span>{{ edu.degree }}</span>
                <span>{{ edu.year }}</span>
            </div>
            <div class="meta-row">
                <span>{{ edu.institution }}</span>
                <span>{{ edu.gpa_or_details if edu.gpa_or_details else '' }}</span>
            </div>
        </div>
        {% endfor %}
    </div>
</body>
</html>
"""
