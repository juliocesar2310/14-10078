FROM python

RUN pip install requests
RUN pip install simplejson

ADD asignacion8.py /

CMD ["python", "./asignacion8.py"]
