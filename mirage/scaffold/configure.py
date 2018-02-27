# -*- coding: utf-8 -*-
"""
Copyright 2017-2018 Shota Shimazu.

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
import warnings
from mirage.project import load_djfile, load_additional_conf, load_secret_conf

def get_all_conf():
    warnings.warn("get_all_conf will be deprecated on next release.", PendingDeprecationWarning)
    return load_djfile()

def get_app_name():
    warnings.warn("get_app_name will be deprecated on next release.", PendingDeprecationWarning)
    data = load_djfile()
    return data["project"]["name"]

def get_app_ver():
    warnings.warn("get_app_ver will be deprecated on next release.", PendingDeprecationWarning)
    data = load_djfile()
    return data["project"]["version"]


def get_proj_config(conf_name):
    warnings.warn("get_proj_config will be deprecated on next release.", PendingDeprecationWarning)

    data = None

    try:
        data = load_djfile()
        if os.path.exists("Miragefile.addon"):
            additional = load_additional_conf()
        elif os.path.exists("Miragefile.secret"):
            secret = load_secret_conf()
    except:
        return "Invalid Miragefile"

    if conf_name == "all":
        return data
    elif conf_name == "name":
        return data["project"]["name"]
    elif conf_name == "version":
        return data["project"]["version"]
    elif conf_name == "author":
        return data["project"]["author"]
    elif conf_name == "git":
        return data["project"]["git"]
    elif conf_name == "license":
        return data["project"]["license"]
    elif conf_name == "description":
        return data["project"]["description"]
    elif conf_name == "iyashi":
        try:
            return additional["additional_options"]["iyashi"]
        except:
            return False



def get_django_config(conf_name):
    warnings.warn("get_django_config will be deprecated on next release.", PendingDeprecationWarning)

    data = None

    try:
        data = load_djfile()
    except:
        return "Invalid Miragefile"

    if conf_name == "path":
        if data["django"]["path"] == ".":
            return os.getcwd()
        else:
            return data["django"]["path"]
    elif conf_name == "package":
        return data["django"]["package"]
    elif conf_name == "database":
        return data["django"]["database"]


def save_djfile(json_struct):
    warnings.warn("save_djfile will be deprecated on next release.", PendingDeprecationWarning)
    pass
