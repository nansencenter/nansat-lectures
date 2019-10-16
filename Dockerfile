from akorosov/nansat
RUN conda install notebook --yes
CMD ["jupyter", "notebook", "--allow-root", "--no-browser", "--ip=0.0.0.0"]
