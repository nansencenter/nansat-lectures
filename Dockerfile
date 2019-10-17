from akorosov/django-geo-spaas
RUN pip install notebook
CMD ["jupyter", "notebook", "--allow-root", "--no-browser", "--ip=0.0.0.0"]
