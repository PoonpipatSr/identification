# โปรแกรมคำนวณเลขพื้นฐาน

print("==== โปรแกรมคำนวณเลขพื้นฐาน ====")

num1 = float(input("กรอกเลขตัวที่ 1: "))
num2 = float(input("กรอกเลขตัวที่ 2: "))

sum_result = num1 + num2
diff_result = num1 - num2
prod_result = num1 * num2

if num2 != 0:
    div_result = num1 / num2
else:
    div_result = "หารไม่ได้ (หารด้วยศูนย์)"

print("\nผลลัพธ์:")
print(f"ผลบวก: {sum_result}")
print(f"ผลลบ: {diff_result}")
print(f"ผลคูณ: {prod_result}")
print(f"ผลหาร: {div_result}")
print(f"ค่าเฉลี่ย: {(num1 + num2) / 2}")
