Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>>  def frameword(PWord) -> None:
...      print("*")
...      print(f"{PWord}*")
...      def main():
...     print("program starting.")
...     word = str(input("insert word:"))
...     
SyntaxError: unexpected indent
>>> frameWord(word)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    frameWord(word)
NameError: name 'frameWord' is not defined
