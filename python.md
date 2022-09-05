# python

## 출력
print 학습
```
print("Hello")

```
큰따옴표(")로 둘러싸인 문자열은 + 연산과 동일하다
```
>>> print("The" "magic show")
Themagic show

>>> print("The"+"magic show")
Themagic show

```






### 변수선언

```
Integer
a=6
a,b=(10,20)
a=b=10


```
#### String
```
imp="I'M sunho"

```
Data type String

```
str1 ="1a"
Str2 ="lala"*3
print(str2)
lalalalalala


Str1= "TYE"
a=len(Str1)
print(a)
3

Slice String
Str_tmp="abcdefghijklmn"
str1=Str_tmp[:3]
str2=Str_tmp[3:]
str3=Str_tmp[3:-1]
str4=Str_tmp[3:-2]
print(str1)
print(str2)
print(str3)
print(str4)

결과
abc
defghijklmn
defghijklm
defghijkl


```
#### 리스트
리스트를 이용하면 홀수 숫자 모음도 간단하게 표현할 수 있다 

```
odd=[1,3,5,7,9]
```

```
a=[1,2,3]
b=[1,2,"life"]
c=[1,2,["life",'is']]
d=[]
```
다음과 같이 여러가지의 리스트를 만들 수 있다.
비어있는 리스트 d는 ([])일수도 있고 a처럼 정수를 포함할수도 있고 b처럼 정수와 문자열을 포함시킬수도 있고 c처럼 문자열 리스트를 추가할 수도 있다. 요약하면 빈 리스트 d는 어떠한 값이든 늘 수 있다.
 **비어 있는 리스트는 d = list()로 생성할 수도 있다 
 
##### 리스트의 인덱싱

```
가족구성원=['나','누나','엄마','아빠'] //가족구성원 리스트 선언

>>>가족구성원
['나', '누나', '엄마', '아빠']

```

가족구성원[0]은 가족구성원의 첫번째 값을 의미한다. 따라서 가족구성원[3]은 네번째 값인 아빠를 의미한다

```
>>> 가족구성원[0]
'나'
>>> 가족구성원[3]
'아빠'

```
가족구성원[-1]은 리스트의 마지막 요소 값을 의미한다
```
>>>가족구성원[-1]
'아빠'

```
이번에는 다음 예처럼 리스트 가족구성원에 를 숫자 나, 누나, 엄마, 아빠 와 또 다른 리스트인 ['할머니', '할아버지', '삼촌']를 포함하도록 만들어 보자.

```
가족구성원 =['나', '누나', '엄마', '아빠',['할머니', '할아버지', '삼촌']]

```

![image](https://user-images.githubusercontent.com/100903674/188471638-2d194b4e-3c96-4b81-aca7-4512abdfb853.png)
다음과 같이 리스트 요소에서 요소값을 뽑아낼 수 있다.

## 입력

input 함수의 사용
```
ex)
span=input("나이가 몇살입니까?")//정수 혹은 실수로 입력하더라도 input으로 받는 값은 문자열로 인식함
spans=100-int(span) 
*/
a:데이터로 변환하고자 하는 값
그래서 데이터 값으로 변환하기 위해선 정수는 int(a) 실수는, str(a) , float(a)

/* 



print(spans)

결과
나이가 몇살입니까? 35
65

```
## 조건문

### if 문

```
money=1250
if money>=3000:
    print("택시를 타도 좋다")
elif money==0:
        print("장난해!!")
else:
    print("내료")

>>>내료
```



