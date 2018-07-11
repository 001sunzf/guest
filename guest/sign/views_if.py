from django.http import JsonResponse
from  sign.models import Event,Guest
from django.core.exceptions import ValidationError,ObjectDoesNotExist
import time
from django.db.utils import IntegrityError
# 添加发布会接口
def add_event(request):
    eid = request.POST.get('eid','')   # 发布会ID
    name = request.POST.get('name','')   # 发布会标题
    limit = request.POST.get('limit','')  # 限制人数
    status = request.POST.get('status','')  # 状态
    address = request.POST.get('address','')  # 地址
    start_time =request.POST.get('start_time','')  # 发布会时间

    if eid == '' or name =='' or limit =='' or address =='' or start_time =='':
        return JsonResponse({'status':10021,'message':'parameter error'})
    result = Event.objects.filter(id = eid)
    if result:
        return JsonResponse({'status':10022,'message':'event id already exists.'})
    result = Event.objects.filter(name =name)
    if result:
        return JsonResponse({'status':10023,'message':'event name already exist.'})
    if status == '':
        status = 1

    try:
        Event.objects.create(id=eid,name=name,limit=limit,address=address,status=int(status),start_time=start_time)
    except ValidationError as e:
        error = 'start_time format error. IT must be in YYYY-MM-DD HH:MM:SS format.'
        return JsonResponse({'status':10024,'message':error})
    return JsonResponse({'status':200,'message':'add event success!'})

# 发布会查询接口
def get_event_list(request):
    eid = request.GET.get('eid','')  # 发布会ID
    name = request.GET.get('name','') # 发布会名称

    if eid =='' and name=='':
        return JsonResponse({'status':10021,'message':'parameter error'})

    if eid !='':
        event = {}
        try:
            result = Event.objects.get(id=eid)
        except ObjectDoesNotExist:
            return JsonResponse({'status':10022,'message':'query result is empty'})
        else:
            event['name'] = result.name
            event['limit'] = result.limit
            event['status'] = result.status
            event['address'] = result.address
            event['start_time'] = result.start_time
            return JsonResponse({'status':200,'message':'success','data':event})
    if name !='':
        datas = []
        results = Event.objects.filter(name__contains=name)
        if results:
            for r in results:
                event = {}
                event['name'] = r.name
                event['limit'] = r.limit
                event['status'] = r.status
                event['address'] = r.address
                event['start_time'] = r.start_time
                datas.append(event)
            return JsonResponse({'status':200,'message':'success','data':datas})
        else:
            return JsonResponse({'status':10022,'message':'query result is empty'})

# 添加嘉宾接口
def add_guest(request):
    eid = request.POST.get('eid','')   # 关联发布会
    realname = request.POST.get('realname','')  # 姓名
    phone = request.POST.get('phone','')   # 手机号
    email = request.POST.get('email','')     # 邮箱

    if eid == '' or relname =='' or phone == '':
        return JsonResponse({'status':10021,'message':'parameter error'})
    result = Event.objects.filter(id=eid)
    if not result:
        return JsonResponse({'status':10022,'message':'event id is null'})
    result = Event.objects.get(id=eid).status
    if not result:
        return JsonResponse({'status':10023,'message':'event status is not aviailble.'})

    event_limit = Event.objects.get(id=eid).limit   # 发布会限制人数
    guest_limit = Event.objects.filter(event_id=eid)  # 发布会已添加的嘉宾数

    if len(guest_limit) >= event_limit:
        retutn JsonResponse({'status':10024,'message':'evnet number is full.'})



