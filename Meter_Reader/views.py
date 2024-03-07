
import random
import smtplib

# from datetime import datetime, timedelta
import datetime
from datetime import timedelta
from email.mime.text import MIMEText


from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.utils import dates

from .models import *


# Create your views here.


def log(request):
    return render(request,"index.html")

def login_post(request):
    username = request.POST['textfield']
    password = request.POST['textfield2']
    data = login.objects.filter(username=username,password=password)
    if data.exists():
        data = data[0]
        request.session['lid'] = data.id
        request.session['lg'] = "lin"

        if data.type == 'admin':
            return redirect('/admin_home')
        elif data.type == 'branch':
            return redirect('/kseb_home')
        elif data.type == 'staff':
            return redirect('/staff_home')
    else:
        return HttpResponse("<script>alert('Invalid');window.location='/'</script>")

def logout(request):
    request.session['lg']=""
    return redirect('/')

def admin_home(request):
    if request.session['lg'] != 'lin':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    return render(request,"admin/admin_index.html")

def kseb_home(request):
    if request.session['lg'] != 'lin':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    return render(request,"kseb_branch/kseb_index.html")

def staff_home(request):
    if request.session['lg'] != 'lin':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    return render(request,"staff/staff_index.html")


#..........................................................

# BRANCH MANAGEMENT

def add_branch(request):
    return render(request,"admin/add_branch.html")

def add_branch_post(request):
    branch_name = request.POST['textfield']
    district = request.POST['select']
    place = request.POST['textfield2']
    post = request.POST['textfield3']
    pin = request.POST['textfield4']
    contact = request.POST['textfield5']
    email = request.POST['textfield6']

    res = random.randint(0000, 9999)

    data = login.objects.filter(username=email)
    if data.exists():
        return HttpResponse("<script>alert('Already exist');window.location='/add_branch'</script>")
    else:
        log_obj = login()
        log_obj.username = email
        log_obj.password = res
        log_obj.type = 'branch'
        log_obj.save()


        obj = branch()
        obj.branch_name = branch_name
        obj.district = district
        obj.place = place
        obj.post = post
        obj.pin = pin
        obj.contact = contact
        obj.email = email
        obj.LOGIN = log_obj
        obj.save()
        try:
            gmail = smtplib.SMTP('smtp.gmail.com', 587)
            gmail.ehlo()
            gmail.starttls()
            gmail.login('riss.princytv@gmail.com', 'vile vivc hvnh xdgs')
        except Exception as e:
            print("Couldn't setup email!!" + str(e))
        msg = MIMEText("Branch Adding Check It..")
        msg['Subject'] = 'Verification'
        msg['To'] = email
        msg['From'] = 'riss.princytv@gmail.com'
        try:
            gmail.send_message(msg)
        except Exception as e:
            print("COULDN'T SEND EMAIL", str(e))
        return HttpResponse("<script>alert('added successfully');window.location='/add_branch#ff'</script>")


def view_branch(request):
    data = branch.objects.all()
    return render(request,"admin/view_branch.html",{"data":data})

def update_branch(request,id):
    data = branch.objects.get(id=id)
    return render(request,"admin/update_branch.html",{"data":data,"id":id})

def update_branch_post(request,id):
    branch_name = request.POST['textfield']
    district = request.POST['select']
    place = request.POST['textfield2']
    post = request.POST['textfield3']
    pin = request.POST['textfield4']
    contact = request.POST['textfield5']
    email = request.POST['textfield6']
    branch.objects.filter(id=id).update(branch_name = branch_name,district = district,place=place,post = post,pin=pin,contact=contact,email=email)
    return HttpResponse("<script>alert('Updated');window.location='/view_branch#ff'</script>")

def delete_branch(request,id):
    branch.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted');window.location='/view_branch#ff'</script>")

# UNIT PRICE SETTING

def add_unit_price(request):
    return render(request,"admin/add_unit_price.html")

