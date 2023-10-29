d = {"apple": 3, "car": 99, "blue": 87, "string": 33, "app": 123}

sorted(d.items())
# 키 순서대로 정렬. 리스트로 반환
[('app', 20), ('apple', 3), ('blue', 87), ('car', 99), ('string', 33)]

sorted(d)
# 키만 빼서 정렬. 리스트로 반환
['app', 'apple', 'blue', 'car', 'string']

sorted(d.items(), key=lambda x: x[1], reverse=True)
# == sorted(d.items(), key=lambda x: -x[1]) 숫자만 가능
# 값 기준 내림차순 정렬
[('app', 123), ('car', 99), ('blue', 87), ('string', 33), ('apple', 3)]

sorted(d.items(), key=lambda x: (x[1], x[0]))
# 두번째 인자 기준 정렬 후 첫번째 인자 기준 정렬
[('apple', 3), ('string', 33), ('blue', 87), ('car', 99), ('app', 123)]

list(d)
# 키 값만 빼서 리스트로 반환
['apple', 'car', 'blue', 'string', 'app']

