package main

import (
	"fmt"
)

func main() {
	var y int
	fmt.Scan(&y)

	if y%4 == 0 && y%100 != 0 || y%400 == 0 {
		fmt.Println("366")
	} else {
		fmt.Println("365")
	}
}
