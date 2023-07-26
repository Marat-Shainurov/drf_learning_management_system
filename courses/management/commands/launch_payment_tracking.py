from pathlib import Path
import sys

from crontab import CronTab
from django.core.management import BaseCommand

from config.settings import BASE_DIR
from courses.models import Payment


class Command(BaseCommand):
    python_executable = Path(sys.executable)
    manage_py = BASE_DIR / 'manage.py'

    def add_arguments(self, parser):
        parser.add_argument('payment_pk', type=int, help='pk of the payment.')

    def handle(self, *args, **options):
        payment_pk = options['payment_pk']

        cron = CronTab(user=True)
        command = f'{Command.python_executable} {Command.manage_py} set_payment_status {payment_pk}'
        job = cron.new(command=command, comment=f'{payment_pk}')
        job.setall('0 * * * *')
        cron.write()
