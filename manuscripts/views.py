from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from manuscripts.models import Manuscript, ManuscriptContentCommentary
import datetime


class IndexView(generic.ListView):
    template_name = 'manuscripts/index.html'
    context_object_name = 'manuscripts'

    def get_queryset(self):
        """Return all text objects.
        """
        return Manuscript.objects.select_related().filter(manuscriptinspection__inspection_date__lte=datetime.date.today()).order_by('-manuscriptinspection__inspection_date')


class DetailView(generic.DetailView):
    model = Manuscript
    template_name = 'manuscripts/detail.html'
    context_object_name = 'manuscript'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(DetailView, self).get_context_data(**kwargs)
        # Add a QuerySet of text witnesses
        context['content'] = ManuscriptContentCommentary.objects.all()
        return context

