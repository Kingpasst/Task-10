from django.db import models


class Question(models.Model):
    """
    Model representing a question in the poll.

    Attributes:
        question_text (CharField): The text of the question.
        pub_date (DateTimeField): The date the question was published.
    """

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """Return the string representation of the question."""
        return self.question_text


class Choice(models.Model):
    """
    Model representing a choice for a question.

    Attributes:
        question (ForeignKey): The question that this choice belongs to.
        choice_text (CharField): The text of the choice.
        votes (IntegerField): The number of votes for this choice.
    """

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)   
    votes = models.IntegerField(default=0)  

    def __str__(self):
        """Return the string representation of the choice."""
        return self.choice_text
