from django import forms
from app.models import Article


class CreateArticleForm(forms.Form):
    ARTICLE_STATUS = (
        ("draft", "draft"),
        ("inprogress", "inprogress"),
        ("published", "published"),
    )
    title = forms.CharField(max_length=100)
    status = forms.CharField(choices=ARTICLE_STATUS)
    content = forms.CharField(widget=forms.Textarea)
    word_count = forms.IntegerField()
    twitter_post = forms.CharField(widget=forms.Textarea, required=False)
    # class Meta:
    #     model = Article
    #     fields = ("title", "status", "content", "word_count", "twitter_post")
