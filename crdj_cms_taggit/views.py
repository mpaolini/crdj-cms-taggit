# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from cms.models import Page
from cms.utils import get_language_from_request
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from crdj_cms_taggit.forms import UpdateTagsForm
from crdj_cms_taggit.api import set_page_tags

@login_required
def update_tags(request, page_id):
    # TODO: permessi di modifica alla pagina (tipo is_staff)
    # TODO: visualizza errori
    # TODO: gestisci ajax
    page = get_object_or_404(Page, pk=page_id)
    if request.method == 'POST':
        form = UpdateTagsForm(request.POST)
        if form.is_valid():
            set_page_tags(page, form.cleaned_data['tags'])
        else:
            # TODO: visualizza errori form
            pass
    # TODO: get_abslute_url è giusto?
    return HttpResponseRedirect(page.get_absolute_url(language=get_language_from_request(request)))
