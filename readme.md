Создание платежа (объект модели Payment и платежа stripe) производится по эндпоинту:
 http://127.0.0.1:8000/courses/payments/create/

Для создания ежечасной проверки статуса по платежу, использована библиотека python-crontab (поле is_paid модели Payment).
https://pypi.org/project/python-crontab/
Библиотека работает на Linux/Ubuntu.
Проверить наличие активных cronjobs в ОС - команда 
crontab -l

После того, как оплата проведена, cronjob удаляется (с помощью отдельно кастомной команды remove_payment_tracking <cronjob_id>).

Проверить статус платежа можно с помощью команды set_payment_status <payment.pk>. 
Инфо будет выведена в консоль.