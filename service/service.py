from flask import Flask
from flask_restful import abort, Api, fields, marshal_with, reqparse, Resource
from datetime import datetime
from models import NotificationModel
from http_status import HttpStatus
from pytz import utc


class NotificationManager():
    last_id = 0

    def __init__(self):
        self.notifications = {}

    def insert_notification(self, notification):
        self.last_id += 1
        notification.id = self.last_id
        self.notifications[self.last_id] = notification

    def get_notification(self, id):
        return self.notifications[id]

    def delete_notification(self, id):
        del self.notifications[id]
