# DSA-Assgn-12
class Queue:
    def __init__(self, max_size):

        self.__max_size = max_size
        self.__elements = [None]*self.__max_size
        self.__rear = -1
        self.__front = 0

    def is_full(self):
        if(self.__rear == self.__max_size-1):
            return True
        return False

    def is_empty(self):
        if(self.__front > self.__rear):
            return True
        return False

    def enqueue(self, data):
        if(self.is_full()):
            print("Queue is full!!!")
        else:
            self.__rear += 1
            self.__elements[self.__rear] = data

    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!!!")
        else:
            data = self.__elements[self.__front]
            self.__front += 1
            return data

    def display(self):
        for index in range(self.__front, self.__rear+1):
            print(self.__elements[index])

    def get_max_size(self):
        return self.__max_size

    # You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg = []
        index = self.__front
        while(index <= self.__rear):
            msg.append((str)(self.__elements[index]))
            index += 1
        msg = " ".join(msg)
        msg = "Queue data(Front to Rear): "+msg
        return msg


class Ball:
    def __init__(self, color, name):
        self.__color = color
        self.__name = name

    def __str__(self):
        return (self.__color+" "+self.__name)

    def get_color(self):
        return self.__color

    def get_name(self):
        return self.__name

# Implement Game class here


class Game:

    def __init__(self, ball_stack):
        self.ball_stack = ball_stack
        self.ball_container = []
        self.red_balls_container = []
        self.green_balls_container = []
        self.blue_balls_container = []
        self.yellow_balls_container = []

    def grouping_based_on_color(self):
        while not self.ball_stack.is_empty():
            temp = self.ball_stack.dequeue()
            if temp.get_color() == 'Red':
                self.red_balls_container.append(temp)
            elif temp.get_color() == 'Blue':
                self.blue_balls_container.append(temp)
            elif temp.get_color() == 'Green':
                self.green_balls_container.append(temp)
            elif temp.get_color() == 'Yellow':
                self.yellow_balls_container.append(temp)

    def rearrange_balls(self):
        temp = self.red_balls_container[0]
        self.red_balls_container = self.red_balls_container[1:]
        self.red_balls_container.insert(1, temp)

        temp = self.blue_balls_container[0]
        self.blue_balls_container = self.blue_balls_container[1:]
        self.blue_balls_container.insert(1, temp)

        temp = self.green_balls_container[0]
        self.green_balls_container = self.green_balls_container[1:]
        self.green_balls_container.insert(1, temp)

        temp = self.yellow_balls_container[0]
        self.yellow_balls_container = self.yellow_balls_container[1:]
        self.yellow_balls_container.insert(1, temp)

    def display_ball_details(self):
        pass


# Use different values to test your program
ball1 = Ball("Red", "A")
ball2 = Ball("Blue", "B")
ball3 = Ball("Yellow", "B")
ball4 = Ball("Blue", "A")
ball5 = Ball("Yellow", "A")
ball6 = Ball("Green", "B")
ball7 = Ball("Green", "A")
ball8 = Ball("Red", "B")
ball_list = Queue(8)
ball_list.enqueue(ball1)
ball_list.enqueue(ball2)
ball_list.enqueue(ball3)
ball_list.enqueue(ball4)
ball_list.enqueue(ball5)
ball_list.enqueue(ball6)
ball_list.enqueue(ball7)
ball_list.enqueue(ball8)

g = Game(ball_list)
g.grouping_based_on_color()
# Create objects of Game class, invoke the methods and test the program
