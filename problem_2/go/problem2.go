package main

import "fmt"

func fibonacci() func() int {
	a, b := 1, 1
	return func() int {
		a, b = b, a+b
		return a
	}
}

func main() {
	sum := 0
	fib := fibonacci()
	f := fib()

	for ; f < 4000000; f = fib() {
		if f%2 == 0 {
			sum += f
		}
	}

	fmt.Println(sum)
}
