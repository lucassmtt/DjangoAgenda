from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from contact.models import Contact


def index_view(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')[:10]

    context = {
        'contacts': contacts,
        'site_title': 'Contatos - '
    }

    return render(
        request=request,
        template_name='contact/index.html',
        context=context
    )


def contact_view(request, contact_id):
    """
        We can raise an exception with this way:

    try:
        contact = Contact.objects.get(pk=contact_id)
        context = {
            'contact': contact
        }
        return render(
            request,
            'contact/contact.html',
            context
        )
    except Contact.DoesNotExist:
        raise Http404

        Or like this:
    """
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    # flake8: noqa
    # contact = get_object_or_404(Contact.objects.filter(pk=contact_id, show=True)) We can put the manager
    site_title = f'{contact.first_name} {contact.last_name} - '
    return render(
        request,
        'contact/contact.html',
        {
            'contact': contact,
            'site_title': site_title,
        }
    )


def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')

    contacts = Contact.objects \
        .filter(show=True) \
        .filter(
            Q(first_name__contains=search_value)
            |  # logic operator or
            Q(last_name__contains=search_value) |
            Q(phone__contains=search_value) |
            Q(email__contains=search_value)
        ) \
        .order_by('-id') \


    context = {
        'contacts': contacts,
        'site_title': 'Search - ',
        'search_value': search_value,
    }

    return render(
        request,
        'contact/index.html',
        context
    )
