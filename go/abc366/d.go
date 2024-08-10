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
func (i *Iost) Atoi(s string) int                 { x, _ := strconv.Atoi(s); return x }
func (i *Iost) GetNextInt() int                   { return i.Atoi(i.Text()) }
func (i *Iost) Atoi64(s string) int64             { x, _ := strconv.ParseInt(s, 10, 64); return x }
func (i *Iost) GetNextInt64() int64               { return i.Atoi64(i.Text()) }
func (i *Iost) Atof64(s string) float64           { x, _ := strconv.ParseFloat(s, 64); return x }
func (i *Iost) GetNextFloat64() float64           { return i.Atof64(i.Text()) }
func (i *Iost) Print(x ...interface{})            { fmt.Fprint(i.Writer, x...) }
func (i *Iost) Printf(s string, x ...interface{}) { fmt.Fprintf(i.Writer, s, x...) }
func (i *Iost) Println(x ...interface{})          { fmt.Fprintln(i.Writer, x...) }
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
	A := make([][][]int, N+1)
	for i := range A {
		A[i] = make([][]int, N+1)
		for j := range A[i] {
			A[i][j] = make([]int, N+1)
		}
	}
	for x := 1; x <= N; x++ {
		for y := 1; y <= N; y++ {
			for z := 1; z <= N; z++ {
				A[x][y][z] = iost.GetNextInt()
			}
		}
	}

	S := make([][][]int, N+1)
	for i := range S {
		S[i] = make([][]int, N+1)
		for j := range S[i] {
			S[i][j] = make([]int, N+1)
		}
	}

	for x := 1; x <= N; x++ {
		for y := 1; y <= N; y++ {
			for z := 1; z <= N; z++ {
				S[x][y][z] = A[x][y][z] +
					S[x-1][y][z] +
					S[x][y-1][z] +
					S[x][y][z-1] -
					S[x-1][y-1][z] -
					S[x-1][y][z-1] -
					S[x][y-1][z-1] +
					S[x-1][y-1][z-1]
			}
		}
	}

	Q := iost.GetNextInt()
	for i := 0; i < Q; i++ {
		Lx := iost.GetNextInt()
		Rx := iost.GetNextInt()
		Ly := iost.GetNextInt()
		Ry := iost.GetNextInt()
		Lz := iost.GetNextInt()
		Rz := iost.GetNextInt()

		result := S[Rx][Ry][Rz] -
			S[Lx-1][Ry][Rz] -
			S[Rx][Ly-1][Rz] -
			S[Rx][Ry][Lz-1] +
			S[Lx-1][Ly-1][Rz] +
			S[Lx-1][Ry][Lz-1] +
			S[Rx][Ly-1][Lz-1] -
			S[Lx-1][Ly-1][Lz-1]

		iost.Println(result)
	}
}
