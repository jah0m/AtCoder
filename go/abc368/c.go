package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
)

var iost *Iost

type Iost struct {
	Scanner *bufio.Scanner
	Writer  *bufio.Writer
}

func NewIost(fp io.Reader, wfp io.Writer) *Iost {
	const BufSize = 2000005
	scanner := bufio.NewScanner(fp)
	scanner.Split(bufio.ScanWords)
	scanner.Buffer(make([]byte, BufSize), BufSize)
	return &Iost{Scanner: scanner, Writer: bufio.NewWriter(wfp)}
}
func (i *Iost) Text() string {
	if !i.Scanner.Scan() {
		panic("scan failed")
	}
	return i.Scanner.Text()
}
func (i *Iost) Atoi(s string) int         { x, _ := strconv.Atoi(s); return x }
func (i *Iost) Itoa(x int) string         { return strconv.Itoa(x) }
func (i *Iost) GetNextInt() int           { return i.Atoi(i.Text()) }
func (i *Iost) Atoi64(s string) int64     { x, _ := strconv.ParseInt(s, 10, 64); return x }
func (i *Iost) GetNextInt64() int64       { return i.Atoi64(i.Text()) }
func (i *Iost) Atof64(s string) float64   { x, _ := strconv.ParseFloat(s, 64); return x }
func (i *Iost) GetNextFloat64() float64   { return i.Atof64(i.Text()) }
func (i *Iost) Print(x ...any)            { fmt.Fprint(i.Writer, x...) }
func (i *Iost) Printf(s string, x ...any) { fmt.Fprintf(i.Writer, s, x...) }
func (i *Iost) Println(x ...any)          { fmt.Fprintln(i.Writer, x...) }
func max[T ~int | ~int64](a, b T) T {
	if a < b {
		return b
	}
	return a
}

func min[T ~int | ~int64](a, b T) T { return -max(-a, -b) }
func abs[T ~int | ~int64](a T) T    { return max(a, -a) }
func main() {
	fp := os.Stdin
	wfp := os.Stdout
	iost = NewIost(fp, wfp)
	defer func() {
		iost.Writer.Flush()
	}()
	solve()
}
func solve() {
	N := iost.GetNextInt()

	H := make([]int, N)
	for i := 0; i < N; i++ {
		H[i] = iost.GetNextInt()
	}

	T := 0
	for i := 0; i < N; i++ {
		for H[i] >= 1 {
			for T%3 != 0 && H[i] >= 1 {
				T++
				if T%3 == 0 {
					H[i] -= 3
				} else {
					H[i]--
				}
			}
			if H[i] >= 5 {
				T += (H[i] / 5) * 3
				H[i] %= 5
			} else if H[i] == 4 {
				T += 3
				H[i] = 0
			} else if H[i] > 0 {
				T += H[i]
				H[i] = 0
			}
		}
	}

	iost.Println(T)
}
