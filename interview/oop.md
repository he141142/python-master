# OOP
## Question:
### Giải thích khái niệm đa hình tại thời điểm biên dịch và đa hình tại thời điểm chạy trong lập trình hướng đối tượng.

Trong lập trình hướng đối tượng, đa hình là một khái niệm quan trọng liên quan đến khả năng của đối tượng để thể hiện hình dạng và hành vi khác nhau dựa trên kiểu của nó. 
Đa hình giúp cho mã nguồn dễ dàng mở rộng và tái sử dụng, đồng thời cung cấp tính linh hoạt và tương thích trong việc làm việc với các đối tượng khác nhau.

Có hai khái niệm quan trọng liên quan đến đa hình trong lập trình hướng đối tượng: đa hình tại thời điểm biên dịch (compile-time polymorphism) và đa hình tại thời điểm chạy (runtime polymorphism).

#### Đa hình tại thời điểm biên dịch (Compile-time Polymorphism):
Đa hình tại thời điểm biên dịch được thực hiện thông qua cơ chế quản lý hàm nạp chồng (function overloading)
và toán tử nạp chồng (operator overloading). Khi có nhiều hàm hoặc toán tử cùng tên trong cùng một lớp,
nhưng có các tham số khác nhau hoặc kiểu dữ liệu khác nhau, 
trình biên dịch sẽ xác định xem hàm hoặc toán tử nào được gọi dựa trên kiểu và số lượng tham số truyền vào.
Việc này giúp đảm bảo rằng các hành vi khác nhau có thể được kích hoạt tùy thuộc vào các tham số đầu vào tại
thời điểm biên dịch.
#### Đa hình tại thời điểm chạy (Runtime Polymorphism):
Đa hình tại thời điểm chạy được thực hiện thông qua kỹ thuật gọi phương thức ảo (virtual method invocation) và kế thừa (inheritance). Khi có một phương thức ảo trong lớp cơ sở và các lớp dẫn xuất có thể ghi đè phương thức đó, việc gọi phương thức sẽ được xác định tại thời điểm chạy dựa trên kiểu của đối tượng thực sự được tạo ra. Điều này cho phép một biến của lớp cơ sở có thể tham chiếu đến các đối tượng khác nhau và gọi các phương thức khác nhau tùy thuộc vào đối tượng thực tế đang được tham chiếu.

#### đưa ra ví dụ về đa hình
Để minh họa khái niệm đa hình trong lập trình hướng đối tượng, hãy xem xét một ví dụ về đa hình tại thời điểm chạy (runtime polymorphism) sử dụng kế thừa và phương thức ảo.

```python
class Shape:
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

# Tạo các đối tượng
shape1 = Rectangle(4, 5)
shape2 = Circle(3)

# Gọi phương thức calculate_area
print("Diện tích hình chữ nhật:", shape1.calculate_area())
print("Diện tích hình tròn:", shape2.calculate_area())
```

### Đặc điểm chính của lập trình hướng đối tượng là gì?
Lập trình hướng đối tượng (OOP - Object-Oriented Programming) là một phương pháp lập trình trong đó chương trình được tổ chức xung quanh các đối tượng,
và các đối tượng này tương tác với nhau để thực hiện các hoạt động. 
Dưới đây là một số đặc điểm chính của lập trình hướng đối tượng:

#### Đối tượng (Object): 
Lập trình hướng đối tượng xem các thành phần của chương trình như là các đối tượng độc lập, có trạng thái (state) và hành vi (behavior) riêng. Mỗi đối tượng có thể chứa dữ liệu và phương thức để thực hiện các thao tác trên dữ liệu đó.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Tạo đối tượng từ lớp Person
person = Person("John", 25)
person.display_info()
```
#### Tính đóng gói (Encapsulation): 
Tính đóng gói cho phép che dấu thông tin chi tiết của một đối tượng và chỉ tiết lộ các phương thức công khai để tương tác với đối tượng.
Điều này giúp bảo vệ dữ liệu và đảm bảo tính nhất quán trong chương trình.
```python
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance

# Sử dụng lớp BankAccount
account = BankAccount()
account.deposit(1000)
account.withdraw(500)
print("Balance:", account.get_balance())
```
#### Kế thừa (Inheritance): 
Kế thừa cho phép xây dựng lớp mới (lớp dẫn xuất) dựa trên các định nghĩa có sẵn của một lớp khác (lớp cơ sở).
Lớp dẫn xuất kế thừa các thuộc tính và phương thức của lớp cơ sở, từ đó mở rộng và thay đổi hành vi của lớp cơ sở.


Cú pháp kế thừa:

```text
class BaseClass:
Body of base class

