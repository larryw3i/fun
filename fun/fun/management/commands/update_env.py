#coding: utf-8
import time
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        """
        添加你你的处理逻辑
        """
        print('hello world！！')