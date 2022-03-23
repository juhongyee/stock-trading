class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#LinkedList 클래스 정의
class LinkedList:
    def __init__(self):
        dummy = Node("dummy") # Node에 관한 객체 생성 인스턴트화한다?
        self.head = dummy #self의 값들을 앞서 만든 dummy에 대해 연
        self.tail = dummy

        self.current = None
        self.befor = None

        self.num_of_data = 0

    def append(self,data):
        new_node = Node(data)
        self.tail.next = new_node #이 현재 리스트의 맨 끝에 node 추가
        self.tail = new_node      #리스트의 맨 끝을 new_node로 변경

        self.num_of_data += 1

    def delete(self):
        pop_data = self.current.data #현재 탐색 위치의 data

        if self.current is self.tail: #is는 a,b가 같은 객체를 가리키면 true, 값과 형태만 같은 것이 아니라 완전히 같은 녀석을 가리키고 있음.
            self.tail = self.before #현재 위치가 맨 마지막 일때 맨 마지막을 바로 직전 node 즉,끝 바로 전 node로 바꿈.

        self.before.next = self.current.next #현재 위치 원래 다음 놈을 before에 붙여
        self.current = self.befor #중요 : current를 next가 아닌 befor로 변경,아마 맨 마지막 노드때문일듯

        self.num_of_data -= 1

        return pop_data
    
    #얘는 0짜리 node Push하면 못 쓰겠다.
    def first(self): #맨 앞 node 검색
        if self.num_of_data == 0: #데이터가 없는 경우 첫번째 node도 없기 때문에 None 리턴,
            return None

        self.befor = self.head #head가 dummynode임.
        self.current = self.head.next

        return self.current.data

    def next(self):
        if self.current.next != None: #맨 끝 node
            self.before = self.current #befor을 현재 current로
            self.current = self.current.next #current를 current의 next로

            return self.current.data
        else:
            return None

    def size(self):
        return self.num_of_data

a = LinkedList()
a.append(4)
a.append(5)
a.append(6)

a.first()# first를 먼저 써서 current를 갱신해줘야 함.
a.next()
a.next()
print(a.current.data,a.size())
