def students():
    python=['harika','swapna','dhanya','kavya']
    webapplication=['harika','kavya','amulya']
    subject=list(set(python).intersection(set(webapplication)))
    print('students in python and appliation are')
    print(subject)
    second=list(set(python).union(set(webapplication)))
    third=list(set(second).difference(set(subject)))
    print('the list of students who are not common in both the classes are')
    print(c)
students()