grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
evaluations = {'Aaron': (5, 3, 3, 5, 4,),  'Bilbo': (2, 2, 2, 3), 'Johnny': (4, 5, 5, 2),'Khendrik': (4, 4, 3),
               'Steve': (5, 5, 5, 4, 5)}
average_1 = (len(evaluations['Aaron']), len(evaluations['Bilbo']), len(evaluations['Johnny']), len(evaluations['Khendrik']),
             len(evaluations['Steve']))
average_2 = (sum(evaluations['Aaron']), sum(evaluations['Bilbo']), sum(evaluations['Johnny']), sum(evaluations['Khendrik']),
             sum(evaluations['Steve']))
average_3 = (average_2[0] / average_1[0], average_2[1] / average_1[1],average_2[2] / average_1[2],average_2[3] / average_1[3],
             average_2[4] / average_1[4])
students_1 = sorted(students)
finish = {students_1[0]: average_3[0], students_1[1]: average_3[1], students_1[2]: average_3[2], students_1[3]: average_3[3],
          students_1[4]: average_3[4]}
print(finish)