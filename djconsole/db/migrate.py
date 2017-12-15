# -*- coding: utf-8 -*-
"""
Copyright 2017 Shota Shimazu.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""


import os

from djconsole.flow import Flow
from djconsole.command import log
from djconsole.command import command


class DjangoMigrateFlow(Flow):

    def __init__(self, subcommand):
        self._subcommand = subcommand

    def flow(self):
        log("Making migrations...")
        self._make_migration()
        self._apply_migration()

    def _make_migration(self):
        os.system("python manage.py makemigrations")

    def _apply_migration(self):
        os.system("python manage.py migrate")