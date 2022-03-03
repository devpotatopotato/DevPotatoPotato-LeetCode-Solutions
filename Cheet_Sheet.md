# Cheet_Sheet

## Dictionary modules

    import collections

### defaultdict object
존재 하지 않는 key를 조회해도 default 값을 기준으로 dictionary item 생성
```
a = collections.defaultdict(int)
a['A'] = 5
a['B'] = 4
print(a))

>>> defaultdict(<class 'int'>, {'A': 5, 'B': 4})
```


### Counter object
item의 개수를 dictionary로 반환
```
a = [1, 2, 3, 4, 5, 5, 5, 6, 6]
b = collections.Counter(a)
print(b)

>>> Counter({5: 3, 6: 2, 1: 1, 2: 1, 3: 1, 4: 1})

* Counter.most_common
```

### OrderedDict object
dictionary 순서 유지 (python 3.7+ 부터는 defulat dictionary도 ordered)

```
a = collections.OrderedDict({"a": 1, "b": 2, "c": 3})
print(a)

>>> OrderedDict([('a', 1), ('b', 2), ('c', 3)])
```

## Regex

### [ ]: [ ] 안에 들어있는 문자들 중 한 개의 문자와 매치

    [a-z]: a~z / [0-5] 0~5  중 한개의 문자와 매치
    [a-zA-Z]: 알파벳 전체 / [0-9] 숫자
    ^ == not / ex) [^0-9] == 숫자 아닌 문자만
    
    [자주 사용하는 문자 클래스]
        \d == [0-9]
        \D == [^0-9]
        \s == [ \t\n\r\f\v] | whitespace 문자와 매치
        \S == [^ \t\n\r\f\v] | not whitespace 와 매치
        \w == [a-zA-Z0-9_]
        \W == [^a-zA-Z0-9_]


### . : \n을 제외한 모든 문자와 매치

    a.b == "a + 모든문자 +b"
    ex) a0b -> 0 . 매치 | aab -> a . 매치 | abc -> 매치 x
    
    a[.]b == "a + . + b"


### * : * 바로 앞 문자가 0번부터 무한번 반복 가능
    ca*t == ct ("a" 0번 반복)
         == cat ("a" 1번 반복)
         == caaat ("a" 3번 반복)

### + : + 바로 앞 문자가 1번부터 무한번 반복 가능
    ca+t == ct ("a" 0번 반복)
         == cat ("a" 1번 반복)
         == caaat ("a" 3번 반복)
    
### {m, n}, ?
    1. {m} | 반드시 m회 반복
      ex) ca{2}t == caat 
    
    2. {m, n} | m~n회 반복
      ex) ca{2, 5}t == cat 
                    == caat
                    == caaaaat

    3. ? == {0, 1}
      ex) ab?c == "a + b(있어도 되고 없어도 됨) + c"

### | : OR
    >>> re.match("Hello|Bye", "Hello my name is...").group()
    Hello

### ^ : 문자열의 맨 처음과 일치
    >>> print(re.search('^Life', 'Life is too short'))
    <re.Match object; span=(0, 4), match='Life'>
    >>> print(re.search('^Life', 'My Life'))
    None

### $ : 문자열의 맨 끝과 일치


### etc..
* #### re.match / re.search / re.findall / re.finditer

* \A : 문자열의 맨 처음과 일치
    * ^ : 각 줄의 처음 (re.MULTILINE)
    * \A : 전체 문자열의 처음 (re.MULTILINE)

* \Z : 문자열의 맨 끝과 일치
    * $ : 각 줄의 끝 (re.MULTILINE)
    * \Z : 전체 문자열의 끝 (re.MULTILINE)

* \b : Word Boundary, whitespace로 구분
    ```
    >>> p = re.compile(r'\bclass\b')
    >>> print(p.search('no class at all'))  
    <re.Match object; span=(3, 8), match='class'>

    >>> print(p.search('the declassified algorithm'))
    None

    >>> print(p.search('one subclass is'))
    None
    ```
    * Raw String임을 알려주는 r반드시 붙여야 함

