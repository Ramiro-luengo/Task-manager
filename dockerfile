# FROM node:12.18.1

FROM python:3.10.2-slim-buster

WORKDIR /app

copy . .

RUN poetry install --no-dev

CMD ["py", "manage.py", "runserver"]

# RUN npm install --production

# RUN mkdir -p WORKDIR/front_end

# COPY ["front_end/package.json", "front_end/package-lock.json*", "./"]
