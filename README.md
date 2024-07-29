# Enigma

> The Enigma machine is a cipher device developed and used in the early- to mid-20th century to protect commercial, diplomatic, and military communication. It was employed extensively by Nazi Germany during World War II, in all branches of the German military. The Enigma machine was considered so secure that it was used to encipher the most top-secret messages.
- Wikipedia

<br>


## Use
  ```python
enigma = Enigma()
enigma.init()
  ```
This starts an endless loop where you can enter Text in the Terminal and the Enigma will encrypt it.

<br>
<br>

```python
enigma.configuration_from_file("C:/Users/Name/input.txt")
enigma.configuration_to_file("C:/Users/Name/output.txt")
```
You can also load a previously saved configuration from a Text-File.