* \B : not \b
    ```
    >>> p = re.compile(r'\Bclass\B')
    >>> print(p.search('no class at all'))  
    None
    
    >>> print(p.search('the declassified algorithm'))
    <re.Match object; span=(6, 11), match='class'>
    
    >>> print(p.search('one subclass is'))
    None
    ```

### ( ) : groupping
    >>> p = re.compile('(ABC)+')
    >>> m = p.search('ABCABCABC OK?')
    >>> print(m)
    <re.Match object; span=(0, 9), match='ABCABCABC'>
    >>> print(m.group())
    ABCABCABC

* groupping 사용 예시)

    ```
    >>> p = re.compile(r"\w+\s+(\d+[-]\d+[-]\d+)")
    >>> m = p.search("park 010-1234-1234")
    ```
    에서...
    ```
    >>> p = re.compile(r"(\w+)\s+((\d)+[-]\d+[-]\d+)")
    >>> m = p.search("park 010-1234-1234")
    >>> print(m.group(1))
    park
    >>> print(m.group(2))
    010-1234-1234
    >>> print(m.group(3))
    010
    ```
* .group(0) : match된 전체 문자열
* .group(n) : n 번째 그룹의 문자열

#### group은 재참조 가능
    ```
    >>> p = re.compile(r'(\b\w+)\s+\1')
    >>> p.search('Paris in the the spring').group()
    'the the'
    ```

#### group 이름 붙이기
    (?P<그룹명>...)

* ex)
    ```
    >>> p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
    >>> m = p.search("park 010-1234-1234")
    >>> print(m.group("name"))
    park
    ```
* 재참조
    ```
    >>> p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
    >>> p.search('Paris in the the spring').group()
    'the the'
    ```

### Lookahed Assertions
    ?=... : ...에 해당하는 정규식과 match 되야함 / 해당 문자열 소비 x
    !=... : ...에 해당하는 정규식과 match 되지 않아야 함 / 해당 문자열 소비 x
* ex)
    ```
    >>> p = re.compile(".+(?=:)")
    >>> m = p.search("http://google.com")
    >>> print(m.group())
    http
    ```

### re.sub
    ```
    print(re.sub("white|blue", "XXX", "I like white and blue."))
    >>> I like XXX and XXX.
    ```
* count
    ```
    print(re.sub("white|blue", "XXX", "I like white and blue.", count=1))
    >>> I like XXX and blue.
    ```

* re.subn : 튜플로 return\
    ex)
    ```
    print(re.subn("white|blue", "XXX", "I like white and blue."))
    >>> ('I like XXX and XXX.', 2)

    print(re.subn("white|blue", "XXX", "I like white and blue.", 1))
    >>> ('I like XXX and blue.', 1)
    ```

#### 재참조
```\g<그룹이름>```로 그룹 이름 참조

* ex)
    ```
    >>> p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
    >>> print(p.sub("\g<phone> \g<name>", "park 010-1234-1234"))
    010-1234-1234 park
    ```
    ```
    >>> p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
    >>> print(p.sub("\g<2> \g<1>", "park 010-1234-1234"))
    010-1234-1234 park
    ```

#### sub의 parameter로 함수 사용
* ex)
    ```
    >>> def hexrepl(match):
            value = int(match.group())
            return hex(value)

    >>> p = re.compile(r'\d+')
    >>> p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.')
    'Call 0xffd2 for printing, 0xc000 for user code.'
    ```

### greedy, non-greedy
* ex)
    ```
    >>> s = '<html><head><title>Title</title>'
    >>> len(s)
    32
    >>> print(re.match('<.*>', s).span())
    (0, 32)
    >>> print(re.match('<.*>', s).group())
    <html><head><title>Title</title>
    ```
<.*>가 \<html>로 match될 걸 기대했지만 *는 greedy하여 \<html>\<head>\<title>Title\</title>가 모두 match됨

non-greedy한 ?을 사용하여 해결
```
>>> print(re.match('<.*?>', s).group())
<html>
```

### reference
* https://wikidocs.net/4308
* https://wikidocs.net/4309