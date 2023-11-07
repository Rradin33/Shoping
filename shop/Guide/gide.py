### 1 => ( install Venv )

# py -m venv venv        ->      code nasb venv
# venv\Scripts\activate.ps1 , venv\Scripts\activate.bat      ->    code fa'al sazi venv

#----------------------------------------------------------------

### 2 => ( install django )

# pip install django       ->            code nasb django

#----------------------------------------------------------------

### 3 => ( install Mysql )

# pip install mysql-connector-python         -> code nasb mysql-connector-python

#----------------------------------------------------------------

### 4 =>( sakhtan shop )

# django-admin.exe startproject shop 

#----------------------------------------------------------------

### 5 => ( bad az sakhtan shop site sakhte shode ra test mikonim k moshkeli nadashte bashad )

# cd shop
# py manage.py runserver 

#----------------------------------------------------------------

### 6 => ( bad posheha ra b vasile dokme (new folder) misazim )

# static, media, apps, templates

#----------------------------------------------------------------

### 7 => ( badesh miravim tanzimat setting ra anjam midahim )

#----------------------------------------------------------------

### 8 => ( sakhtan applicationha dakhele apps )

# cd shop
# cd apps
# django-admin.exe startapp main          ->       app main sakhte mishavad

###( bad vared app main mishavim va dakhele fole apps.py minevisim ( name = 'apps.main' ) 
### va bad dakhele setting zire INSTALLED_APPS minevisim ( 'apps.main.apps.MainConfig' ) )

### ( va bad sakhtan url app main )

# urls.py

### ( va bad tanzim url app main dar file URL madar(asli) )

# path('', include('apps.main.urls', namespace='main'))      ->      url madar app main

###( in tanzimat bala ra baraye tamame app ha injam midahim )

#----------------------------------------------------------------

### 9 => ( migrations )

# py manage.py makemigrations         ->          baraye sakhte shodam class model dar Database

# py manage.py migrate                ->          baraye sakhte shodan shakhehahe modelemon dar Database

#----------------------------------------------------------------

### 10 => ( superuser )

# cd shop
# py manage.py createsuperuser        ->          baraye sakhte shodan page admin dar site ast

#---------------------------------------------------------------

### 11 -> ( pillow )

# python -m pip install Pillow       ->           harmoghe dar modelhamon az image estefade mikonim baraye inke esm axsha dar Database save shavand ghabl az inke migrate konim bayad in cod ra bezanim

#---------------------------------------------------------------

### 12 -> ( check ) 

# py manage.py check                 ->           harmoghe codehamon ro minevisim dar akhar vaghti mikhahim bebinim khatai darim ya na in code ra dar Terminal minevisim

#---------------------------------------------------------------

### 13 -> ( ckeditor )

# pip install django-ckeditor        ->           ckeditor ra nasb mikonim baraye zamani k mikhahim b ghesmate tozihat(description) site model bedahim yani masalan vasatesh axs bezarim ya emkanat Word ra behesh bedahim ta b neveshtehash shekl bedahim masalan yek kalame ro bozorg konim ya rang konim ya ziresh khat bekeshim va ... 

# bad az inke nasb kardim miravim dakhele Setting zir INSTALLED_APP minevisim  "ckeditor",
#                                                                              " ckeditor_uploader",

# bad miravim pain Settings.py in code ra minevisim ta system b ckeditor vasl shavad