def add_unit_price_post(request):
    connection_type = request.POST['select']
    unit_from = request.POST['textfield']
    unit_to = request.POST['textfield2']
    amount = request.POST['textfield3']
    last_updated = request.POST['textfield4']

    obj = unit_price()
    obj.connection_type = connection_type
    obj.unit_from = unit_from
    obj.unit_to = unit_to
    obj.amount =amount
    obj.last_updated = last_updated
    obj.save()
    return HttpResponse("<script>alert('Added Successfully');window.location='/add_unit_price#ff'</script>")

def view_unit_price(request):
    data = unit_price.objects.all()
    return render(request,"admin/view_unit_price.html",{"data":data})

def update_unit_price(request,id):
    data = unit_price.objects.get(id=id)
    return render(request,"admin/update_unit_price.html",{"data":data,"id":id})

def update_unit_price_post(request,id):
    connection_type = request.POST['select']
    unit_from = request.POST['textfield']
    unit_to = request.POST['textfield2']
    amount = request.POST['textfield3']
    last_updated = request.POST['textfield4']
    unit_price.objects.filter(id=id).update(connection_type=connection_type,unit_from = unit_from,unit_to =unit_to,
                                            amount=amount,last_updated=last_updated)
    return HttpResponse("<script>alert('Updated');window.location='/view_unit_price#ff'</script>")

def delete_unit_price(request,id):
    unit_price.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted');window.location='/view_unit_price#ff'</script>")


# NOTIFICATION MANAGEMENT

def add_notification(request):
    data = branch.objects.all()
    return render(request,"admin/add_notification.html",{"data":data})

def add_notification_post(request):
    branch_name = request.POST['select']
    notifications = request.POST['textfield']
    date = request.POST['textfield2']
    obj = notification()
    obj.branch_name = branch_name
    obj.notification = notifications
    obj.date = date
    obj.save()
    return HttpResponse("<script>alert('notification added');window.location='/add_notification#ff'</script>")

def view_notification(request):
    data = notification.objects.all()
    return render(request,"admin/view_notification.html",{"data":data})

def delete_notification(request,id):
    notification.objects.get(id=id).delete()
    return HttpResponse("<script>alert('notification Removed');window.location='/view_notification#ff'</script>")



# def view_rating(request):
#     data = rating.objects.all()
#     return render(request,"admin/view_rating.html",{"data":data})

def view_rating(request):
    data=rating.objects.all()
    print(data)
    lis=[]
    for i in data:
        rt=[]
        nrt=[]

        for j in range(int(i.rating)):
            rt.append(j)
        for j in range(5-int(i.rating)):
            nrt.append(j)

        dict={'name':i.CONSUMER.name,'date':i.date,'rate':rt,'norate':nrt}
        lis.append(dict)

    return render(request,"admin/view_rating.html",{"data":lis})

# VIEW CONSUMER

def add_consumer(request):
    data1 = branch.objects.all()
    return render(request,"admin/view_consumer.html",{"data1":data1})

def view_area(request,id):
   data = area.objects.filter(BRANCH=id)
   return render(request,"admin/view_area.html",{"data":data})

def view_consumer(request):
    area = request.POST['select']
    data2 = consumer.objects.filter(AREA=area)
    return render(request,"admin/view_consumer.html",{"data2":data2})

# VIEW STAFF........

def add_staff(request):
    data1 = branch.objects.all()
    return render(request,"admin/add_staff.html",{"data1":data1})

def staff_view_area(request,id):

    data = area.objects.filter(BRANCH=id)
    return render(request,"admin/staff_view_area.html",{"data":data})

def view_staff(request):
    area = request.POST['select']
    data2 = work_allocation.objects.filter(AREA=area)
    return render(request, "admin/add_staff.html", {"data2": data2})


# ...........................................................................................

# KSEB BRANCH


def add_area(request):
    return render(request,"kseb_branch/add_area.html")

