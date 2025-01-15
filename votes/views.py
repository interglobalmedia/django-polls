from django.db.models import F
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views.generic import DetailView, ListView

from .models import Choice, Question


# Create your views here.
class VotesIndexView(ListView):
    template_name = "votes/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by(
            "-pub_date"
        )[:5]


class VotesDetailView(DetailView):
    model = Question
    template_name = "votes/detail.html"

    def get_object(self, queryset=None):
        question = super().get_object(queryset=queryset)
        if question.pub_date > timezone.now():
            raise Http404("Question not yet published")
        return question


class VotesResultsView(DetailView):
    model = Question
    template_name = "votes/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "votes/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("votes:results", args=(question.id,)))
