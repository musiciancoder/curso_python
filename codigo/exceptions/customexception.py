class MyException(Exception):
    pass

try:
    raise  MyException("Oh no!")
except MyException as e:
    print(e)

"""
class MyException extends Exception {
    public MyException(String message) {
        super(message);
    }
}

public class ExceptionDemo {
    public static void main(String[] args) {
        try {
            throw new MyException("Oh no!");
        } catch (MyException e) {
            System.out.println(e.getMessage());
        }
    }
}
"""