def add_area_post(request):
    data = area.objects.all()
    if data.exists():
        return HttpResponse("<script>alert('Already exists,Try to add another!');window.location='/add_area#ff'</script>")
    else:

        area_name = request.POST['textfield']
        obj = area()
        obj.area_name = area_name
        obj.BRANCH = branch.objects.get(LOGIN=request.session['lid'])
        obj.save()
        return HttpResponse("<script>alert('Area added');window.location='/add_area#ff'</script>")

def view_areas(request):
    data = area.objects.filter(BRANCH__LOGIN=request.session['lid'])
    return render(request,"kseb_branch/view_area.html",{"data":data})

def delete_area(request,id):
    area.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Area deleted');window.location='/view_areas#ff'</script>")

# STAFF MANAGEMENT

def add_staffs(request):
    return render(request,"kseb_branch/add_staff.html")

def add_staff_post(request):
    name = request.POST['textfield']
    photo = request.FILES['fileField']
    fs = FileSystemStorage()
    dt = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    fs.save(r"C:\Users\DELL\PycharmProjects\KSEB_Meter_Reader\Meter_Reader\static\photo\\" + dt + '.jpg', photo)
    photo = '/static/photo/' + dt + '.jpg'

    gender = request.POST['RadioGroup1']
    age = request.POST['textfield2']
    place = request.POST['textfield3']
    post = request.POST['textfield4']
    pin = request.POST['textfield5']
    email = request.POST['textfield6']
    contact = request.POST['textfield7']
    salary = request.POST['textfield8']

    res = random.randint(0000, 9999)

    data = login.objects.filter(username=email)
    if data.exists():
        return HttpResponse("<script>alert('Already exist');window.location='/add_staffs'</script>")
    else:
        log_obj = login()
        log_obj.username = email
        log_obj.password = res
        log_obj.type = 'staff'
        log_obj.save()

        obj = staff()
        obj.name = name
        obj.photo = photo
        obj.gender = gender
        obj.age = age
        obj.place = place
        obj.post = post
        obj.pin = pin
        obj.email = email
        obj.contact = contact
        obj.salary = salary
        obj.BRANCH = branch.objects.get(LOGIN=request.session['lid'])
        obj.LOGIN = log_obj
        obj.save()
        try:
            gmail = smtplib.SMTP('smtp.gmail.com', 587)
            gmail.ehlo()
            gmail.starttls()
            gmail.login('riss.princytv@gmail.com', 'vile vivc hvnh xdgs')
        except Exception as e:
            print("Couldn't setup email!!" + str(e))
        msg = MIMEText("Staff Adding Check It..")
        msg['Subject'] = 'Verification'
        msg['To'] = email
        msg['From'] = 'riss.princytv@gmail.com'
        try:
            gmail.send_message(msg)
        except Exception as e:
            print("COULDN'T SEND EMAIL", str(e))
        # print(obj)
        return HttpResponse("<script>alert('staff added');window.location='/add_staffs#ff'</script>")

def view_staffs(request):
    data = staff.objects.filter(BRANCH__LOGIN=request.session['lid'])
    return render(request,"kseb_branch/view_staff.html",{"data":data})

def update_staff(request,id):
    data = staff.objects.get(id=id)
    return render(request,"kseb_branch/update_staff.html",{"data":data,"id":id})

def update_staff_post(request,id):
    try:
        name = request.POST['textfield']
        photo = request.FILES['fileField']
        fs = FileSystemStorage()
        dt = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        fs.save(r"C:\Users\DELL\PycharmProjects\KSEB_Meter_Reader\Meter_Reader\static\photo\\" + dt + '.jpg', photo)
        photo = '/static/photo/' + dt + '.jpg'

        gender = request.POST['RadioGroup1']
        age = request.POST['textfield2']
        place = request.POST['textfield3']
        post = request.POST['textfield4']
        pin = request.POST['textfield5']
        email = request.POST['textfield6']
        contact = request.POST['textfield7']
        salary = request.POST['textfield8']
        staff.objects.filter(id=id).update(name =name,photo=photo,gender = gender,
                                           age =age,place=place,post=post,pin=pin,email =email,contact=contact,salary =salary)
        return HttpResponse("<script>alert('Staff updated');window.location='/view_staffs#ff'</script>")

    except Exception as e:
        name = request.POST['textfield']
        gender = request.POST['RadioGroup1']
        age = request.POST['textfield2']
        place = request.POST['textfield3']
        post = request.POST['textfield4']
        pin = request.POST['textfield5']
        email = request.POST['textfield6']
        contact = request.POST['textfield7']
        salary = request.POST['textfield8']
        staff.objects.filter(id=id).update(name=name,gender=gender,
                                           age=age, place=place, post=post, pin=pin, email=email, contact=contact,
                                           salary=salary)
        return HttpResponse("<script>alert('Staff Updated');window.location='/view_staffs#ff'</script>")