class DerivedClass(BaseClass):
Body of derived class
```
```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def info(self):
    print(self.name + ",", self.age, "years old.")

# Student inherits from Person
# without add any other properties or methods
class Student(Person):
  pass

# create an object of Student class
kane = Student("Kane", 29)
kane.info()
```


#### Đa hình (Polymorphism):
Đa hình cho phép các đối tượng cùng kiểu có thể thực hiện các hành vi khác nhau dựa trên kiểu đối tượng thực tế đang được tham chiếu.
Điều này giúp đơn giản hóa việc xử lý và tương tác với các đối tượng khác nhau một cách linh hoạt.
#### Trừu tượng (Abstraction): 
Trừu tượng cho phép tạo ra các lớp trừu tượng (abstract class) hoặc giao diện (interface) để mô hình hóa các khái niệm chung và thuộc tính quan trọng của các đối tượng. Điều này giúp tạo ra một mức độ trừu tượng cao và giảm sự phụ thuộc vào chi tiết cụ thể của triển khai.
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Sử dụng trừu tượng với lớp Animal
dog = Dog()
cat = Cat()
print(dog.speak())  # Output: "Woof!"
print(cat.speak())  # Output: "Meow!"
```

### Giải thích khái niệm đóng gói và ẩn thông tin trong lập trình hướng đối tượng.

```
Đóng gói (Encapsulation) và ẩn thông tin (Information Hiding) là hai khái niệm liên quan trong lập trình hướng đối tượng, nhằm bảo vệ dữ liệu và giới hạn truy cập đến thông tin quan trọng của một đối tượng. Dưới đây là giải thích cho từng khái niệm:

Đóng gói (Encapsulation): Đóng gói là quá trình đưa các thuộc tính (biến) và phương thức (hành vi) liên quan vào một đối tượng duy nhất. Đối tượng là một thực thể độc lập có khả năng tồn tại, có trạng thái (dữ liệu) và hành vi (phương thức) của riêng nó. Việc đóng gói giúp tạo ra một mức độ bao bọc cho đối tượng, làm cho dữ liệu và phương thức liên quan trở nên ổn định và gắn kết với nhau.

Ẩn thông tin (Information Hiding): Ẩn thông tin là quá trình che dấu thông tin chi tiết của một đối tượng và chỉ tiết lộ giao diện công khai để tương tác với đối tượng đó. Điều này đảm bảo rằng thông tin bên trong đối tượng không thể truy cập và thay đổi trực tiếp từ bên ngoài. Thông tin chi tiết và triển khai của một đối tượng được giữ riêng tư (private), chỉ có các phương thức công khai (public methods) được cung cấp để tương tác với đối tượng. Điều này đảm bảo tính nhất quán và bảo mật dữ liệu.

Mục tiêu của đóng gói và ẩn thông tin là tạo ra một giao diện công khai (public interface) cho đối tượng, thông qua đó mọi tương tác và thao tác trên đối tượng đều được thực hiện qua các phương thức công khai được cung cấp. Điều này giúp bảo vệ dữ liệu và đảm bảo tính nhất quán trong chương trình, đồng thời cung cấp sự linh hoạt và khả năng mở rộng trong việc thay đổi triển khai bên trong mà không ảnh hưởng đến mã nguồn bên ngoài sử dụng đối tượng đó.

Trong lập trình hướng đối tượng, chúng ta sử dụng các từ khóa truy cập như private, protected, public và cung cấp các phương thức getter và setter để kiểm soát quyền truy cập và truy xuất dữ
```

#### python có việc ẩn đối tượng hay không
Trong Python, không có một cách rõ ràng để ẩn hoàn toàn thông tin của một đối tượng.
Python không hỗ trợ kiểu truy cập private như một số ngôn ngữ khác như Java hoặc C++. Tuy nhiên, Python cung cấp một cơ chế cho phép người lập trình gợi ý rằng một thuộc tính hoặc phương thức nên được coi là "ẩn" và không nên truy cập trực tiếp từ bên ngoài.

Theo quy ước thông thường, trong Python, một thuộc tính hoặc phương thức được coi là "ẩn" bằng cách sử dụng một dấu gạch dưới đầu tên của nó (_). Điều này chỉ ra rằng thuộc tính hoặc phương thức đó là nội bộ cho lớp và không nên được truy cập trực tiếp từ bên ngoài. Tuy nhiên, việc sử dụng dấu gạch dưới chỉ là một gợi ý, không phải là một ràng buộc cú pháp.

