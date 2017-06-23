from django import forms

from .models import Page, Bookmark

class BookmarkForm(forms.ModelForm):
    url = forms.URLField(label='URL')

    def save(self, *args, **kwargs):
        url = self.clean_data['url']
        self.instanse.page, created = Page.objects.get_or_create(url=url)
        super().save(*args, **kwargs)

    class Meta:
        model = Bookmark
        fields = (
            'name',
            'url',
            'tags',
            'comment',
            )

