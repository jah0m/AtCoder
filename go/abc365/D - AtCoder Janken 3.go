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
func isLocal() bool                               { return os.Getenv("NICKEL") == "BACK" }
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
	if isLocal() {
		fp, _ = os.Open(os.Getenv("WELL_EVERYBODY_LIES_TOO_MUCH"))
	}
	iost = NewIost(fp, wfp)
	defer func() {
		iost.Writer.Flush()
	}()
	solve()
}

func solve() {
	n := iost.GetNextInt()
	s := iost.Text()

	M := map[byte]int{'R': 0, 'P': 1, 'S': 2}

	dp := make([][3]int, n+1)
	dp[0][0] = 0
	dp[0][1] = 0
	dp[0][2] = 0
	for i := range s {
		i++
		// j 代表当前手势 0, 1, 2 分别代表 R, P, S 石头<布<剪刀
		for j := 0; j < 3; j++ {
			//不能输，所以输得情况不考虑
			if j == (M[s[i-1]]+2)%3 {
				continue
			}
			//那么当前能否得分取决可以通过beat函数判断
			//获取上一轮与当前轮不同手势的最大值，然后加上当前手势的得分
			dp[i][j] = max(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3]) + beat(j, M[s[i-1]])
		}

	}
	ans := 0
	for i := 0; i < 3; i++ {
		ans = max(ans, dp[n][i])
	}
	iost.Println(ans)
}

func beat(a, b int) int {
	if a == (b+1)%3 {
		return 1
	}
	return 0
}
