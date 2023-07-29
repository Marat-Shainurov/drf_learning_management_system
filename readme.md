Создание платежа (объект модели Payment и платежа stripe) производится по эндпоинту:
 http://127.0.0.1:8000/courses/payments/create/
обязательный поля - payment_type ('cash' или 'transfer'), paid_course/paid_lesson (id курса или урока).

Для создания ежечасной проверки статуса по платежу, использована библиотека celery (поле is_paid модели Payment).

