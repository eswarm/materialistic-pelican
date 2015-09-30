# materialistic-pelican

A material theme based on Material Design Lite(from Google) for [Pelican](http://www,getpelican.com) based sites. 

![](https://github.com/eswarm/materialistic-pelican/blob/master/screenshot.png)
![](https://github.com/eswarm/materialistic-pelican/blob/master/screenshots/post.png) 

You can see it live [here](http://eswarm.in)

Can be customized with a single variable change into 240 colors !!  

Some of them here 

![](https://github.com/eswarm/materialistic-pelican/blob/master/screenshots/brown.png)

![](https://github.com/eswarm/materialistic-pelican/blob/master/screenshots/index_red.png)

![](https://github.com/eswarm/materialistic-pelican/blob/master/screenshots/light_green_red.png)

![](https://github.com/eswarm/materialistic-pelican/blob/master/screenshots/lightblue.png)

![](https://github.com/eswarm/materialistic-pelican/blob/master/screenshots/teal.png)


To use the theme, download this repository and add this variable to your settings file with the appropriate directory

`THEME = "/some/path/materialistic-pelican"`

or 

while generating content add `-t /some/path/materialistic-pelican` to your command

Refer [this](https://github.com/getpelican/pelican-themes) and [this](http://docs.getpelican.com/en/3.6.3/settings.html#themes) for more information on using themes. 

## Theme Specific variables 

### CDN

For ease of developing you can use the CDN provided by google for enabling your themes. If the variable is set to false, the attached css and js will be used, you can change or edit them as necessary. 

`USE_CDN = True`

### Colors

Please note this will work only if you set `USE_CDN` to true. 

`PRIMARY_COLOR`

The primary color that will be used, for navbar, article headings etc. Choose one from from list below. 

Choose from 

                        'Cyan', 'Teal', 'Green', 'Light Green', 'Lime',
                        'Yellow', 'Amber', 'Orange',
                        'Brown', 'Blue Grey','Grey',
                        'Deep Orange', 'Red', 'Pink', 'Purple',
                        'Deep Purple', 'Indigo', 'Blue', 'Light Blue'
                        
`ACCENT_COLOR`

The accent color that will be used, for links, buttons etc. 

Choose from 

                        'Cyan', 'Teal', 'Green', 'Light Green', 'Lime',
                        'Yellow', 'Amber', 'Orange', 
                        'Deep Orange', 'Red', 'Pink', 'Purple',
                        'Deep Purple', 'Indigo', 'Blue', 'Light Blue'
                        
For e.g 
```
PRIMARY_COLOR = 'Indigo'
ACCENT_COLOR = 'Light Blue'
```
Was the screenshot posted above. 

### Comments 

To enable google plus comments on your articles set the following variable to true. This will be enabled on the about page too, if you have one. 

GOOGLE_PLUS_COMMENTS = True

### Logo URL 

The picture that will be used in the left drawer. 

`USER_LOGO_URL = SITEURL + '/images/logo.png'`

### AVATAR URL 

The picture that will be used in author 

`USER_AVATAR_URL = SITEURL + '/images/avatar.png'`

My pelicanconf.py for reference is below.  

```

SOCIAL = (('Github', 'https://github.com/eswarm'),
		  ('Google plus', 'https://plus.google.com/102630360601349400454/about'),
          ('Twitter', 'https://twitter.com/eswar_001'))

DEFAULT_PAGINATION = 4

PRIMARY_COLOR = 'Indigo'
ACCENT_COLOR = 'Light Blue'
GOOGLE_PLUS_COMMENTS = True
USE_CDN = True

THEME = '../materialistic pelican'
STATIC_PATHS = ['images']

# provide an absolute url here, for pages to work properly.
USER_LOGO_URL = SITEURL + '/images/logo.png'
# provide an absolute url here, for pages to work properly.
USER_AVATAR_URL = SITEURL + '/images/avatar.png'

```




