from os import environ, path

# Process Name
proc_name = 'gunicorn_bms'

bind = 'unix:/tmp/{0}.sock'.format(proc_name)
pythonpath = path.dirname(path.abspath(__file__))
environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
