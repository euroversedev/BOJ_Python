'''
자료구조 빈출 유형
= 프린트, 커서, 대기열 등
'''

''' [ Stack ]
스택 관련 문제
빈출 유형 : 스택 사이에 다른 데이터를 삽입하거나 따로 저장해둘 필요가 있는 경우
           ex) 2504 10799
           => 1. 스택에 데이터를 직접 넣어줘서 처리 (2504에 문자를 숫자로 바꿔서 넣어준 것처럼)
           => 2. 별도의 변수에 저장해서 각 상황마다 연산 처리.
'''



''' [ Queue ]
큐 관련 문제
빈출 유형 : 요세푸스 문제 => 데크의 rotate를 이용하면 좋음
'''


''' [ Extra ]
자료 구조 문제에서 자주 사용되는 기타 방법론들..

1. 문자열은 replace( ) 메소드를 지원한다.
2. 문자열의 숫자 판별은 isnum()이 아니고 isdigit()이다.
   알파벳은 isalpha()이다.

'''


''' [review] 1406_1
https://www.acmicpc.net/board/view/54572

del S[cursor-1] 과 S = S[:cursor] + [cm...의 시간 복잡도가 O(N)인 것에 주목하자.
파이썬 리스트는 연속된 메모리 공간을 할당해서 자료를 저장하므로,
리스트의 한가운데에 원소를 삽입/삭제하기 위해서는 그 자리 이후의 원소를 모두 밀거나 당겨야 한다.

이 문제를 해결하기 위해서는 다음 중 한가지를 선택해야 한다.
1. 리스트의 맨 뒤에서만 삽입/삭제하는 알고리즘 구현 => 스택(or 큐) 두 개로 구현
2. 한 가운데의 원소를 삽입/삭제했을 때 이외의 원소는 건드릴 필요가 없는 자료구조 사용 => Linked List
'''

''' review
1406_1.py를 참고하길 바람.

"리스트의 맨 뒤에서만 삽입/삭제하는 알고리즘 구현 => 스택(or 큐) 두 개로 구현"
=> 덱 하나로 구현하려고 했더니, 커서가 맨 처음이랑 마지막에 있을 때를 구별을 못하네..
=> 걍 큐 두개 쓰자

프린트 or 에디터(1406)과 같이
커서를 이용하거나 인덱스를 따로 저장해야하는 경우는
단순 구현으로 풀기보다는 자료구조를 이용하면 쉽게 풀 수 있음. 매우 중요!
"커서, 대기열, 인덱스 문제 = 자료구조"
'''