def delete_staff(request,id):
    staff.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Staff removed');window.location='/view_staffs'</script>")


# CONSUMER MANAGEMENT

def add_consumers(request):
    data = area.objects.all()
    return render(request,"kseb_branch/add_consumer.html",{"data":data})

def add_consumers_post(request):
    area = request.POST['select']
    consumer_no = request.POST['textfield']
    connection_type = request.POST['select1']
    name = request.POST['textfield3']
    gender = request.POST['RadioGroup1']
    place = request.POST['textfield4']
    post = request.POST['textfield5']
    pin = request.POST['textfield6']
    email = request.POST['textfield7']
    contact = request.POST['textfield8']
    password = random.randint(0000,9999)

    data = login.objects.filter(username=email)
    if data.exists():
        return HttpResponse("<script>alert('Already Exists');window.location=''</script>")
    else:
        obj = login()
        obj.username = email
        obj.password = password
        obj.type = 'consumer'
        obj.save()

        obj1 = consumer()
        obj1.AREA_id = area
        obj1.consumer_no = consumer_no
        obj1.connection_type = connection_type
        obj1.name = name
        obj1.gender = gender
        obj1.place = place
        obj1.post = post
        obj1.pin = pin
        obj1.email = email
        obj1.contact =contact
        obj1.LOGIN = obj
        obj1.save()
        try:
            gmail = smtplib.SMTP('smtp.gmail.com', 587)
            gmail.ehlo()
            gmail.starttls()
            gmail.login('riss.princytv@gmail.com', 'vile vivc hvnh xdgs')
        except Exception as e:
            print("Couldn't setup email!!" + str(e))
        msg = MIMEText("Cosumer Adding Check It..")
        msg['Subject'] = 'Verification'
        msg['To'] = email
        msg['From'] = 'riss.princytv@gmail.com'
        try:
            gmail.send_message(msg)
        except Exception as e:
            print("COULDN'T SEND EMAIL", str(e))
        return HttpResponse("<script>alert('Consumer Added');window.location='/add_consumers'</script>")

def view_consumers(request):
    data = consumer.objects.filter(AREA__BRANCH__LOGIN=request.session['lid'])
    # data = consumer.objects.all()
    return render(request,"kseb_branch/view_consumer.html",{"data":data})


def update_consumer(request,id):
    data = area.objects.filter(BRANCH__LOGIN=request.session['lid'])
    data1 = consumer.objects.get(id=id)


    return render(request,"kseb_branch/update_consumer.html",{"data":data,"data1":data1,"id":id})

def update_consumer_post(request,id):
    area = request.POST['select']
    consumer_no = request.POST['textfield']
    connection_type = request.POST['select1']
    name = request.POST['textfield3']
    gender = request.POST['RadioGroup1']
    place = request.POST['textfield4']
    post = request.POST['textfield5']
    pin = request.POST['textfield6']
    email = request.POST['textfield7']
    contact = request.POST['textfield8']
    consumer.objects.filter(id=id).update(area = area,consumer_no = consumer_no,connection_type=connection_type,name =name,
                                          gender=gender,place=place,post=post,pin=pin,email=email,contact=contact)
    return HttpResponse("<script>alert('Consumer updated');window.location='/view_consumers#ff'</script>")

