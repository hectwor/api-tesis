from mongoengine import connect
MONGO_DATABASE_NAME = 'api-ts'
MONGO_HOST = 'localhost'
MONGO_PORT = 27017

connect(MONGO_DATABASE_NAME, host=MONGO_HOST, port=MONGO_PORT)