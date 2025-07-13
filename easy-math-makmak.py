def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "หารไม่ได้ (หารด้วยศูนย์)"
    return a / b

def average(a, b):
    return (a + b) / 2

def main():
    print("==== โปรแกรมคำนวณเลขพื้นฐาน ====")

    try:
        num1 = float(input("กรอกเลขตัวที่ 1: "))
        num2 = float(input("กรอกเลขตัวที่ 2: "))
    except ValueError:
        print("กรุณากรอกตัวเลขเท่านั้น")
        return

    print("\nผลลัพธ์:")
    print(f"ผลบวก: {add(num1, num2)}")
    print(f"ผลลบ: {subtract(num1, num2)}")
    print(f"ผลคูณ: {multiply(num1, num2)}")
    print(f"ผลหาร: {divide(num1, num2)}")
    print(f"ค่าเฉลี่ย: {average(num1, num2)}")

main()
