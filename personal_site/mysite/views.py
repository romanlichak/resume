from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import PersonalData, Experience, Education, Skill, DesireRole, AddEducation
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.views.decorators.http import require_POST
from taggit.models import Tag
from django.db.models import Count
from .forms import EmailPostForm



def resume_list(request):
    exp = Experience.objects.all()
    person = PersonalData.objects.all()
    desire = DesireRole.objects.all()
    edu = Education.objects.all()
    addedu = AddEducation.objects.all()
    skl = Skill.objects.all()

    lst = []

    for c in exp:
        lst.append(c)

    #return render(request,'mysite/resume/list.html',{'exp': exp})
    return render(request,'mysite/resume/test.html',
                  {'exp': exp[0],
                   'exp1': exp[1],
                   'person':person,
                    'desire': desire,
                   'comp' : lst[0],
                   'edu':edu[2],
                   'edu1': edu[1],
                   'edu2': edu[0],
                   'addedu':addedu[0],
                   'addedu1':addedu[1],
                   'skl':skl[0]
                   })


def list(request):
    exp = Experience.objects.all()

    return render(request,'mysite/resume/list.html',{'exp': exp})


def resume_detail(request, id2):
    exp = get_object_or_404(Experience,
                            id=id2,)

    return render(request, 'mysite/resume/detail.html', {'exp': exp})


def invitation(request):
    # Retrieve post by id
    # post = Experience.objects.all()
    sent = False

    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
       # prj = Project.describe
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data

            # post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read "
            message = f"Read s comments: {cd['comments']}"
            send_mail(subject, message, 'lichakroman9@gmail.com', [cd['to']])
            sent = True

    else:
        form = EmailPostForm()
    return render(request, 'mysite/resume/invite.html', {
                                                    'form': form,
                                                    'sent': sent})











