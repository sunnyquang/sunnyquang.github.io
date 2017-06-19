# imports - standard imports
import os

# imports - third-party imports
import addict

# imports - module imports
from build.util import pardir, relurljoin

CONFIG                                      = addict.Dict()

CONFIG.environment                          = os.getenv('WEBDEV_ENV', 'development')
CONFIG.exclude                              = [
    'Gemfile',
    'Gemfile.lock',
    'package.json',
    'requirements',
    'requirements.txt',
    'build',
    'Makefile',
    'LICENSE',
    'README.md',
    'TODO.md'
]
CONFIG.sass.style                           = 'compressed'

# paths
CONFIG.path.root                            = pardir(__file__, 2)
CONFIG.path.assets                          = os.path.join(CONFIG.path.root, 'assets')
CONFIG.path.images                          = os.path.join(CONFIG.path.assets,  'img')

# brand
CONFIG.brand.name                           = 'Sunny Quang'
CONFIG.brand.description                    = ''
CONFIG.brand.email                          = 'achillesrasquinha@gmail.com'
CONFIG.brand.phone                          = '+17132568541'
CONFIG.brand.social.skype                   = 'sunnyquang'
CONFIG.brand.social.facebook                = 'https://www.facebook.com/sunny.quang.1'
CONFIG.brand.social.instagram               = 'https://instagram.com/sunny_dalight'
CONFIG.brand.social.twitter                 = ''

CONFIG.brand.mailchimp.dc                   = 'us16'
CONFIG.brand.mailchimp.APIVersion           = '3.0'
CONFIG.brand.mailchimp.APIKey               = '4ef6b1c6f1b1115a59cb247029d9e574-us16'
CONFIG.brand.mailchimp.listID               = '2685434741'

# URLs
CONFIG.url                                  = 'sunnymobilityfitness.com'
CONFIG.baseurl                              = '/'
CONFIG.urls.assets                          = relurljoin(CONFIG.baseurl,    'assets')
CONFIG.urls.data                            = relurljoin(CONFIG.urls.assets,  'data')
CONFIG.urls.images                          = relurljoin(CONFIG.urls.assets,   'img')
CONFIG.urls.icons                           = relurljoin(CONFIG.urls.images, 'icons')
CONFIG.plugins                              = [
    'jekyll-seo-tag'
]

CONFIG.lang                                 = 'en'

# colors
CONFIG.color.primary                        = '#222222'

# navbar
CONFIG.data.navbar.links                    = [
    { "title": "Home",       "url": CONFIG.baseurl },
    { "title": "About Me",   "url": relurljoin(CONFIG.baseurl, 'about') },
    { "title": "Blog",       "url": 'http://blog.{url}'.format(url = CONFIG.url) },
    { "title": "Boxing",     "url": relurljoin(CONFIG.baseurl, 'boxing') },
    { "title": "Training",   "url": relurljoin(CONFIG.baseurl, 'training') },
    { "title": "Contact",    "url": relurljoin(CONFIG.baseurl, 'contact.html') }
]

CONFIG.data.about.paragraphs                = [
    'Sunny is an experienced personal trainer and boxing instructor. His approach focuses on teaching functional exercises for anyone interested in improving mobility, sports performance, and weight loss.',
    'Sunny began his personal training as an MMA fighter at the age of 19. He has several MMA fights under his belt and is currently being promoted by Legacy Fighting. In addition to being an accomplished MMA fighter, he has training across a wide spectrum of modalities including weightlifting, kettlebells, and boxing. His passion for training others is motivated by the conviction that we must counteract the inertia that accompanies our modern lifestyle by adopting a holistic mind body approach by utilizing functional exercises to develop mobility, power, and strength.',
    'Sunny holds a degree from the National Personal Training Institute. His personal training certifications include NASM certified, Kettlebell certified, Trigger point certified, and as a Box n Burn boxing instructor. Sunny teaches boxing classes on the weekends. All levels are welcomed.'
]

