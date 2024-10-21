import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'bank.html')


def bank_login(request):
    from studyScript import bank
    body = json.loads(request.body.decode('utf-8'))
    account = body.get("account")
    psd = body.get("psd")
    type = body.get("type")
    money = body.get("money")
    print(account, psd, type)
    bank_obj = bank.Bank(account_number=account, password=psd)
    if type in (3, 4, 5):
        bank_obj.login()
    try:
        result = bank_obj.run(str(type), money)
        if result:
            return HttpResponse(json.dumps({"code": 200, "msg": "操作成功", "data": result}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"code": 400, "msg": "操作失败", "data": result}), content_type="application/json")
    except Exception as e:
        return HttpResponse(json.dumps({"code": 500, "msg": "操作失败", "data": e}), content_type="application/json")
