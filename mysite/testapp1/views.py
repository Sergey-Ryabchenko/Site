from django.shortcuts import render

from testapp1.models import Worker



def index_page(request):
    # new_worker = Worker(name='Sarah', surname='Connor', salary=2)
    # new_worker.save()

    # Worker.objects.create(name='T', surname='800', salary=300)

    # x = Worker.objects.get(id=4)
    # x.name = 'T-800'
    # x.surname = 'Skynetson'
    # x.save()

    # Worker.objects.get(id=3).delete()

    all_workers = Worker.objects.all()
    for i in all_workers:
        print(i.name, i.surname, i.salary, i.id)
    return render(request, 'index.html')
# Create your views here.
