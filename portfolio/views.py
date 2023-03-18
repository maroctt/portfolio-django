from django.shortcuts import render

def about(request):
    return render(request, 'about.html', {})


def projects(request):
    projects = [
        {'title': 'P000',
         'code':'#',
         'demo':'#',
         'image':'assets/p000.jpg'
        },
        {'title': 'P001',
         'code':'#',
         'demo':'#',
         'image':'assets/p001.jpg'
        },
        {'title': 'P002',
         'code':'#',
         'demo':'#',
         'image':'assets/p002.jpg'
        },
        {'title': 'P003',
         'code':'#',
         'demo':'#',
         'image':'assets/p003.jpg'
        },
        {'title': 'P004',
         'code':'#',
         'demo':'#',
         'image':'assets/p004.jpg'
        },
        {'title': 'P005',
         'code':'#',
         'demo':'#',
         'image':'assets/p005.jpg'
        }
    ]
    context = {'projects':projects}
    return render(request, 'projects.html', context)