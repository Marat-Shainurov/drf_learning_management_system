from pathlib import Path
import sys

from crontab import CronTab
from django.core.management import BaseCommand

from config.settings import BASE_DIR
from courses.models import Payment
from courses.services import set_pay_status


class Command(BaseCommand):
    python_executable = Path(sys.executable)
    manage_py = BASE_DIR / 'manage.py'

    def add_arguments(self, parser):
        parser.add_argument('payment_pk', type=int, help='pk of the payment.')

    def handle(self, *args, **options):
        payment_pk = options['payment_pk']
        payment_obj = Payment.objects.get(pk=payment_pk)
        set_pay_status(payment_obj)