CONFIG.author.email                         = 'syiree.official@gmail.com'

# Jekyll SEO
CONFIG.description                          = CONFIG.brand.description
CONFIG.url                                  = 'https://sunnyquang.com'
CONFIG.twitter.username                     = CONFIG.brand.social.twitter

CONFIG.data.images.certifications           = [
    { "src": relurljoin(CONFIG.urls.images, 'certifications', filename) }
    for filename in os.listdir(os.path.join(CONFIG.path.images, 'certifications'))
]

CONFIG.data.images.carousel                 = [
    { "src": relurljoin(CONFIG.urls.images, 'carousel', filename) }
    for filename in os.listdir(os.path.join(CONFIG.path.images, 'carousel'))
]

CONFIG.data.training.levels.beginner        = {
    'tagline': 'Unlock your Potential',
       'link': relurljoin(CONFIG.baseurl, 'training', 'beginner.html'),
   'packages': [
        {
                'name': 'Level 1',
               'image': { 'src': relurljoin(CONFIG.urls.images, 'training',
                    'thumbnails', '1.jpg') },
            'duration': 30,    # minutes
            'sessions': 4,     # monthly
           'equipment': ['gym'],
               'price': 180,   # USD
        },
        {
                'name': 'Level 2',
               'image': { 'src': relurljoin(CONFIG.urls.images, 'training',
                    'thumbnails', '2.jpg') },
            'duration': 30,
            'sessions': 8,
           'equipment': ['gym'],
               'price': 360,
        },
        {
                'name': 'Level 3',
               'image': { 'src': relurljoin(CONFIG.urls.images, 'training',
                    'thumbnails', '3.jpg') },
            'duration': 30,
            'sessions': 12,
           'equipment': ['gym'],
               'price': 540,
        }
   ]
}

CONFIG.data.training.levels.intermediate       = {
    'tagline': 'Experience the Power of Transformation',
       'link': relurljoin(CONFIG.baseurl, 'training', 'intermediate.html'),
    'packages': [
        {
                'name': 'Level 1',
               'image': { 'src': relurljoin(CONFIG.urls.images, 'training',
                    'thumbnails', '1.jpg') },
            'duration': 45,    # minutes
            'sessions': 4,     # monthly
           'equipment': ['gym'],
               'price': 240,   # USD
        },
        {
                'name': 'Level 2',
               'image': { 'src': relurljoin(CONFIG.urls.images, 'training',
                    'thumbnails', '2.jpg') },
            'duration': 45,
            'sessions': 8,
           'equipment': ['gym'],
               'price': 480,
            },
            {
                    'name': 'Level 3',
                   'image': { 'src': relurljoin(CONFIG.urls.images, 'training',
                        'thumbnails', '3.jpg') },
                'duration': 45,
                'sessions': 12,
                   'price': 720,
            }
       ]
}

CONFIG.data.training.levels.advance            = {
    'tagline': 'Fitness beyond Limits',
       'link': relurljoin(CONFIG.baseurl, 'training', 'advance.html'),
   'packages': [
        {
                'name': 'Level 1',
               'image': { 'src': relurljoin(CONFIG.urls.images, 'training',
                    'thumbnails', '1.jpg') },
            'duration': 60,    # minutes
            'sessions': 4,     # monthly
           'equipment': ['gym'],
               'price': 300,   # USD
        },
        {
                'name': 'Level 2',
               'image': { 'src': relurljoin(CONFIG.urls.images, 'training',
                    'thumbnails', '2.jpg') },
            'duration': 60,
            'sessions': 8,
           'equipment': ['gym'],
               'price': 600,
        },
        {
                'name': 'Level 3',
               'image': { 'src': relurljoin(CONFIG.urls.images, 'training',
                    'thumbnails', '3.jpg') },
            'duration': 60,
            'sessions': 12,
           'equipment': ['gym'],
               'price': 900,
        }
   ]
}
