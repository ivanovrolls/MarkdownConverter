import mistune
def cv_data(md_text):
    resume = {
        'name': "",
        'email': "",
        'phone': "",
        'website': "",
        'summary': "",
        'jobs': [],
        'skills': [],
    }

    lines = md_text.split('\n')
    current_section = None
    job = None

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if line.startswith('# '):
            resume['name'] = line[2:].strip()
        elif line.startswith('**Email:**'):
            resume['email'] = line[len('**Email:**'):].strip()
        elif line.startswith('**Phone:**'):
            resume['phone'] = line[len('**Phone:**'):].strip()
        elif line.startswith('**Website:**'):
            resume['website'] = line[len('**Website:**'):].strip()

        #sections
        elif line.startswith('## Summary'):
            current_section = 'summary'
            resume['summary'] = ""
        elif line.startswith('## Work Experience'):
            current_section = 'work_experience'
        elif line.startswith('## Skills'):
            current_section = 'skills'
        elif line.startswith('## Education'):
            current_section = 'education'

        elif current_section == 'summary':
            resume['summary'] += line + " "

        elif current_section == 'work_experience':
            if line.startswith('### '):
                if job:
                    resume['jobs'].append(job)
                job = {
                    'title': '',
                    'company': '',
                    'location': '',
                    'start_date': '',
                    'end_date': '',
                    'description': []
                }
                parts = line[4:].split('—')
                job['title'] = parts[0].strip()
                if len(parts) > 1:
                    job['company'] = parts[1].strip()

            elif job and '|' in line:
                parts = line.split('|')
                job['location'] = parts[0].strip().strip('*')
                dates = parts[1].strip().split('to')
                job['start_date'] = dates[0].strip()
                if len(dates) > 1:
                    job['end_date'] = dates[1].strip()

            elif job and line.startswith('- '):
                job['description'].append(line[2:].strip())

        elif current_section == 'education':
            if line.startswith('### '):
                edu = {
                    'degree': '',
                    'school': '',
                    'location': '',
                    'start_date': '',
                    'end_date': ''
                }
                parts = line[4:].split('—')
                edu['degree'] = parts[0].strip()
                if len(parts) > 1:
                    edu['school'] = parts[1].strip()
                resume.setdefault('education', []).append(edu)

            elif resume.get('education'):
                edu = resume['education'][-1]
                parts = line.split('|')
                if len(parts) == 2:
                    edu['location'] = parts[0].strip().strip('*')
                    dates = parts[1].strip().split('to')
                    edu['start_date'] = dates[0].strip()
                    if len(dates) > 1:
                        edu['end_date'] = dates[1].strip()

        elif current_section == 'skills':
            if line.startswith('- '):
                resume['skills'].append(line[2:].strip())

    if job:
        resume['jobs'].append(job)
    resume['summary'] = resume['summary'].strip()

    return resume
