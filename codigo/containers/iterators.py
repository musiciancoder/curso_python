#esto no esta en el curso, lo saque de W3SCHOOLS

#The for loop actually creates an iterator object and executes the next() method for each loop.

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

"""
When to Use Iterators Instead of for Loops
✅ When dealing with large datasets or streaming data ✅ When writing custom iteration logic ✅ When working with infinite sequences ✅ When optimizing performance and memory efficiency

Since you're transitioning into Python and Machine Learning, iterators are essential in frameworks like TensorFlow and PyTorch, where data is processed in batches efficiently.

Would you like to see how iterators apply to data pipelines in machine learning?"""