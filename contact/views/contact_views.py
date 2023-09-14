from django.shortcuts import render, get_object_or_404
from django.http import Http404

from contact.models import Contact


def index_view(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')[:10]

    context = {
        'contacts': contacts
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
    # contact = get_object_or_404(Contact.objects.filter(pk=contact_id, show=True)) We can put the manager
    return render(
        request,
        'contact/contact.html',
        {
            'contact': contact
        }
    )
