from mongoengine import connect

connect('api-ts', host='mongomock://localhost', alias='default')

