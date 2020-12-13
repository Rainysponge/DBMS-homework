import datetime
import pymysql
from django.utils import timezone
from django.db.models import Sum
from .models import Pay, Commodity, Order


def get_30_days_earn_data(shop):
    today = timezone.now().date()

    pay_money = []
    dates = []
    for i in range(30, -1, -1):
        date = today - datetime.timedelta(days=i)
        dates.append(date.strftime('%m/%d'))
        pay_details = Pay.objects.filter(shop=shop, pay_time__year=date.year,
                                         pay_time__month=date.month, pay_time__day=date.day)
        result = pay_details.aggregate(pay_details_sum=Sum('pay_money'))
        pay_money.append(result['pay_details_sum'] or 0)

    return dates, pay_money


def get_commodity_consumption_data(shop):
    commodity_list = []
    pay_money = []
    res = []
    count = 0
    # pay_today = Pay.objects.filter(buyer_id=user, pay_time__year=today.year,
    #                                pay_time__month=today.month, pay_time__day=today.day)
    try:
        commodity = Commodity.objects.filter(shop=shop)
    except:
        return commodity_list, pay_money
    for item in commodity:
        commodity_list.append(item.commodity_name)
        try:
            order_detail = Order.objects.filter(commodity_id=item)
        except:
            result = 0
            pay_money.append(result)
            continue

        number_sum = order_detail.aggregate(number_sum=Sum('number'))
        result = number_sum['number_sum'] * item.commodity_price if number_sum['number_sum'] else 0
        pay_money.append(result)
        res.append({'value': result, 'name': item.commodity_name})

    if len(res) <= 3:
        return res
    else:
        res = sorted(res, key=lambda x: x['value'], reverse=True)
        return res[:3]


def func(nums):
    try:
        PY_MYSQL_CONN_DICT = {
            "host": '192.168.0.214',
            "port": 3306,
            "user": 'root',
            "passwd": '******',
            "db": 'POS'
        }  # 密码需要更改后使用

        conn = pymysql.connect(**PY_MYSQL_CONN_DICT)  # 游标
        cusor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        # 调用 p1 存储过程，传入4个参数
        nums = tuple(nums)  # 需要元组形式
        cusor.callproc('p1', args=nums)

        # 返回获得的集合，即存储函数中的 SELECT * FROM tmp; 结果
        res1 = cusor.fetchall()
        print(res1)

        # 以 python 固定格式获取返回的值：@_存储过程名_0, 第一个返回值
        cusor.execute("select @_p1_0, @_p1_1, @_p1_2, @_p1_3")
        res2 = cusor.fetchall()
        print(res2)

        conn.commit()
        cusor.close()
        conn.close()
    except:
        pass


def createTrigglr():
    try:
        db = pymysql.connect("localhost", "root", "******", "POS")

        # 使用cursor()方法创建一个游标对象
        cursor = db.cursor()
        sql = '''create trigger ygdelete after delete on store_pay
                begin
                delete from store_order where store_order.id=:old.id; 
                end;'''
        # 使用executte()方法执行SQL语句
        cursor.execute(sql)

        # 使用fetall()获取全部数据
        data = cursor.fetchall()

        # 打印获取到的数据
        # print(data)

        # 关闭游标和数据库的连接
        cursor.close()
        db.close()
    except:
        pass
