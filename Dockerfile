FROM python:3.9
RUN mkdir /webapp
COPY requirements.txt /webapp/requirements.txt
WORKDIR /webapp
ENV PYTHONPATH .:$PYTHONPATH
RUN pip install -r requirements.txt
COPY . /webapp/
EXPOSE 8501
CMD streamlit run /webapp/main.py