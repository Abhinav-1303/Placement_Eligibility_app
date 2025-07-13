var a = 10
var b = 20

document.writeln(a+b)// we can add subtarct etc like this
document.writeln("<br>")
document.writeln(b%a)

b++
a--
document.writeln("<br>")
document.writeln(b + "<br>")
document.writeln(a)

document.writeln(a**2)
document.writeln(b**3)

var x = 12
x+=4
document.writeln("<br>" + x) //gives 4+12 = 16

result = x%5 // 16/5 = 15 remainder will be 1 on result
document.writeln("<br>" + result)

var c = 3
var d = "3"
document.writeln("<br>" + (c==d) + "<br>" + (c===d)) // == checks only value, === checks data type also as "" inside this is string

var h = 19
var k = 22
document.writeln("<br>" + (h<k) + "<br>" + (h>k))

var s = 20
var r = 20
document.writeln("<br>" + (r==20 && s==20))
document.writeln("<br>"+ (!(a==20)))