def delete_consumer(request,id):
    consumer.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Consumer deleted');window.location='/view_consumers#ff</script>")


#....ALLOCATE WORK TO STAFF

def allocate_work_tostaff(request,id):
    b=branch.objects.get(LOGIN=request.session['lid'])
    data = area.objects.filter(BRANCH = b)
    # data = area.objects.all()
    return render(request,"kseb_branch/allocate_work_tostaff.html",{"data":data,"id":id})

def allocate_area(request,id):
    area = request.POST['select']
    obj = work_allocation()
    obj.AREA_id = area
    obj.STAFF_id = id
    obj.save()
    return HttpResponse("<script>alert('work allocated for staff');window.location='/view_staffs'</script>")

def view_complaints(request):
    b = branch.objects.get(LOGIN=request.session['lid'])

    data = complaints.objects.filter(CONSUMER__AREA__BRANCH = b)

    return render(request,"kseb_branch/view_complaint.html",{"data":data})

def send_reply(request,id):
    return render(request,"kseb_branch/send_reply.html",{"id":id})

def send_reply_post(request,id):

    my_date = date.today()
    my_datetime = datetime(my_date.year, my_date.month, my_date.day)
    reply_date = my_date
    reply = request.POST['textarea']
    complaints.objects.filter(id=id).update(reply=reply, reply_date=reply_date)
    return HttpResponse("<script>alert('Reply sended');window.location='/view_complaints'</script>")

def view_bill(request):
    res = bill.objects.all()

    return render(request,"kseb_branch/view_bill.html",{'data':res})

def view_bill_post(request):
    consumer1 = request.POST['textfield']
    # bill.objects.filter(CONSUMER__name__icontains=consumer1)
    res=bill.objects.filter(CONSUMER__name=consumer1)
    return render(request, "kseb_branch/view_bill.html", {'data': res})

#............................................................................................... ---> STAFF MODULE

def view_profile(request):
    data = staff.objects.get(LOGIN=request.session['lid'])
    return render(request,"staff/view_profile.html",{"data":data})

def view_allocated_work(request):
    st = staff.objects.get(id=request.session['lid'])
    data = work_allocation.objects.filter(STAFF=st)
    return render(request,"staff/view_allocated_work.html",{"data":data})

def staff_view_consumer(request):
    data = area.objects.all()
    return render(request,"staff/view_consumers.html",{"data":data})

def view_consumer_post(request):
    area = request.POST['select']
    data1 = consumer.objects.filter(AREA=area)
    # print(data1)
    # data = area.objects.all()
    return render(request, "staff/view_consumers.html", {"data1": data1})

def view_previous_reading(request,id):
    data = bill.objects.filter(CONSUMER=id)
    return render(request,"staff/view_previous_reading.html",{"data":data})

def current_readings(request,id):
    return render(request, "staff/current_reading.html",{"id":id})

