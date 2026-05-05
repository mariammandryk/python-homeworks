import my_module


st1 = my_module.Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = my_module.Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = my_module.Group('PD1')
gr.add_student(st1)
gr.add_student(st2)

print(gr)

assert gr.find_student('Jobs') == st1
assert gr.find_student('Jobs2') is None

gr.delete_student('Taylor')
print(gr)

print("OK")