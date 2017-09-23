
Alt & Space::Send, {vkF3sc029} ;Alt+Space->IME ON/OFF

#UseHook  ; Needed for remapping keys to each other, e.g. A becomes B, and B becomes A.
SetStoreCapslockMode Off  ; Optional. Allows Capslock to be ON to send remapped keys in uppercase.
+VKF4::~
 VKF4::`
 VKF3::`
+2::Send,{@}
+6::Send,{^}
+7::&
+8::*
+9::(
+0::)
+-::_
+^::+
 ^::=
+@::{
 @::[
+[::}
 [::]
+;::Send,{:}
:::Send,{'}
*::Send,{"}
+]::|
 ]::\
\::BS
