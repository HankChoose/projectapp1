# Use the Python 3.9 image
FROM python:3.9

# Setup work folder
WORKDIR /wiki
ADD requirements.txt /wiki/

# Change work folder
#RUN mkdir /wiki
#WORKDIR /wiki


# Install Python dependency
RUN pip install virtualenv
RUN virtualenv venv
#RUN source venv/bin/activate
RUN . venv/bin/activate
RUNpip install django-debug-toolbar==3.2.2
RUN pip install --no-cache-dir -r requirements.txt
RUN pip3 install markdown2
# Copy to wiki folder
COPY . /wiki/

# Run application
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD python manage.py runserver 0.0.0.0:8000

