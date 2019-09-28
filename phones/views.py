from django.shortcuts import render
from phones.models import Apple, Samsung, Meizu


def show_catalog(request):
    template = 'catalog.html'
    phones = (Apple, Samsung, Meizu)
    phone_list = []
    for phone in phones:
        model = phone.objects.select_related()
        print(model)
        phone_list.append(model)

    context = {'phone_list': phone_list}
    return render(
        request,
        template,
        context
    )
