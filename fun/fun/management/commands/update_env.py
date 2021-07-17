#coding: utf-8
import time
from django.core.management import BaseCommand
from fun.settings import BASE_DIR
import yaml
import os


class Command(BaseCommand):

    def handle(self, *args, **options):
        env_yaml_path = os.path.join( BASE_DIR, '.env.yaml' )
        env_example_yaml_path = os.path.join( BASE_DIR, '.env.example.yaml' )
        env_yaml = yaml.safe_load( open( env_yaml_path, 'r' ) )
        env_example_yaml = yaml.safe_load( open( env_example_yaml_path, 'r' ) )
        env_example_yaml.update( env_yaml )
        yaml.safe_dump( env_example_yaml, open( env_yaml_path, 'w') )
        
