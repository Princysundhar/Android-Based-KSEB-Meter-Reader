from django.db import models

# Create your models here.

class login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    type = models.CharField(max_length=100)

class branch(models.Model):
    branch_name = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(login,on_delete=models.CASCADE,default=1)

class notification(models.Model):
    notification = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    # status = models.CharField(max_length=50)
    BRANCH = models.ForeignKey(branch,on_delete=models.CASCADE,default=1)

class staff(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)

    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE, default=1)
    BRANCH = models.ForeignKey(branch, on_delete=models.CASCADE, default=1)

class area(models.Model):
    area_name = models.CharField(max_length=100)
    BRANCH = models.ForeignKey(branch, on_delete=models.CASCADE, default=1)


class consumer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    consumer_no = models.CharField(max_length=100)
    connection_type = models.CharField(max_length=100)
    AREA = models.ForeignKey(area,on_delete=models.CASCADE,default=1)
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE, default=1)

class rating(models.Model):
    rating = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    CONSUMER = models.ForeignKey(consumer,on_delete=models.CASCADE,default=1)

class bank(models.Model):
    bank_name = models.CharField(max_length=100)
    account_no = models.CharField(max_length=100)
    IFSC_code = models.CharField(max_length=100)
    amount = models.CharField(max_length=100,default=1)
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE, default=1)

class complaints(models.Model):
    complaint = models.CharField(max_length=100)
    complaint_date = models.CharField(max_length=100)
    reply = models.CharField(max_length=100)
    reply_date = models.CharField(max_length=100)
    CONSUMER = models.ForeignKey(consumer, on_delete=models.CASCADE, default=1)

class bill(models.Model):
    amount = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    due_date = models.CharField(max_length=100,default=1)
    dis_date = models.CharField(max_length=100,default=1)
    current_reading = models.CharField(max_length=100)
    unit_consumed = models.CharField(max_length=100)
    status = models.CharField(max_length=100,default=1)
    CONSUMER = models.ForeignKey(consumer, on_delete=models.CASCADE, default=1)

class unit_price(models.Model):
    connection_type = models.CharField(max_length=100)
    unit_from = models.CharField(max_length=100)
    unit_to = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    last_updated = models.CharField(max_length=100)

class work_allocation(models.Model):
    STAFF = models.ForeignKey(staff,on_delete=models.CASCADE,default=1)
    AREA = models.ForeignKey(area,on_delete=models.CASCADE,default=1)