```python
class MyClass:
    def __init__(self):
        self._private_variable = 10

    def _private_method(self):
        print("This is a private method.")

    def public_method(self):
        print("This is a public method.")

# Sử dụng lớp MyClass
obj = MyClass()
print(obj._private_variable)  # Gợi ý không nên truy cập trực tiếp
obj._private_method()         # Gợi ý không nên gọi trực tiếp
obj.public_method()           # Gọi phương thức công khai
```

```text
Mặc dù thuộc tính và phương thức có dấu gạch dưới được coi là "ẩn", nhưng vẫn có thể truy cập và gọi chúng từ bên ngoài đối tượng. Việc này dựa vào tinh thần "nguyên tắc đồng lòng" (principle of least astonishment) trong Python, khuyến khích người lập trình sử dụng thuộc tính và phương thức một cách có trách nhiệm, tránh truy cập và sửa đổi trực tiếp các thuộc tính và phương thức "ẩn" từ bên ngoài.
```

### Phân biệt giữa lớp trừu tượng (Abstract) và giao diện (Interface) trong lập trình hướng đối tượng.
Lớp trừu tượng (Abstract Class) và giao diện (Interface) là hai khái niệm quan trọng trong lập trình hướng đối tượng, được sử dụng để mô hình hóa các khái niệm chung và định nghĩa các hành vi chuẩn cho các đối tượng. Dưới đây là sự phân biệt giữa lớp trừu tượng và giao diện:

