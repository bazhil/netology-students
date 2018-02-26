students=[
  {'имя': 'Билл', 'фамилия': 'Гейтс', 'пол': 'мужской', 'опыт в программировании': 'нет', 'оценки': [8, 7, 6, 5, 4], 'оценка за экзамен': 6},
  {'имя': 'Исаак', 'фамилия': 'Ньютон', 'пол': 'мужской', 'опыт в программировании': 'да', 'оценки': [10, 9, 10, 8, 9], 'оценка за экзамен': 9},
  {'имя': 'Павел', 'фамилия': 'Дуров', 'пол': 'мужской', 'опыт в программировании': 'да', 'оценки': [10, 9, 10, 8, 9], 'оценка за экзамен': 9},
  {'имя': 'Софья', 'фамилия': 'Великая', 'пол': 'женский', 'опыт в программировании': 'да', 'оценки': [10, 9, 10, 9, 9], 'оценка за экзамен': 8},
  {'имя': 'Валентина', 'фамилия': 'Терешкова', 'пол': 'женский', 'опыт в программировании': 'нет', 'оценки': [6, 5, 6, 6, 5], 'оценка за экзамен': 7},
  {'имя': 'Елена', 'фамилия': 'Ларина', 'пол': 'женский', 'опыт в программировании': 'да', 'оценки': [6, 8, 9, 10, 7], 'оценка за экзамен': 6}
]

def average_mark(students):
  hw_marks = 0
  for student in students:
    hw_marks += sum(student['оценки'])/len(student['оценки'])
  return hw_marks/len(students)

def average_exam_marks(students):
  exam_marks=0
  for student in students:
    exam_marks+=student['оценка за экзамен']
  return exam_marks/len(students)


def average_group(students, target_group, value_group):
  
  sorted_students=[]
  for student in students:
    if student[target_group]==value_group:
      sorted_students.append(student)
  return sorted_students
  

def best_student(students):
  best_mark=0
  best_student=[]
  for student in students:
    average_student_mark=sum(student['оценки'])/len(student['оценки'])
    max_mark=0.6*average_student_mark+0.4*student['оценка за экзамен']
    if max_mark>best_mark:
      best_mark=max_mark
      best_student=[student['имя']]
    elif max_mark==best_mark:
      best_student.append(student['имя'])
  if len(best_student)==1:
    print('Лучший студент: ', best_student[0], ' с интегральной оценкой ', best_mark)  
  elif len(best_student)>1:
    print('Лучшие студенты: ', ', '.join(best_student), ' с интегральной оценкой ', best_mark)
  else:
    print('Лучшие студенты не выявлены')
  
while True:
  print('Введите команду из перечисленных: a - для вывода средней оценки, b - средняя оценка в разрезе, c - лучшие студенты')
  command=input()
  if command=="a":
    result=average_mark(students)
    print('Средняя оценка:',result) 
    result=average_exam_marks(students)
    print('Средняя оценка за экзамен:', result)
  elif command=="b":
    print('Введите имя группы: пол, опыт в программировании')
    target_group=input()
    if target_group=='пол':
      print('Введите значение группы: мужской, женский')
    elif target_group=='опыт в программировании':
      print('Введите значение группы: да, нет')
    else:
      print('Введено неправильное имя группы')
      continue 
    value_group=input()
    if target_group=='пол':
      if value_group=='мужской':
        group='мужчин'
      else:
        group='женщин'
    elif terget_group=='опыт в программировании':
      if value_group=='да':
        group='студентов с опытом'
      else:
        group='студентов без опыта'
    sorted_students=average_group(students, target_group, value_group)
    result=average_mark(sorted_students)
    print('Средняя оценка за домашние задания у {}:'.format(group), result) 
    result=average_exam_marks(sorted_students)
    print('Средняя оценка за экзамен у {}:'.format(group), result)
  elif command=="c":
    best_student(students)
  else:
    print("Некорректный ввод")
  

