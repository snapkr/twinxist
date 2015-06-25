import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hello.settings") #Changed in DDS v.0.3

BOT_NAME = 'Websites'

SPIDER_MODULES = ['dynamic_scraper.spiders', 'scraper',]
USER_AGENT = '%s/%s' % (BOT_NAME, '1.0')

ITEM_PIPELINES = {
    'dynamic_scraper.pipelines.ValidationPipeline': 100,
    'dynamic_scraper.pipelines.DjangoImagesPipeline': 200,
    'scraper.pipelines.DjangoWriterPipeline': 400,
}
IMAGES_STORE = "/webapps/hello_django/static/scraped_images/thumbnails"
#IMAGES_STORE = os.path.join(PROJECT_ROOT, '../static/scraped_images/thumbnails')

IMAGES_THUMBS = {
    'small': (300, 300),
}
