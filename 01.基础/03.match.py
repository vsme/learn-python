# 假设我们要根据天气情况给出不同的建议
weather = "rainy"
# 使用match语句进行多分支判断
match weather:
    case "sunny":
        print("天气晴朗，适合出门散步。")  # 如果是晴天
    case "rainy":
        print("下雨了，记得带伞。")        # 如果是雨天
    case "snowy":
        print("下雪了，注意保暖。")        # 如果是雪天
    case _:
        print("无法识别的天气类型。")      # 其他情况

# 判断一个月份属于哪个季节
month = 4
match month:
    case 12 | 1 | 2:# 12月、1月、2月属于冬季
        print("冬季")
    case 3 | 4 | 5:# 3月、4月、5月属于春季
        print("春季")
    case 6 | 7 | 8:# 6月、7月、8月属于夏季
        print("夏季")
    case 9 | 10 | 11:# 9月、10月、11月属于秋季  
        print("秋季")
    case _:# 其他情况
        print("月份无效")

# 判断分数等级
score = 85

match score:
    case ma if ma >= 90:
        print("成绩优秀")
    case ma if 80 <= ma < 90:
        print("成绩良好")
    case ma if 60 <= ma < 80:
        print("成绩及格")
    case _:
        print("成绩不及格")

def f(seq):
  match seq:
    case (x, y, *rest):
        return f"≥2 个元素：x={x}, y={y}, rest={rest}"
    case [x, y, rest]:   # 只有长度==3时才会走到这里（且上面的分支已先匹配到更宽）
        return f"正好 3 个：{x}, {y}, {rest}"
    case _:
        return "不匹配"

print(f([1, 2]))          # ≥2 个元素：x=1, y=2, rest=[]
print(f([1, 2, 3]))       # ≥2 个元素：x=1, y=2, rest=[3]
print(f([1, 2, 3, 4]))    # ≥2 个元素：x=1, y=2, rest=[3, 4]
print(f((1, 2, 3, 4)))    # ≥2 个元素：x=1, y=2, rest=[3, 4]

def handle(msg):
    match msg:
        case {"kind": "pay", "amount": amt} if amt > 0:
            return f"支付 {amt}"
        case {"kind": "pay", "amount": amt} if amt <= 0:
            return "金额非法"
        case _:
            return "未知消息"

print(handle({"kind": "pay", "amount": 100}))   # 支付 100
print(handle({"kind": "pay", "amount": 0}))     # 金额非法
print(handle({"kind": "pay", "amount": -5}))    # 金额非法
print(handle({"kind": "refund", "amount": 50})) # 未知消息
print(handle({"foo": 1}))                       # 未知消息
print(handle(["pay", 100]))                     # 未知消息
