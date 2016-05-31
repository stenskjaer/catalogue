from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Text
from manuscripts.models import ManuscriptContentCommentary, ManuscriptInspection


class IndexView(generic.ListView):
    template_name = 'texts/index.html'
    context_object_name = 'text_list'

    def get_queryset(self):
        """Return all text objects.
        """
        return Text.objects.all()


class Details(generic.DetailView):
    model = Text
    template_name = 'texts/detail.html'
    context_object_name = 'text_detail'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(Details, self).get_context_data(**kwargs)
        # Add a QuerySet of text witnesses
        context['witnesses'] = ManuscriptContentCommentary.objects.all()
        return context


class Inspected(generic.ListView):
    model = Text
    template_name = 'texts/inspections.html'
    context_object_name = 'texts'

    def get_queryset(self):
        # First, get all the inspected manuscripts
        inspection_ids = [inspection.manuscript.id for inspection in ManuscriptInspection.objects.all()]
        # Then, read all texts (on De anima) into memory
        all_texts = Text.objects.select_related().filter(commentary_on=148)
        # Find the content that has been inspected
        inspected_list = []
        for item in ManuscriptContentCommentary.objects.select_related().all():
            if item.manuscript.id in inspection_ids:
                inspected_list.append(item.content.id)

        # Sort the list of relevant texts into relevance lists
        text_list = {}
        text_list['high_relevance'] = []
        text_list['some_relevance'] = []
        text_list['low_relevance']  = []
        text_list['no_relevance']   = []
        text_list['unknown'] = []
        for text in all_texts:
            if text.id in inspected_list:
                if text.relevance == Text.RELEVANCE_HIGH:
                    text_list['high_relevance'].append(text)
                elif text.relevance == Text.RELEVANCE_MID:
                    text_list['some_relevance'].append(text)
                elif text.relevance == Text.RELEVANCE_LOW:
                    text_list['low_relevance'].append(text)
                elif text.relevance == Text.RELEVANCE_NONE:
                    text_list['no_relevance'].append(text)
                elif text.relevance == Text.RELEVANCE_UNKNOWN:
                    text_list['unknown'].append(text)
        text_list['total_count'] = len(
            text_list['high_relevance'] +
            text_list['some_relevance'] +
            text_list['low_relevance']  +
            text_list['no_relevance']   +
            text_list['unknown']
        )
        return(text_list)

class Relevant(generic.ListView):
    model = Text
    template_name = 'texts/relevant.html'
    context_object_name = 'texts'


    def get_queryset(self):
        # Read all texts (on De anima) into memory
        all_texts = Text.objects.select_related().filter(commentary_on=148)

        # Sort the list of relevant texts into relevance lists
        text_list = {}
        text_list['high_relevance'] = []
        text_list['some_relevance'] = []
        text_list['low_relevance']  = []
        text_list['no_relevance']   = []
        text_list['unknown'] = []
        for text in all_texts:
            if text.relevance == Text.RELEVANCE_HIGH:
                text_list['high_relevance'].append(text)
            elif text.relevance == Text.RELEVANCE_MID:
                text_list['some_relevance'].append(text)
            elif text.relevance == Text.RELEVANCE_LOW:
                text_list['low_relevance'].append(text)
            elif text.relevance == Text.RELEVANCE_NONE:
                text_list['no_relevance'].append(text)
            elif text.relevance == Text.RELEVANCE_UNKNOWN:
                text_list['unknown'].append(text)
        text_list['total_count'] = len(
            text_list['high_relevance'] +
            text_list['some_relevance'] +
            text_list['low_relevance']  +
            text_list['no_relevance']   +
            text_list['unknown']
        )
        return(text_list)
