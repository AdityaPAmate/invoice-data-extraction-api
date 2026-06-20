FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libgl1 \
    libsm6 \
    libxrender1 \
    libxext6 \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8080

ENV FLAGS_use_mkldnn=False
ENV ONEDNN_VERBOSE=0
ENV OMP_NUM_THREADS=1
ENV MKL_NUM_THREADS=1

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--timeout", "300", "file_extractor.wsgi:application"]