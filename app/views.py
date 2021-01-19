from django.shortcuts import render
from django.conf import settings
from .models import Questions
from .forms import QuestionForm
import wikipedia


def index(request):
    if request.method == "POST":
        prediction_score = 0.0
        answer = "There was an error!"
        form = QuestionForm(request.POST)
        if form.is_valid():

            try:
                question = form.cleaned_data["question"]
                wiki_terms = form.cleaned_data['wiki_terms']
                print(question, wiki_terms)
                wikipedia.set_lang('en')
                wiki_text = wikipedia.summary(wiki_terms)
                result = settings.BERT_PIPELINE(
                    question=question, context=wiki_text)
                answer = result['answer']
                prediction_score = result['score']

                q = Questions()
                q.wiki_text = wiki_text
                q.wiki_terms = wiki_terms
                q.question = question
                q.answer = answer
                q.prediction_score = prediction_score
                q.save()

            except:
                answer = "There was an error!"
        return render(request, "main/index.html", {'form': form,
                                                   'answer': answer, 'score': prediction_score})

    else:
        form = QuestionForm()
        return render(request, 'main/index.html', {'form': form})
