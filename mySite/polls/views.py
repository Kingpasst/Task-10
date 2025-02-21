from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Choice
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    """
    Displays the latest five questions in the polls.

    Args:
        request: The HTTP request object.

    Returns:
        Rendered HTML template displaying the latest questions.
    """
    latest_questions = Question.objects.order_by('-pub_date')[:5]  # Latest 5 questions
    return render(request, 'polls/index.html', {'latest_questions': latest_questions})


@login_required
def detail(request, question_id):
    """
    Displays the details of a specific question.

    Args:
        request: The HTTP request object.
        question_id: The ID of the question to retrieve.

    Returns:
        Rendered HTML template displaying the question details.

    Raises:
        Http404: If the question does not exist.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


@login_required
def vote(request, question_id):
    """
    Processes the vote for a specific question.

    Args:
        request: The HTTP request object.
        question_id: The ID of the question being voted on.

    Returns:
        Redirects to the results page after processing the vote.

    Raises:
        Http404: If the question does not exist.
        KeyError: If no choice is selected.
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('polls:results', question_id=question.id)


@login_required
def results(request, question_id):
    """
    Displays the results of a specific question.

    Args:
        request: The HTTP request object.
        question_id: The ID of the question whose results are to be displayed.

    Returns:
        Rendered HTML template displaying the results of the question.

    Raises:
        Http404: If the question does not exist.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
