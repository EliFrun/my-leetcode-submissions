func rearrangeBarcodes(barcodes []int) []int {
    counts := map[int]int{}
    
    for _, v := range(barcodes) {
        if _, ok := counts[v]; ok {
            counts[v]++
        } else {
            counts[v] = 1
        }
    }
    rank := rankByCount(counts)
    ret := make([]int, len(barcodes))
    curr := 0
    for len(rank) > 0 {
        key, value := rank[0].Key, rank[0].Value
        for i, j := curr, 0; j < value; i, j = i + 2, j + 1 {
            if i >= len(barcodes) {
                i = 1
            }
            curr = i
            ret[i] = key
        }
        curr += 2
        rank = rank[1:]
    }
    return ret
}

func rankByCount(wordFrequencies map[int]int) PairList{
  pl := make(PairList, len(wordFrequencies))
  i := 0
  for k, v := range wordFrequencies {
    pl[i] = Pair{k, v}
    i++
  }
  sort.Sort(sort.Reverse(pl))
  return pl
}

type Pair struct {
  Key int
  Value int
}

type PairList []Pair

func (p PairList) Len() int { return len(p) }
func (p PairList) Less(i, j int) bool { return p[i].Value < p[j].Value }
func (p PairList) Swap(i, j int){ p[i], p[j] = p[j], p[i] }
