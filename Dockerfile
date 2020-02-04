from nansencenter/geospaas
RUN conda install cartopy notebook
CMD ["jupyter", "notebook", "--allow-root", "--no-browser", "--ip=0.0.0.0"]
