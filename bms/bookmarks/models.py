from bs4 import BeautifulSoup
from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from urllib.error import HTTPError
from urllib.parse import urlparse
from urllib.request import urlopen


class Page(models.Model):
    url = models.URLField('URL')
    fqdn = models.CharField('完全修飾ドメイン名', max_length=140, editable=False)
    title = models.CharField(
        'タイトル',
        max_length=140,
        editable=False)
    updated_date = models.DateTimeField('更新日時', auto_now=True)
    created_date = models.DateTimeField('登録日時', auto_now_add=True)

    def save(self, *args, **kwargs):
        # retrieve FQDN
        result = urlparse(self.url)
        self.fqdn = result.netloc

        # retrieve title
        if not self.title:
            try:
                with urlopen(self.url) as response:
                    soup = BeautifulSoup(response.read())
                self.title = soup.title and soup.title.string
            except HTTPError:
                self.title = ''
        self.clean_fields()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = 'ページ'


class Bookmark(models.Model):
    user = models.ForeignKey(User, verbose_name=User._meta.verbose_name)
    page = models.ForeignKey(Page, verbose_name=Page._meta.verbose_name)
    name = models.CharField('名前', max_length=50, blank=True)
    tags = TaggableManager()
    comment = models.TextField('コメント', max_length=140)
    star = models.BooleanField('スター')
    archived = models.BooleanField('アーカイブ')
    updated_date = models.DateTimeField('更新日時', auto_now=True)
    created_date = models.DateTimeField('登録日時', auto_now_add=True)

    def save(self, *args, **kwargs):
        # retrieve name
        self.name = self.name or self.page.title

        self.clean_fields()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = 'ブックマーク'