- Lớp trừu tượng (Abstract Class):
    + Lớp trừu tượng là một lớp mà không thể tạo ra các đối tượng cụ thể từ đó.
    + Nó được sử dụng để mô hình hóa một khái niệm chung và định nghĩa các phương thức có sẵn nhưng chưa được triển khai hoàn chỉnh.
    + Lớp trừu tượng có thể chứa cả các phương thức trừu tượng (abstract methods) và các phương thức đã được triển khai.
    + Các lớp dẫn xuất (concrete classes) kế thừa từ lớp trừu tượng và phải triển khai (override) tất cả các phương thức trừu tượng được định nghĩa trong lớp trừu tượng.
    + Lớp trừu tượng được định nghĩa bằng từ khóa abc.ABC và phương thức trừu tượng được định nghĩa bằng decorator @abstractmethod.
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        return "animal speak"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
```

- Giao diện (Interface):
    + Giao diện là một tập hợp các phương thức mà các lớp khác nhau có thể triển khai.
    + Nó chỉ định các hành vi và chức năng mà một đối tượng phải có.
    + Giao diện không chứa bất kỳ triển khai nào của các phương thức, chỉ định các phương thức và các đặc điểm công khai.
    + Các lớp khác nhau có thể triển khai cùng một giao diện và cung cấp các triển khai riêng cho các phương thức của giao diện đó.
    + Trong Python, không có từ khóa hoặc cú pháp đặc biệt để định nghĩa giao diện, mà việc định nghĩa giao diện thường dựa trên quy ước và hợp đồng giữa các lập trình viên.
    
```python
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement this method.")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
```



Khi nào sử dụng chúng:
- Interface : Khi bạn muốn tạo dựng một bộ khung chuẩn gồm các chức năng mà những module hay project cần phải có. Giống như sau khi nhận requirement của khách hàng về team ngồi với nhau và phân tích các đầu mục các tính năng của từng module, sau đó triển khai vào code viết các interface như đã phân tích,để các bạn dev có thể nhìn vào đó để thực hiện đủ các tính năng (khi đã implement rồi thì không sót một tính năng nào ^^).
- Abstract class: Giống như demo trên bạn có thể hiểu khi định nghĩa một đối tượng có những chức năng A,B,C trong đó tính năng A,B chắc chắn sẽ thực thi theo cách nào đó, còn tính năng C phải tùy thuộc vào đối tượng cụ thể là gì, như đối tượng Dog, Cat tuy chúng đều có thể phát ra âm thanh nhưng âm thanh là khác nhau. Vì vậy method Speak() là abstract method để chỉ ra rằng tính năng này còn dang dở chưa rõ thực thi, các lớp extend phải hoàn thành nốt tính năng này, còn những tính năng đã hoàn thành vẫn sử dụng như bình thường đây là những tính năng chung.

#### Ví dụ cho interface và Abstract:
Ví dụ về Abstract:
- Ví dụ Design chức năng Giỏ hàng Online shopping được liên kết với nhiều bên Tiki, Shopee, Lazada
Giỏ hàng đều có chức năng:
  + Thêm vào giỏ `def addToCart(item)`
  + Xuất bill `def billCalc()`
  + Áp dụng voucher `def applyVoucher()`
  
Nhưng chỉ  có   Tiki và Shopee là có hệ thống voucher, Lazada không hỗ trợ,các tính năng còn lại các bên đều dùng
thì mình chỉ triển khai  `Áp dụng voucher` cho 2 bên là `Tiki` và `Shopee`

Interface:
ví dụ define một interface Cart và có 2 chức năng:
+ Thêm vào giỏ `def addToCart(item)`
+ Xuất bill `def billCalc()`

bất kì một đối tượng nào triển khai interface này thì phải cung cấp các triển khai cho toàn bộ interface `Cart` (
`addToCart(item)` và  `billCalc()` đều phải triển khai
)

Note: **Một đối tượng có thể triển khai nhiều interface nhưng chỉ có thể extends 1 abstract class.**


Interface: 
- Có thể kế thừa nhiều interface(tính đa hình).
- Xây dựng được bộ khung mẫu mà các lớp phải follow theo.
- Giúp quản lý tốt, nắm bắt được các chức năng phải có cho một đối tượng nào đó.

|#|ABSTRACT|INTERFACE|
|---------|----------------------------|----------------------------|
|Ưu điểm|Có thể linh động các method. giống như một class thông thường.<br>Các class extend có thể override hoặc không override các method thường. |Có thể kế thừa nhiều interface(tính đa hình).<br>Xây dựng được bộ khung mẫu mà các lớp phải follow theo.<br>Giúp quản lý tốt, nắm bắt được các chức năng phải có cho một đối tượng nào đó.|
|Nhược điểm| Không thể extend nhiều abstract class.|Mỗi khi định nghĩa thêm tính năng, các class impelement nó đồng lọat phải thêm tính năng đó, khả năng cao sẽ không có xử lý gì.|


#### SOLID
- Single responsibility priciple (SRP)
- Open/Closed principle (OCP)
- Liskov substitution principe (LSP)
- Interface segregation principle (ISP)
- Dependency inversion principle (DIP) Trong bài viết này mình sẽ giới thiệu từng nguyên tắc trong 5 nguyên tắc trên cũng như cách áp dụng nó làm tăng chất lượng code trong Ruby


# DESIGN PATTERN

Design patterns là những giải pháp tái sử dụng cho các vấn đề phổ biến trong thiết kế và phát triển phần mềm. Chúng đại diện cho các phương pháp tốt nhất và các cách tiếp cận đã được kiểm chứng để giải quyết các thách thức cụ thể trong thiết kế và kiến trúc.

Design patterns không phải là thiết kế hoàn chỉnh hoặc đoạn mã. Thay vào đó, chúng là mô tả cấp cao về mối quan hệ và tương tác giữa các lớp, đối tượng và thành phần phần mềm. Chúng miêu tả cấu trúc, hành vi và sự cộng tác giữa các thành phần phần mềm, tập trung vào sắp xếp các lớp và đối tượng để đạt được các mục tiêu cụ thể.

Design patterns mang lại nhiều lợi ích:

Tái sử dụng: Design patterns cung cấp các giải pháp có thể được tái sử dụng trong các ngữ cảnh và ứng dụng khác nhau, tiết kiệm thời gian và công sức bằng cách sử dụng các phương pháp đã được kiểm chứng.

Dễ bảo trì: Design patterns thúc đẩy thiết kế theo cách mô đun và có cấu trúc, làm cho việc hiểu, chỉnh sửa và bảo trì mã nguồn dễ dàng hơn theo thời gian.

Mở rộng: Bằng cách tuân theo design patterns, hệ thống có thể được thiết kế để linh hoạt và thích ứng, cho phép mở rộng và phát triển dễ dàng khi yêu cầu thay đổi.

Sự cộng tác: Design patterns cung cấp ngôn ngữ và từ vựng chung cho kỹ sư phần mềm để truyền tải và chia sẻ các khái niệm và ý tưởng thiết kế.

Có một số loại design patterns, bao gồm các pattern tạo đối tượng (ví dụ: Singleton, Factory), pattern cấu trúc (ví dụ: Adapter, Decorator) và pattern hành vi (ví dụ: Observer, Strategy). Mỗi pattern giải quyết các loại vấn đề cụ thể và cung cấp hướng dẫn để giải quyết chúng.

Quan trọng là nhớ rằng design patterns không phải lúc nào cũng áp dụng hoặc cần thiết trong mọi tình huống. Chúng nên được sử dụng một cách thận trọng, dựa trên yêu cầu cụ thể và ràng buộc của dự án. Cũng quan trọng là xem xét các sự đánh đổi và nhược điểm có thể đi kèm khi sử dụng design patterns, như tăng độ phức tạp hoặc giảm hiệu năng trong một số trường hợp.

Tổng quan, design patterns là công cụ quý giá để cải thiện thiết kế phần mềm, thúc đẩy tính mô-đun và xây dựng mã nguồn có khả năng bảo trì và mở rộng.


