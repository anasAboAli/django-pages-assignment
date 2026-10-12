from datetime import date

from django.shortcuts import render


def index(request):
    # All the data is passed to the template through this dictionary (the context).
    context = {
        'first_name': 'anas',            # capfirst -> "Anas"
        'last_name': 'YourLastName',     # joined to the first name with the add filter
        'student_id': 120200000,         # stored as a number, shown as text with stringformat
        'address': 'Gaza, Palestine',    # shown in capitals with upper
        'email': '',                     # empty -> the default filter shows a fallback value
        'date_of_birth': date(2004, 1, 1),
        'university': 'Islamic University of Gaza',
        'faculty': 'Faculty of Information Technology',
        'major': 'Software Development',
        'level': 'Third Year',
        'skills': ['Python', 'Django', 'HTML', 'CSS', 'Git & GitHub'],
    }
    return render(request, 'pages/index.html', context)
