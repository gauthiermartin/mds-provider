"""
Generating random data of miscellaneous types.
"""

from datetime import datetime, timedelta
import json
import random
import string
import uuid


def random_date_from(date,
                     min_td=timedelta(seconds=0),
                     max_td=timedelta(seconds=0)):
    """
    Produces a datetime at a random offset from :date:.
    """
    min_s = min(min_td.total_seconds(), max_td.total_seconds())
    max_s = max(min_td.total_seconds(), max_td.total_seconds())
    offset = random.uniform(min_s, max_s)
    return date + timedelta(seconds=offset)


def random_string(k, chars=None):
    """
    Create a random string of length :k: from the set of uppercase letters
    and numbers.

    Optionally use the set of characters :chars:.
    """
    if chars is None:
        chars = string.ascii_uppercase + string.digits
    return "".join(random.choices(chars, k=k))


def random_uuid():
    """
    Create a uuid and formated it as a string by removing the -
    """
    uuid_value = uuid.uuid4()

    formated_uuid = str(uuid_value).replace('-', '')

    return formated_uuid


def random_file_url(company):
    return "https://{}.co/{}.jpg".format(
        "-".join(company.split()), random_string(7)
    ).lower()
