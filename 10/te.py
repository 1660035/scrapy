import re

import validators
from newspaper import Article


def is_url(url):
    return validators.url(url)


def crawl(url):
    if not is_url(url):
        result = {
            'url': url,
            'error': 'Url không hợp lệ!',
            'success': False
        }

        return result
    article = Article(url)
    article.download()
    article.parse()
    result = {'url': url, 'error': '','author':article.authors , 'success': True, 'title': article.title,
           'keywords': ', '.join(article.keywords if article.keywords else (
               article.meta_keywords if article.meta_keywords else article.meta_data.get('keywords', []))),
           'published_date': article.publish_date if article.publish_date
           else article.meta_data.get('pubdate', ''), 'top_img': article.top_image,
           'content': re.sub('\\n+', '</p><p>', '<p>' + article.text + '</p>')}
    return result['title']


if __name__ == '__main__':
    res = crawl(
        'https://www.news.com.au/sport/sports-life/history/england-rugby-could-ban-swing-low-sweet-chariot-because-of-slavery-links/news-story/76302d2ad2b6271085ea4940addb5c86')
    print(res)