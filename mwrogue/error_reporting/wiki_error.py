import datetime
import traceback

import pytz


class WikiError(object):
    error_type = None
    title = None
    error = None

    def __init__(self):
        self.timestamp = datetime.datetime.now(tz=pytz.timezone('America/Los_Angeles'))
        self.date = self.timestamp.strftime('%Y-%m-%d')

    def format_for_print(self):
        error_text = self.error
        if isinstance(self.error, Exception):
            error_text = "<br>".join(traceback.format_exception(type(self.error), self.error, self.error.__traceback__))
            error_text = error_text.replace("\n", "")
        return "<b>{}</b> - {} - {}:<br>{}".format(
            self.date,
            self.error_type,
            '[[{}]]'.format(self.title) if self.title else '(No title recorded)',
            error_text
        )