# CKEDITOR_UPLOAD_PATH = "images/ckeditor/upload_files"
# CKEDITOR_STORAGE_BACKEND = "django.core.files.storage.FileSystemStorage"
# CKEDITOR_CONFIGS = {
#     'default': {
#         'skin': 'moono',
#         # 'skin': 'office2013',
#         'toolbar_Basic': [
#             ['Source', '-', 'Bold', 'Italic']
#         ],
#         'toolbar_YourCustomToolbarConfig': [
#             {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
#             {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
#             {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
#             {'name': 'forms',
#              'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
#                        'HiddenField']},
#             '/',
#             {'name': 'basicstyles',
#              'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
#             {'name': 'paragraph',
#              'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
#                        'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
#                        'Language']},
#             {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
#             {'name': 'insert',
#              'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
#             '/',
#             {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
#             {'name': 'colors', 'items': ['TextColor', 'BGColor']},
#             {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
#             {'name': 'about', 'items': ['About']},
#             '/',  # put this to force next toolbar on new line
#             {'name': 'yourcustomtools', 'items': [
#                 # put the name of your editor.ui.addButton here
#                 'Preview',
#                 'Maximize',

#             ]},
#         ],
#         'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
#         'tabSpaces': 4,
#         'extraPlugins': ','.join([
#             'uploadimage', # the upload image feature
#             # your extra plugins here
#             'div',
#             'autolink',
#             'autoembed',
#             'embedsemantic',
#             'autogrow',
#             # 'devtools',
#             'widget',
#             'lineutils',
#             'clipboard',
#             'dialog',
#             'dialogui',
#             'elementspath'
#         ]),
#     }
# }

# bad miravim dakhele folder ( shop ) dakhele ( urls.py ) in URL ra minevisim ( path('ckeditor', include('ckeditor_uploader.urls')), )
# va bad agar didim dar panel admin in code ejra nashod va ghesmate tozihat hich taghiri nakard bayad dar ghesmat terminal benvisim ( py manage.py makemigrations ) va ( py manage.py migrate )
# va dar akhar dakhele har description khastim model bedim bayad beravim dakhele safhe html oun description in code ra benvisim  ->  {% autoescape off %}
#																																												 	{{product.description}} 
#																																												 {% endautoescape %} 

#----------------------------------------------------------------

### 14 -> ( render_partial )

#  ( pip instal django_render_partial )          ->          baraye in ast ma yek view benvisim va in view bere etela'at site ro az Database begire biyare va bedimesh b yek safhe HTML ta in etela'at ro roye safhe site neshan bede, dar kol ( render_partial ) yek view ra run mikonad va oun view yek template ro run mikone, in codha ra dar folder ( products ) dar views.py minevisim
# vaghti in ra nasb kardim bad miravim dakhele folder Settings.py in code ra zire INSTALLED_APP minevisim ( django_render_partial )                                            
# vaghti vared site mishavim va b site negah mikonim ghesmathaye mokhtalefi vojod darad mesl ( arzantarin mahsolat, mahsolat vizhe, akharin mahsolat ) k har ko2m az in ghesmatha jodagane tavasote yek ( partial ) codhashon ro minevisim                                                   
# safhe asli site tavasote app ( main ) run mishe va sakhte mishe ama masalan yek ghesmat az safhe asli site arzantarin mahsolat ra neshan midahad, yek ghesmate digar akharin mahsolat ra neshan midahad, ghesmate pain safhe asli site makhsos maghalat hast va ma bayad har ko2m az in bakhsh ha ro dakhele app khodesh piyade sazi konim va tavasote app main oun ro seda mizanim va ta roye site zaher beshe

#----------------------------------------------------------------

### 15 -> ( django.contrib.humanize )

# ( django.contrib.humanize ) in app baraye cama vasate ghaimate kalaha ast, yani dar site vasate gheimatha cama migozarad baraye mesal 28,000,000
# baraye nasb bayad beravim dakhele setting zire INSTALLED_APPS code bala ra benvisim
# bad dar har ghesmat az code k mikhahim gheimat ra benvisim ( dakhele safhe HTML ) balaye safhe minevisim {% load humanize %} va bad in code ra minevisim k vasate ghaimatha cama begozarad ( {{ product.price|intcomma }} ), va in code kamelesh ast k man dar file product_box.html neveshtam ( <div class="product-card__prices">{{ product.price|intcomma }}تومان</div> )





                                                      