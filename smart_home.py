class SmartDevice:

  def __init__(self, device_id):
    self.id = device_id
    self.is_active = False

class SmartAC(SmartDevice):

  def __init__(self, device_id):
    super().__init__(device_id)
    self.__temperature = 20

  def temp_up(self):
    if self.__temperature < 30:
      self.__temperature += 1
    else:
      print('الحرارة وصلت للحد الأعلى 30 : '+self.id)

  def temp_down(self):
    if self.__temperature > 16:
      self.__temperature -= 1
    else:
      print('الحرارة وصلت للحد الأدنى 16 : '+self.id)


  def print_info(self):
    status = 'يعمل' if self.is_active else 'متوقف'
    return f'اسم الجهاز: {self.id} | الحالة: {status} | الحرارة: {self.__temperature}'


# إنشاء كائن مكيف الصالة
ac1 = SmartAC('مكيف الصالة')
ac1.is_active = True
ac1.temp_up()
ac1.temp_up()

# إنشاء كائن مكيف الغرفة
ac2 = SmartAC('مكيف الغرفة')
ac2.is_active = True
ac2.temp_down()


file = open('./a_status.txt', 'w', encoding='utf-8')
file.write(ac1.print_info() + '\n')
file.write(ac2.print_info() + '\n')
file.close()

print('تم حفظ حالة المكيفات في الملف بنجاح!')