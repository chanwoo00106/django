# Arguments

> *args 는 함수를 시작 할때 문자열 여러개를 매개변수로 가져온다.
```python
def arg(*args):
  print(f"len of args: {len(args)}")
  for i in args:
    print(i)
    
arg() # len of args: 0
arg("Teemo") # len of args: 1 \n Teemo
arg("Teemo", "captain") # len of args: 2 \n Teemo \n captain
```

> **kwargs는 딕셔너리값을 여러개 가져온다

```python
def kwarg(**kwargs):
    print(f"len of kwargs: {len(kwargs)}")
    for key, value in kwargs.items():
        print(f"key:{key}, value:{value}")
  
kwarg() # len of kwargs: 0
kwarg(arg1="good") # len of kwargs: 1 \n key:arg1, value:good
kwarg(arg1="good", arg2="bad") # len of kwargs: 2 \n key:arg1, value:good \n key:arg2, value:bad
```

# 데코레이터

> 걍 쉽게 말해서 함수가 시작되기 전에 데코레이터에 쓰여있는 함수를 먼저 실행한다고 보면 됨

[이거 보고 이해하셈](https://www.daleseo.com/python-decorators/)