def current_reading_post(request, id):
    c_reading = request.POST['textfield']
    data = bill.objects.filter(CONSUMER=id,status='paid').order_by('-id')
    # print(data)
    if data.exists():
        prev_reading = data[0].current_reading
        if int(prev_reading)>0:
            unit_consumed =int(c_reading)-int(prev_reading)
            # print("uuuuuuuuuuuu",unit_consumed)
            qry=unit_price.objects.all()
            for i in qry:
                if int(unit_consumed) >= int(i.unit_from):
                    if  int(unit_consumed) <= int(i.unit_to):
                        amount = i.amount
                        # print(amount)

                        obj = bill()

                        obj.date = datetime.datetime.today().strftime("%Y%m%d")

                        obj.amount = amount
                        obj.current_reading = c_reading
                        obj.unit_consumed = unit_consumed
                        obj.status = 'pending'
                        obj.CONSUMER = consumer.objects.get(id=id)
                        # print(datetime.today() + timedelta(days=20))
                        due = datetime.datetime.today() + timedelta(10)
                        dis = due +  timedelta(5)
                        obj.dis_date =dis
                        obj.due_date = due
                        obj.save()
                        return HttpResponse("<script>alert('Reading Added');window.location='/staff_view_consumer'</script>")
                    else:
                        pass
                pass
        else:
            unit_consumed = int(c_reading)
            qry = unit_price.objects.all()
            for i in qry:
                if int(unit_consumed) >= int(i.unit_from):
                    if int(unit_consumed) <= int(i.unit_to):
                        amount = i.amount
                        print(amount)
                        obj = bill()
                        obj.date = datetime.datetime.now().strftime("%Y%m%d")
                        obj.amount = amount
                        obj.current_reading = c_reading
                        obj.unit_consumed = unit_consumed
                        obj.status = 'pending'
                        obj.CONSUMER_id = consumer.objects.get(id=id)

                        date = datetime.datetime.now().date()
                        due = date + timedelta(10)
                        dis = due + timedelta(5)
                        obj.dis_date = dis
                        obj.due_date = due
                        obj.save()

                        return HttpResponse("<script>alert('Reading');window.location='/staff_view_consumer'</script>")
                    else:
                        pass
                pass
    else:
        unit_consumed = int(c_reading)
        qry = unit_price.objects.all()
        for i in qry:
            if int(unit_consumed) >= int(i.unit_from):
                if int(unit_consumed) <= int(i.unit_to):
                    amount = i.amount
                    print(amount)
                    obj = bill()
                    obj.date = datetime.datetime.now().strftime("%Y-%m-%d")
                    obj.amount = amount
                    obj.current_reading = c_reading
                    obj.unit_consumed = unit_consumed
                    obj.status = 'pending'
                    obj.CONSUMER_id = id
                    date = datetime.datetime.now().date()
                    due = date + timedelta(10)
                    dis = due + timedelta(5)
                    obj.dis_date = dis
                    obj.due_date = due
                    obj.save()

                    return HttpResponse("<script>alert('Reading');window.location='/staff_view_consumer'</script>")
                else:
                    pass
            pass



    return HttpResponse("<script>alert('Added');window.location='/staff_view_consumer'</script>")


# ........................................................................................................ ----> CONSUMER MODULE

def android_login(request):
    username = request.POST['username']
    password = request.POST['password']
    data = login.objects.filter(username=username,password=password)
    if data.exists():
        lid = data[0].id
        res = consumer.objects.get(LOGIN=lid)
        type = data[0].type
        name = res.name
        email = res.email
        return JsonResponse({"status":"ok","type":type,"lid":lid,'name':name,'email':email})
    else:
        return JsonResponse({"status":None})

def android_view_profile(request):
    lid = request.POST['lid']
    res=consumer.objects.get(LOGIN=lid)
    return JsonResponse({"status": "ok", "consumer_no": res.consumer_no, "connection_type": res.connection_type,
                         "area": res.AREA.area_name, "name": res.name, "gender": res.gender, "place": res.place,"post":res.post,
                         "pin":res.pin,"email":res.email,"contact":res.contact})


def android_view_previous_bill(request):
    lid = request.POST['lid']
    res = bill.objects.filter(CONSUMER=consumer.objects.get(LOGIN=lid))
    ar = []
    for i in res:
        ar.append(
            {
                "bid":i.id,
                "amount":i.amount,
                "date":i.date,
                "current_reading":i.current_reading,
                "unit_consumed":i.unit_consumed,
                "status":i.status
            }
        )
    return JsonResponse({"status":"ok","data":ar})

def android_send_complaint(request):
    lid = request.POST['lid']
    # userinstance = user.objects.get(LOGIN=lid)
    complaint = request.POST['complaint']
    complaint_date = datetime.datetime.now().strftime("%Y-%m-%d")
    obj = complaints()
    obj.complaint = complaint
    obj.complaint_date = complaint_date
    obj.reply = 'pending'
    obj.reply_date = '0000-00-00'
    obj.CONSUMER = consumer.objects.get(LOGIN=lid)
    obj.save()
    return JsonResponse({"status":"ok"})

