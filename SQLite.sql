INSERT INTO DJANGO (engine, transmission, fuel) VALUES (W12, mechanical, petrol)


DJANGO.objects.create(engine='V8', transmission='mechanical', fuel='diesel')
DJANGO.objects.create(engine='inline', transmission='automatic', fuel='gas')
DJANGO.objects.create(engine='V6', transmission='automatic', fuel='petrol')

DJANGO.objects.filter(fuel='gas').update(fuel='petrol')

DJANGO.objects.all()

DJANGO.objects.filter(engine='V6').delete

