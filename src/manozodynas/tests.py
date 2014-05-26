# encoding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse
from manozodynas.testutils import StatefulTesting
from manozodynas.models import WordWithoutTranslation

class IndexTestCase(StatefulTesting):
    def test_index_page(self):
        self.open(reverse('index'))
        self.assertStatusCode(200)


class WordWithoutTranslationTests(TestCase):
    """WordWithoutTranslation model tests"""

    def test_str(self):

        wordwithouttranslation = WordWithoutTranslation(word = "kafkesque",
                context = 'utilised in snobbish milieu')

        
        self.assertEquals(
            str(wordwithouttranslation),
            'kafkesque', 'utilised in snobbish milieu',
        )