def android_view_complaint(request):
    lid = request.POST['lid']
    # userinstance = user.objects.get(LOGIN = lid)
    res = complaints.objects.filter(CONSUMER__LOGIN=lid)
    ar = []
    for i in res:
        ar.append(
            {
                "cid":i.id,
                "complaint":i.complaint,
                "complaint_date":i.complaint_date,
                "reply":i.reply,
                "reply_date":i.reply_date
            }
        )
    return JsonResponse({"status":"ok","data":ar})

def android_send_rate(request):
    lid = request.POST['lid']
    rate = request.POST['rate']
    # date = datetime.datetime.now().strftime("%Y-%m-%d")
    obj = rating()
    obj.rating = rate
    obj.date = datetime.today().strftime("%Y-%m-%d")
    obj.CONSUMER = consumer.objects.get(LOGIN=lid)
    obj.save()
    return JsonResponse({"status": "ok"})

def android_view_notification(request):
    # lid = request.POST['lid']
    res = notification.objects.all()
    ar = []
    for i in res:
        ar.append(
            {
                "nid":i.id,
                "notification":i.notification,
                "date":i.date
            }
        )
    return JsonResponse({"status":"ok","data":ar})

def android_online_payment(request):
    lid = request.POST['lid']
    # print(lid,"lid")
    bid = request.POST['bid']
    # branch_id = request.POST['branch_id']

    bank_name =request.POST['bank_name']
    account_no = request.POST['account_no']
    ifsc_code = request.POST['ifsc_code']
    amount = request.POST['amount']

    # print("b",bank_name,"a",account_no,ifsc_code)

    data = bank.objects.filter(bank_name=bank_name, account_no=account_no, IFSC_code=ifsc_code, LOGIN=lid)
    # print("kkkk",data)
    if data.exists():
        data2 = bill.objects.filter(CONSUMER__LOGIN=lid,status='pending')
        res = bank.objects.get(LOGIN=lid)
        amount1 = res.amount
        if amount1 >= amount:
            for i in data2:

                res = bank.objects.get(LOGIN=lid)  # consumer bank
                amount1 = res.amount
                balance1 = int(amount1) - int(i.amount)
                bank.objects.filter(LOGIN=lid).update(amount=balance1)
                qry1 = consumer.objects.get(LOGIN=lid)
                aid = qry1.AREA_id
                qry2 = area.objects.get(id=aid)
                bid = qry2.BRANCH_id


                data1 = branch.objects.get(id=bid)
                branch_id = data1.LOGIN
                res2 = bank.objects.get(LOGIN=branch_id)  # kseb  bank
                amount2 = res2.amount
                balance2 = int(amount2) + int(i.amount)

                bank.objects.filter(LOGIN=branch_id).update(amount=balance2)
                # bill.objects.filter(LOGIN=branch_id).update(status = 'paid')
                bill.objects.filter(id=i.id).update(status='paid')

            return JsonResponse({"status": "ok"})
        else:
            return JsonResponse({"status": "insufficient"})

    else:
        return JsonResponse({"status": "no"})

def android_view_bill(request):
    lid = request.POST['lid']

    qry = bill.objects.filter(CONSUMER__LOGIN=lid,status='paid').order_by('-id')
    # print(qry)
    global previous_reading
    if len(qry)>0:
        previous_reading = qry[0].current_reading
    else:
        previous_reading = 0

    res = bill.objects.filter(CONSUMER__LOGIN=lid,status="pending")
    ar = []
    for i in res:
        ar.append(
            {
                "bid":i.id,
                "area":i.CONSUMER.AREA.area_name,
                "bill_date":i.date,
                "due_date":i.due_date,
                "dis_date":i.dis_date,
                "c_no":i.CONSUMER.name,
                "c_name":i.CONSUMER.consumer_no,
                "tariff":i.CONSUMER.connection_type,
                "bill_amount":i.amount,
                "unit": i.unit_consumed,
                "current_reading":i.current_reading,
                "previous_reading":previous_reading,
            }
        )
    return JsonResponse({"status":"ok","data":ar})



























